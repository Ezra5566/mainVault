"""FastAPI deployment of the trained model."""

import os
import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.models.custom_model import CustomModel
from src import config

# -------------------------------------------------
# Initialize FastAPI app
# -------------------------------------------------
app = FastAPI()

# -------------------------------------------------
# Request schema
# -------------------------------------------------
class PredictionRequest(BaseModel):
    """Feature vector for a single prediction."""
    features: list[float]  # Expect a flat list of input dimensions


# -------------------------------------------------
# Load the best model at startup
# -------------------------------------------------
def load_model() -> CustomModel:
    """Load the best checkpoint (model_best.pth) and return a ready model."""
    if not os.path.exists("model_best.pth"):
        raise FileNotFoundError("Model checkpoint 'model_best.pth' not found. Train the model first.")
    checkpoint = torch.load("model_best.pth", map_location="cpu")
    # Extract model hyperparameters from checkpoint (if stored) or use defaults
    model_state = checkpoint
    # Reconstruct input dimension from checkpoint keys (if saved) - assume 'input_dim' stored
    # For simplicity, assume input_dim = 100 (must match training)
    input_dim = checkpoint.get("input_dim", 100)
    hidden_dims = checkpoint.get("hidden_dims", [128, 64, 32])
    output_dim = checkpoint.get("output_dim", 2)
    dropout = checkpoint.get("dropout", 0.3)
    activation = checkpoint.get("activation", "relu")

    model = CustomModel(
        input_dim=input_dim,
        hidden_dims=hidden_dims,
        output_dim=output_dim,
        dropout=dropout,
        activation=activation,
    )
    model.load_state_dict(model_state)
    model.eval()
    return model


# Load model once when the module is imported (global)
try:
    model = load_model()
    logger = None  # Lazy init if not present
except Exception as exc:
    # If loading fails (e.g., model not trained yet), set model to None and log later if needed
    model = None
    # We'll handle inference errors gracefully
# -------------------------------------------------
# Inference endpoint
# -------------------------------------------------
@app.post("/predict")
def predict(request: PredictionRequest):
    """Run inference on a single feature vector."""
    if model is None:
        raise HTTPException(status_code=500, detail="Model is not loaded. Train the model first.")
    try:
        # Convert list to tensor
        x = torch.tensor(request.features, dtype=torch.float32)
        # Ensure correct shape: (1, input_dim)
        if x.dim() != 2:
            x = x.view(1, -1)
        with torch.no_grad():
            logits = model(x)
            probs = torch.nn.functional.softmax(logits, dim=1)
        # Return probabilities for each class
        return {"probabilities": probs.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# -------------------------------------------------
# Simple health check
# -------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}