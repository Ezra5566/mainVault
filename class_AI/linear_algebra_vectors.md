---
title: Linear Algebra – Vectors
tags: [math, linear-algebra, week2-4, vectors]
week: 2
---

## What Is a Vector?
- An **ordered list of numbers** (scalars) that represents magnitude and direction.  
- Notation: **v** = [v₁, v₂, …, vₙ]ᵀ (column vector) or **v** = (v₁, v₂, …, vₙ) (row vector).  
- **Dimension (or length)**: Number of components (e.g., a 3‑D vector has 3 components).

## Basic Operations
| Operation | Symbol | Description |
|----------|--------|-------------|
| **Addition** | **v + w** | Component‑wise addition; geometrically, place vectors head‑to‑tail. |
| **Scalar Multiplication** | **α v** | Scales magnitude; reverses direction if α < 0. |
| **Dot Product** | **v·w** = Σ vᵢwᵢ | Returns a scalar; measures similarity/orthogonality. |
| **Cross Product** (3‑D only) | **v × w** | Returns a vector orthogonal to both; magnitude = area of parallelogram. |
| **Norm (Length)** | **‖v‖** = √(v·v) | Euclidean length; generalizations include L¹ and Lᵢ norms. |
| **Unit Vector** | **û** = v/‖v‖ | Normalized direction; used for angles and projections. |

## Geometric Interpretation
- **Direction & Magnitude**: Visualize vectors as arrows in 2‑D or 3‑D space.  
- **Angle Between Vectors**: cos θ = (v·w) / (‖v‖‖w‖).  
- **Projection**: proj₍w₎ v = (v·w / ‖w‖²) w – component of **v** along **w**.

## Why Vectors Matter in AI
- **Feature Representation** – Data points (e.g., images, texts) are encoded as high‑dimensional vectors.  
- **Neural‑Network Input** – Weight matrices multiply input vectors to produce activations.  
- **Geometric Intuition** – Concepts like similarity, orthogonality, and projection underpin algorithms such as cosine similarity, PCA, and attention mechanisms.

## Quick Exercises
1. Compute the dot product of **a** = [1, 2, 3]ᵀ and **b** = [4, ‑1, 0]ᵀ.  
2. Find the unit vector of **c** = [3, 4]ᵀ.  
3. Determine whether **d** = [1, 2]ᵀ and **e** = [‑2, 1]ᵀ are orthogonal.

---

---

> **Cluster hub:** see [[Generative AI - Map of Content]] for the full AI/ML map of content and study path.
