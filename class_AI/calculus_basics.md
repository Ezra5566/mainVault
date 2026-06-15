---
title: Calculus Basics for AI
tags: [math, calculus, week2-4, gradients]
week: 2
---

## Why Calculus Matters in AI
- **Model Training**: Most AI learning algorithms use **gradient‑based optimization** to minimize loss functions.  
- **Understanding Change**: Derivatives quantify how a function behaves locally—essential for interpreting model behavior and debugging.

## Core Concepts

### 1. Derivatives
- **Definition**: The derivative of a function *f* at *x* measures the rate of change as *x* varies.
- **Notation**: *f′(x)* or *df/dx*.
- **Geometric Meaning**: Slope of the tangent line to the graph of *f* at *x*.
- **Simple Example**:  
  - *f(x) = x²* ⇒ *f′(x) = 2x*.

### 2. Partial Derivatives
- **Multi‑Variable Functions**: When *f(x₁, x₂, …, xₙ)*, the partial derivative with respect to *xᵢ* holds all other variables constant.
- **Notation**: ∂f/∂xᵢ.
- **Example**:  
  - *f(x, y) = x²y* ⇒ ∂f/∂x = 2xy, ∂f/∂y = x².

### 3. Gradients
- **Vector of Partial Derivatives**: ∇*f* = [∂f/∂x₁, ∂f/∂x₂, …, ∂f/∂xₙ].
- **Interpretation**: Points in the direction of steepest ascent; opposite direction points to steepest descent.
- **Role in AI**: Gradient descent updates model parameters *θ* as *θ ← θ – α∇L(θ)* (α = learning rate, L = loss).

### 4. Chain Rule
- **Purpose**: Compute derivatives of composite functions.
- **Formula**: If *y = f(g(x))*, then *dy/dx = f′(g(x))·g′(x)*.
- **Multi‑Variable Version**: ∂(f∘g)/∂x = ∂f/∂g · ∂g/∂x.
- **AI Example**: Back‑propagation through layers of a neural network uses the chain rule to propagate error gradients.

### 5. Integrals (Brief Overview)
- **Definite Integral**: ∫ₐᵇ f(x) dx = area under the curve from *a* to *b*.  
- **Indefinite Integral**: ∫ f(x) dx = set of antiderivatives + constant.
- **Why It Appears**: Expected value calculations, probability density functions, and continuous‑action reinforcement learning involve integration.

## Visual Intuition
```
          f(x)
           |
           |   tangent line
           |  slope = f′(x)
           |
   ────────┼──────── x
```
- The steeper the slope, the larger the gradient magnitude.

## Practical Takeaways for AI Students
1. **Compute Gradients**: When coding from scratch, use automatic differentiation libraries (e.g., JAX, PyTorch `autograd`) to avoid manual calculus errors.  
2. **Visualize Gradients**: Plot loss curves and gradient magnitudes to detect issues like vanishing/exploding gradients.  
3. **Learning Rate Tuning**: Gradient magnitude guides the scale of parameter updates; too large → divergence, too small → slow convergence.  
4. **Higher‑Order Derivatives**: Some advanced optimizers (e.g., Newton’s method) use second‑order derivatives (Hessian) for faster convergence, though they are computationally heavier.

---

### Quick Exercises
1. Find the derivative of *f(x) = 3x³ – 5x + 2*.  
2. Compute the gradient of *f(x, y) = x²y + eʸ*.  
3. Apply the chain rule to *h(x) = sin(x²)*. What is *h′(x)*?  

---