"""Model training pipeline."""

import os
import logging
import pandas as pd
import torch
from torch.utils.data import DataLoader, Dataset
from src.models.custom_model import CustomModel
from src import config
import torch.nn.functional as F
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ----------------------------------------------------------------------
# Dataset class for PyTorch
# ----------------------------------------------------------------------
class FeatureDataset(Dataset):
    def __init__(self, df: pd.DataFrame, target_col: str):
        self.features = df.drop(columns=[target_col]).values.astype('float32')
        self.labels = df[target_col].values.astype('long')
        self.size = len(self.labels)

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return torch.tensor(self.features[idx]), torch.tensor(self.labels[idx])

# ----------------------------------------------------------------------
# Training loop utilities
# ----------------------------------------------------------------------
def train_one_epoch(model, dataloader, optimizer, criterion, device):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    for inputs, labels in dataloader:
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * inputs.size(0)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    epoch_loss = running_loss / total
    epoch_acc = correct / total
    return epoch_loss, epoch_acc

def validate_one_epoch(model, dataloader, criterion, device):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in dataloader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            running_loss += loss.item() * inputs.size(0)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    val_loss = running_loss / total
    val_acc = correct / total
    return val_loss, val_acc

# ----------------------------------------------------------------------
# Main training function
# ----------------------------------------------------------------------
def main(args):
    # Load processed features
    logger.info("Loading processed features...")
    processed_df = pd.read_parquet("data/processed/features.parquet")
    # Assume target column is the last column in the parquet, or we could read a separate label file
    # For simplicity, suppose there is a column named 'label' in the processed data
    target_col = "label"
    if target_col not in processed_df.columns:
        raise ValueError(f"Target column '{target_col}' not found in processed data.")
    
    # Split train/val
    train_frac = 0.8
    train_df = processed_df.sample(frac=train_frac, random_state=42)
    val_df = processed_df.drop(train_df.index)

    train_dataset = FeatureDataset(train_df, target_col)
    val_dataset = FeatureDataset(val_df, target_col)

    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True, num_workers=2)
    val_loader = DataLoader(val_dataset, batch_size=args.batch_size, shuffle=False, num_workers=2)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info(f"Using device: {device}")

    # Model instantiation
    model = CustomModel(
        input_dim=train_df.drop(columns=[target_col]).shape[1],
        hidden_dims=args.hidden_dims,
        output_dim=2,  # binary classification assumed
        dropout=args.dropout,
        activation="relu",
    ).to(device)

    logger.info(f"Model architecture:\n{model}")

    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)
    criterion = torch.nn.CrossEntropyLoss()

    best_val_acc = 0.0
    for epoch in range(1, args.epochs + 1):
        logger.info(f"--- Epoch {epoch}/{args.epochs} ---")
        train_loss, train_acc = train_one_epoch(model, train_loader, optimizer, criterion, device)
        val_loss, val_acc = validate_one_epoch(model, val_loader, criterion, device)

        logger.info(f"Train Loss: {train_loss:.4f} | Train Acc: {train_acc:.4f}")
        logger.info(f"Val   Loss: {val_loss:.4f} | Val   Acc: {val_acc:.4f}")

        # Save checkpoint
        checkpoint_path = f"checkpoints/epoch_{epoch}.pth"
        os.makedirs("checkpoints", exist_ok=True)
        torch.save({
            "epoch": epoch,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "train_loss": train_loss,
            "val_loss": val_loss,
            "train_acc": train_acc,
            "val_acc": val_acc,
        }, checkpoint_path)

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), "model_best.pth")
            logger.info(f"New best model saved (Val Acc: {best_val_acc:.4f})")

    # Save final model for inference
    torch.save(model, "model_final.pth")
    logger.info("Training complete. Final model saved as model_final.pth")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train custom PyTorch model")
    parser.add_argument("--epochs", type=int, default=10, help="Number of training epochs")
    parser.add_argument("--batch_size", type=int, default=64, help="Batch size")
    parser.add_argument("--lr", type=float, default=0.001, help="Learning rate")
    parser.add_argument("--dropout", type=float, default=0.3, help="Dropout probability")
    parser.add_argument("--hidden_dims", type=str, default="128,64,32", help="Comma-separated hidden dimensions")
    args = parser.parse_args()

    # Convert hidden_dims string to list of ints
    args.hidden_dims = [int(d) for d in args.hidden_dims.split(",") if d.strip()]
    main(args)