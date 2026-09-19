---
title: Linear Algebra – Matrices
tags: [math, linear-algebra, week2-4, matrices]
week: 2
---

## What Is a Matrix?
- A **matrix** is a rectangular array of numbers arranged in rows and columns.  
- Notation: **A** ∈ ℝᵐˣⁿ (m rows, n columns).  
- **Square matrix**: m = n.  
- **Row vector**: 1 × n. **Column vector**: n × 1.

## Common Types
| Type | Description |
|------|-------------|
| **Diagonal** | Non‑zero entries only on the main diagonal. |
| **Identity (I)** | Diagonal matrix with 1’s on the diagonal; acts as multiplicative identity. |
| **Zero matrix** | All entries are 0. |
| **Symmetric** | A = Aᵀ (equal to its transpose). |
| **Orthogonal** | AᵀA = I (preserves length and angles). |

## Basic Operations
1. **Addition** – Component‑wise; matrices must share the same dimensions.  
2. **Scalar Multiplication** – Multiply every entry by a scalar α.  
3. **Transpose (Aᵀ)** – Rows become columns and vice‑versa.  
4. **Matrix Multiplication (AB)** – Dot‑product of rows of A with columns of B; result dimension m × p if A is m × n and B is n × p.  
   - Not commutative; associativity holds ( (AB)C = A(BC) ).
5. **Determinant (det A)** – Scalar that encodes volume scaling; defined for square matrices.  
6. **Inverse (A⁻¹)** – Matrix such that A⁻¹A = I; exists only if det A ≠ 0.  

## Applications in AI
- **Weight Matrices** in neural networks: each layer performs **y = Wx + b**, where **W** is a matrix mapping input vector **x** to output vector **y**.  
- **Linear Transformations**: Matrices encode rotations, scalings, and projections that underpin concepts like PCA (Principal Component Analysis).  
- **Embedding Spaces**: Word embeddings, image feature maps, and graph representations are stored as matrices of shape (n_samples, embedding_dim).  

## Quick Exercises
1. Multiply a 2 × 3 matrix **A** by a 3 × 2 matrix **B**. What are the dimensions of **AB**?  
2. Compute the determinant of \(\begin{bmatrix}2 & 0\\ 1 & 3\end{bmatrix}\).  
3. Find the transpose of \(\begin{bmatrix}1 & 2 & 3\end{bmatrix}\) (row vector).  

---

---

> **Cluster hub:** see [[Generative AI - Map of Content]] for the full AI/ML map of content and study path.
