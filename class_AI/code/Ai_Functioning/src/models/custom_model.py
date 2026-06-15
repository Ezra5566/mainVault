"""Custom PyTorch model architecture."""

import torch
import torch.nn as nn
import torch.nn.functional as F

class CustomModel(nn.Module):
    """
    A flexible feed‑forward model with:
    - Configurable hidden layers
    - Optional dropout
    - Customizable activation
    - Built‑in support for multi‑class or binary classification
    """

    def __init__(
        self,
        input_dim: int,
        hidden_dims: list[int],
        output_dim: int,
        dropout: float = 0.3,
        activation: str = "relu",
    ):
        """
        Args:
            input_dim: Dimensionality of input features.
            hidden_dims: List of hidden layer sizes, e.g. [128, 64, 32].
            output_dim: Number of target classes.
            dropout: Dropout probability applied after each hidden layer.
            activation: Activation function name ('relu', 'gelu', 'tanh').
        """
        super().__init__()
        # Build layers dynamically
        layer_sizes = [input_dim] + hidden_dims + [output_dim]
        self.layers = nn.ModuleList()
        self.activations = {"relu": nn.ReLU(), "gelu": nn.GELU(), "tanh": nn.Tanh()}
        self.dropout = nn.Dropout(dropout)

        for i in range(len(layer_sizes) - 1):
            self.layers.add_module(f"linear_{i}", nn.Linear(layer_sizes[i], layer_sizes[i + 1]))
            # Store activation for later use in forward
            if i < len(hidden_dims):
                self.custom_activation = self.activations[activation]

    def forward(self, x):
        """
        Forward pass through the network.

        Args:
            x: Input tensor of shape (batch_size, input_dim).

        Returns:
            Logits tensor of shape (batch_size, output_dim).
        """
        for i, layer in enumerate(self.layers):
            x = layer(x)
            # Apply activation after each hidden layer, not after final output
            if i < len(self.layers) - 1:  # not the last layer
                x = self.custom_activation(x)
                x = self.dropout(x)
        return x

# ---------------------------------------------------------------------------
# Example usage (can be removed in production)
if __name__ == "__main__":
    # Dummy input to sanity‑check shapes
    dummy_input = torch.randn(4, 100)  # batch_size=4, 100‑dim input
    model = CustomModel(
        input_dim=100,
        hidden_dims=[128, 64, 32],
        output_dim=2,
        dropout=0.3,
        activation="relu",
    )
    logits = model(dummy_input)
    print(f"Logits shape: {logits.shape}")