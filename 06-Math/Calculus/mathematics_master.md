# Mathematics Master Curriculum

## A Comprehensive Educational Reference Document

---

# Table of Contents

1. [Arithmetic & Number Theory Basics](#1-arithmetic--number-theory-basics)
2. [Elementary Algebra](#2-elementary-algebra)
3. [Geometry & Trigonometry](#3-geometry--trigonometry)
4. [Linear Algebra](#4-linear-algebra)
5. [Calculus (Differential & Integral)](#5-calculus-differential--integral)
6. [Multivariable Calculus](#6-multivariable-calculus)
7. [Differential Equations](#7-differential-equations)
8. [Statistics & Probability](#8-statistics--probability)
9. [Discrete Mathematics](#9-discrete-mathematics)
10. [Real Analysis](#10-real-analysis)
11. [Abstract Algebra](#11-abstract-algebra)
12. [Topology](#12-topology)
13. [Complex Analysis](#13-complex-analysis)
14. [Number Theory](#14-number-theory)
15. [Mathematical Logic](#15-mathematical-logic)
16. [Information Theory](#16-information-theory)
17. [Numerical Analysis](#17-numerical-analysis)
18. [Optimization](#18-optimization)
19. [Graph Theory](#19-graph-theory)
20. [Mathematical Foundations for AI/ML](#20-mathematical-foundations-for-aiml)

---

# 1. Arithmetic & Number Theory Basics

## Learning Objectives

- Understand fundamental operations with integers, rational, and real numbers
- Master number theory concepts including divisibility, prime numbers, and modular arithmetic
- Develop number sense and estimation skills
- Apply arithmetic operations to solve real-world problems

## Key Concepts and Definitions

### Number Systems

```
┌─────────────────────────────────────────────────────────────┐
│                    NUMBER SYSTEMS                           │
├─────────────────────────────────────────────────────────────┤
│  ℕ  = {1, 2, 3, 4, ...}        Natural Numbers              │
│  ℤ  = {..., -2, -1, 0, 1, 2}   Integers                     │
│  ℚ  = {a/b | a,b ∈ ℤ, b≠0}    Rational Numbers             │
│  ℝ  = All decimal expansions   Real Numbers                │
│  ℂ  = {a + bi | a,b ∈ ℤ}      Complex Numbers               │
└─────────────────────────────────────────────────────────────┘
```

### Divisibility

A number *a* divides *b* (denoted *a | b*) if ∃ *k* ∈ ℤ such that *b = ak*.

### Prime Numbers

A prime number is a natural number greater than 1 with exactly two positive divisors: 1 and itself.

## Important Formulas and Theorems

### Fundamental Theorem of Arithmetic

Every integer *n > 1* can be uniquely expressed as:

```
n = p₁^e₁ × p₂^e₂ × p₃^e₃ × ... × pₖ^eₖ
```

where *pᵢ* are distinct primes and *eᵢ* are positive integers.

### Euclidean Algorithm

For integers *a* and *b*:

```
gcd(a, b) = gcd(b, a mod b)
```

### Modular Arithmetic

```
(a + b) mod n = ((a mod n) + (b mod n)) mod n
(a × b) mod n = ((a mod n) × (b mod n)) mod n
```

## Worked Examples

### Example 1: Finding GCD using Euclidean Algorithm

Find gcd(252, 105):

```
Step 1: 252 = 105 × 2 + 42     → 252 mod 105 = 42
Step 2: 105 = 42 × 2 + 21     → 105 mod 42 = 21  
Step 3: 42 = 21 × 2 + 0       → Stop
```

Therefore, **gcd(252, 105) = 21**

### Example 2: Prime Factorization

Express 180 as a product of primes:

```
180 ÷ 2 = 90
90 ÷ 2 = 45
45 ÷ 3 = 15
15 ÷ 3 = 5
5 ÷ 5 = 1

180 = 2² × 3² × 5
```

### Example 3: Modular Arithmetic Computation

Calculate (47 + 58) mod 13:

```
47 mod 13 = 8   (since 47 = 13 × 3 + 8)
58 mod 13 = 6   (since 58 = 13 × 4 + 6)
(8 + 6) mod 13 = 14 mod 13 = 1
```

Therefore, **(47 + 58) mod 13 = 1**

## AI/ML Applications

- **Cryptography**: Modular arithmetic is fundamental to RSA, AES, and blockchain algorithms
- **Hash Functions**: Number theory enables cryptographic hash functions used in machine learning model versioning
- **Random Number Generation**: Linear congruential generators rely on modular arithmetic

---

# 2. Elementary Algebra

## Learning Objectives

- Manipulate algebraic expressions including polynomials
- Solve linear and quadratic equations
- Understand functions and their properties
- Apply algebraic problem-solving techniques

## Key Concepts and Definitions

### Algebraic Expressions

An algebraic expression combines numbers, variables, and operations:

```
3x² + 2x - 7    (polynomial of degree 2)
√(x + 1)       (radical expression)
```

### Functions

A function *f: A → B* assigns each element *x ∈ A* exactly one element *f(x) ∈ B*:

```
f(x) = ax + b           Linear function
f(x) = ax² + bx + c     Quadratic function
```

## Important Formulas and Theorems

### Quadratic Formula

For *ax² + bx + c = 0* (where *a ≠ 0*):

```
x = (-b ± √(b² - 4ac)) / 2a
```

### Binomial Theorem

```
(x + y)ⁿ = Σₖ₌₀ⁿ C(n,k) × xⁿ⁻ᵏ × yᵏ

where C(n,k) = n! / (k!(n-k)!)
```

### Difference of Squares

```
a² - b² = (a + b)(a - b)
```

## Worked Examples

### Example 1: Solving a Quadratic Equation

Solve *2x² - 5x - 3 = 0*:

```
a = 2, b = -5, c = -3
Discriminant: b² - 4ac = (-5)² - 4(2)(-3) = 25 + 24 = 49

x = (5 ± √49) / (2×2) = (5 ± 7) / 4

x₁ = (5 + 7)/4 = 12/4 = 3
x₂ = (5 - 7)/4 = -2/4 = -1/2
```

**Solution: x = 3 or x = -½**

### Example 2: Simplifying an Expression

Simplify *(x² - 4x + 3)/(x - 1)*:

```
x² - 4x + 3 = (x - 1)(x - 3)  [factor]

(x² - 4x + 3)/(x - 1) = ((x - 1)(x - 3))/(x - 1) = x - 3
```

### Example 3: Evaluating a Function

Given *f(x) = 2x² - 3x + 1*, find *f(2) + f(-1)*:

```
f(2) = 2(4) - 3(2) + 1 = 8 - 6 + 1 = 3
f(-1) = 2(1) - 3(-1) + 1 = 2 + 3 + 1 = 6

f(2) + f(-1) = 3 + 6 = 9
```

## AI/ML Applications

- **Loss Functions**: Quadratic loss (MSE) uses quadratic equations
- **Polynomial Regression**: Fitting polynomial functions to data
- **Activation Functions**: Algebraic expressions used in neural networks (ReLU, sigmoid)

---

# 3. Geometry & Trigonometry

## Learning Objectives

- Master geometric principles and proofs
- Understand trigonometric ratios and identities
- Apply geometry to solve spatial problems
- Connect geometry to coordinate systems

## Key Concepts and Definitions

### Fundamental Geometric Shapes

```
Triangle: 3 sides, sum of angles = 180°
Quadrilateral: 4 sides, sum of angles = 360°
Circle: set of points equidistant from center
```

### Trigonometric Ratios (Right Triangle)

```
sin(θ) = opposite / hypotenuse
cos(θ) = adjacent / hypotenuse  
tan(θ) = opposite / adjacent
```

## Important Formulas and Theorems

### Pythagorean Theorem

For a right triangle with legs *a*, *b* and hypotenuse *c*:

```
a² + b² = c²
```

### Area Formulas

```
Triangle: A = ½ × base × height
Rectangle: A = length × width
Circle: A = πr²
```

### Trigonometric Identities

```
sin²(θ) + cos²(θ) = 1
tan(θ) = sin(θ)/cos(θ)
sin(2θ) = 2sin(θ)cos(θ)
```

### Law of Sines and Cosines

```
Law of Sines: a/sin(A) = b/sin(B) = c/sin(C)
Law of Cosines: c² = a² + b² - 2ab·cos(C)
```

## Worked Examples

### Example 1: Finding Unknown Side

In a right triangle, one leg = 3, hypotenuse = 5. Find the other leg:

```
a² + b² = c²
3² + b² = 5²
9 + b² = 25
b² = 16
b = 4
```

### Example 2: Trigonometric Calculation

Find sin(45°) and cos(45°):

```
sin(45°) = √2/2 ≈ 0.707
cos(45°) = √2/2 ≈ 0.707
```

### Example 3: Using Law of Cosines

In triangle with sides a=7, b=9, angle C=60°, find c:

```
c² = a² + b² - 2ab·cos(C)
c² = 49 + 81 - 2(7)(9)(0.5)
c² = 130 - 63 = 67
c = √67 ≈ 8.19
```

## ASCII Illustrations

### Coordinate Plane

```
           y
           │
     (-2,3)│•(0,3)    (2,3)
           │
    (-2,0) │•────────(2,0)───► x
           │
     (-2,-3)│•(0,-3)  (2,-3)
           │
```

### Unit Circle and Reference Angles

```
           y
           │    90°
      (-1,0)┼────────(1,0)
           │    180°  0°
           │ \     │     /
           │  \    │    /
    270°───│───\───┼───/──────► 0°
           │     \  │  /
           │      \ │ /
           │       \│/ 
           │        •
```

## AI/ML Applications

- **Computer Vision**: Geometric transformations for image processing
- **Robotics**: Kinematics using trigonometry for motion planning
- **Graphics Programming**: 3D transformations, rotations using matrices

---

# 4. Linear Algebra

## Learning Objectives

- Master matrix operations and properties
- Understand vector spaces and linear transformations
- Solve systems of linear equations
- Apply eigenvalues and eigenvectors

## Key Concepts and Definitions

### Matrices

A matrix is a rectangular array of numbers:

```
A = [aᵢⱼ]  where i = row, j = column

Example (2×3 matrix):
┌         ┐
│ 1  2  3 │
│ 4  5  6 │
└         ┘
```

### Vectors

A vector is a matrix with one row or one column:

```
v = [v₁, v₂, ..., vₙ]ᵀ  (column vector)
```

### Vector Space

A set V with operations + and · satisfying:
- Commutativity: u + v = v + u
- Associativity: (u + v) + w = u + (v + w)
- Additive identity: ∃ 0 ∈ V such that v + 0 = v
- Additive inverse: ∃ -v ∈ V such that v + (-v) = 0
- Distributivity: a(bv) = (ab)v

## Important Formulas and Theorems

### Matrix Operations

```
Matrix Addition: A + B = [aᵢⱼ + bᵢⱼ]
Scalar Multiplication: kA = [kaᵢⱼ]
Matrix Multiplication: (AB)ᵢⱼ = Σₖ aᵢₖ · bₖⱼ
Transpose: (Aᵀ)ᵢⱼ = aⱼᵢ
Determinant: det(A)
```

### Inverse Matrix

```
A⁻¹ exists iff det(A) ≠ 0
A · A⁻¹ = I (identity)
```

### Eigenvalues and Eigenvectors

```
Av = λv

where:
- A is an n×n matrix
- v is a non-zero eigenvector
- λ is the corresponding eigenvalue
```

## Worked Examples

### Example 1: Matrix Multiplication

Multiply:

```
A = [1 2]    B = [3]
    [3 4]        [5]

AB = [1×3 + 2×5] = [13]
     [3×3 + 4×5]   [29]
```

### Example 2: Solving Linear System

Solve:

```
2x + y = 5
x - y = 1

Matrix form: [2 1][x] = [5]
             [1-1][y]   [1]

Using elimination:
2x + y = 5
x - y = 1  →  y = x - 1

2x + (x - 1) = 5
3x = 6
x = 2, y = 1
```

### Example 3: Finding Eigenvalues

Find eigenvalues of A = [2 1]
                        [1 2]

```
det(A - λI) = 0
|[2-λ   1  ]| = 0
|[ 1   2-λ]| = 0

(2-λ)(2-λ) - 1 = 0
λ² - 4λ + 3 = 0
(λ-1)(λ-3) = 0

λ₁ = 1, λ₂ = 3
```

## ASCII Illustrations

### Matrix Representation

```
┌                              ┐
│  a₁₁   a₁₂   a₁₃  ...  a₁ₙ  │  ← row 1
│  a₂₁   a₂₂   a₂₃  ...  a₂ₙ  │  ← row 2
│  a₃₁   a₃₂   a₃₃  ...  a₃ₙ  │  ← row 3
│   .     .     .         .    │
│  aₘ₁   aₘ₂   aₘ₃  ...  aₘₙ  ���  �� row m
└                              ┘
         ↑
       column
```

### Linear Transformation

```
Input Vector     Transformation      Output Vector
    v                T                  T(v)
    
    [₁]           [a b]           [a×₁ + b×₂]
    [₂]    ──►    [c d]    ──►    [c×₁ + d×₂]
```

## AI/ML Applications

- **Neural Networks**: Matrix multiplication for forward pass
- **Principal Component Analysis (PCA)**: Eigenvalue decomposition
- **Natural Language Processing**: Word embeddings as vectors
- **Image Processing**: Convolution as matrix operations

---

# 5. Calculus (Differential & Integral)

## Learning Objectives

- Master limits and continuity
- Understand differentiation and integration
- Apply calculus to solve optimization problems
- Connect derivatives to rates of change

## Key Concepts and Definitions

### Limits

The limit of f(x) as x approaches a is L:

```
lim(x→a) f(x) = L
```

### Derivative

The derivative measures instantaneous rate of change:

```
f'(x) = lim(h→0) [f(x+h) - f(x)] / h
```

### Integral

The integral accumulates area under a curve:

```
∫f(x)dx = F(x) + C    (indefinite)
∫ₐᵇ f(x)dx           (definite)
```

## Important Formulas and Theorems

### Differentiation Rules

```
d/dx [cf(x)] = c·f'(x)
d/dx [f(x) + g(x)] = f'(x) + g'(x)
d/dx [f(x)·g(x)] = f'(x)g(x) + f(x)g'(x)
d/dx [f(g(x))] = f'(g(x))·g'(x)
d/dx [xⁿ] = n·xⁿ⁻¹
```

### Fundamental Theorem of Calculus

```
∫ₐᵇ f(x)dx = F(b) - F(a)

where F'(x) = f(x)
```

### Integration Formulas

```
∫xⁿdx = xⁿ⁺¹/(n+1) + C   (n ≠ -1)
∫(1/x)dx = ln|x| + C
∫eˣdx = eˣ + C
∫sin(x)dx = -cos(x) + C
∫cos(x)dx = sin(x) + C
```

## Worked Examples

### Example 1: Finding Derivative

Differentiate f(x) = 3x⁴ - 2x² + 5x - 1:

```
f'(x) = 12x³ - 4x + 5
```

### Example 2: Computing Definite Integral

Evaluate ∫₀² (x² + 1)dx:

```
∫(x² + 1)dx = x³/3 + x + C

Evaluate from 0 to 2:
= [2³/3 + 2] - [0] = (8/3 + 2) = 14/3
```

### Example 3: Derivative using Chain Rule

Differentiate f(x) = sin(x³):

```
f'(x) = cos(x³) · 3x² = 3x²cos(x³)
```

## ASCII Illustrations

### Derivative as Tangent Line

```
          f(x)
           │
         4 │           •───• (tangent line)
         3 │         •
         2 │       •
         1 │     •
         0 │   •
        -1 │ •
           └─────────────────────► x
             -1  0  1  2  3  4
```

### Integral as Area Under Curve

```
        f(x)
         │ ╲
       4 │  ╲████████████
         │   ╲███████████
       3 │    ╲█████████
         │     ╲████████
       2 │      ╲███████
         │       ╲█████
       1 │        ╲███
         │         ╲█
       0 │          ╲
         └──────────────────► x
           0     1     2
           
        Area = ∫₀² f(x)dx
```

## AI/ML Applications

- **Gradient Descent**: Derivatives for optimization
- **Backpropagation**: Chain rule for neural network training
- **Loss Function Optimization**: Finding minima using calculus
- **Probability Density Functions**: Integration for probability calculations

---

# 6. Multivariable Calculus

## Learning Objectives

- Extend calculus to functions of multiple variables
- Master partial derivatives and multiple integrals
- Understand gradient vectors and directional derivatives
- Apply vector calculus to physical applications

## Key Concepts and Definitions

### Functions of Several Variables

```
f: ℝⁿ → ℝ
f(x₁, x₂, ..., xₙ) = z
```

### Partial Derivatives

```
∂f/∂xᵢ = lim(h→0) [f(x₁, ..., xᵢ+h, ..., xₙ) - f(x₁, ..., xₙ)] / h
```

### Gradient

For f(x, y), the gradient is:

```
∇f = (∂f/∂x, ∂f/∂y)
```

### Multiple Integrals

```
∬f(x,y)dA  (double integral over region)
∭f(x,y,z)dV (triple integral over volume)
```

## Important Formulas and Theorems

### Chain Rule (Multivariable)

```
∂z/∂x = (∂z/∂u)(∂u/∂x) + (∂z/∂v)(∂v/∂x)
```

### Green's Theorem (2D)

```
∮C Pdx + Qdy = ∬D (∂Q/∂x - ∂P/∂y)dA
```

### Stokes' Theorem

```
∮C F·dr = ∬S (∇×F)·n dS
```

### Divergence Theorem

```
∭V (∇·F)dV = ∬∂S F·n dS
```

## Worked Examples

### Example 1: Partial Derivatives

Find ∂f/∂x and ∂f/∂y for f(x,y) = x²y + xy²:

```
∂f/∂x = 2xy + y²
∂f/∂y = x² + 2xy
```

### Example 2: Gradient

Find ∇f for f(x,y) = x² + y²:

```
∇f = (2x, 2y)

At point (1,1): ∇f = (2, 2)
```

### Example 3: Double Integral

Evaluate ∬₀¹∫₀¹ (x + y)dx dy:

```
∫₀¹ (x + y)dx = [x²/2 + yx]₀¹ = 1/2 + y

∫₀¹ (1/2 + y)dy = [y/2 + y²/2]₀¹ = 1/2 + 1/2 = 1
```

## ASCII Illustrations

### 3D Surface

```
                    z
                    │
                4   │    • • •
                    │  •       • •
                3   │ •           • •
                    │•               • •
                2   │                   • •
                    │                     • •
                1   │                       ••
                    └──────────────────────────► y
                     0  1  2  3 4
                     
        x: ─────────────────────────────
```

### Gradient Descent

```
        High ──►  Contour lines  ──► Low
                
                ╭─────╮
               ╱ ╲   ╱ ╲
              ╱   ╲ ╱   ╲
             ╱ •───╮───• ╲
            ╱   ╱ ╲╲╲╲╲╲
           ╱   ╱  ╰─╮  ╲
          ╱   ╱    ╰─╮  ╲
         ╱   ╱•─────╮•──╲
        ╱   ╱        ╰───╲
       ╱   ╱            ╲╲
      ╱   ╱              ╲╲
     ╱   ╱                ╲╲
    ╱   ╱───────────────────╲╲
```

## AI/ML Applications

- **Multivariate Statistics**: Partial derivatives in statistical models
- **Machine Learning Loss Functions**: Gradient descent in high dimensions
- **Neural Network Training**: Computing gradients in weight space
- **Feature Scaling**: Understanding multivariate relationships

---

# 7. Differential Equations

## Learning Objectives

- Understand ordinary differential equations (ODEs)
- Master solution techniques for first-order ODEs
- Apply ODEs to model physical systems
- Solve higher-order linear differential equations

## Key Concepts and Definitions

### Differential Equation

An equation involving derivatives:

```
dy/dx = f(x, y)           (first-order)
d²y/dx² + p(x)dy/dx + q(x)y = r(x)  (second-order)
```

### Order and Degree

- **Order**: Highest derivative order
- **Degree**: Power of highest order (after clearing fractions)

### Solutions

A solution is a function y = f(x) that satisfies the equation.

## Important Formulas and Theorems

### First-Order Linear ODE

```
dy/dx + P(x)y = Q(x)

Integrating factor: μ(x) = e^(∫P(x)dx)

Solution: μ(x)y = ∫μ(x)Q(x)dx + C
```

### Separable Equations

```
dy/dx = g(x)h(y)

Separate: dy/h(y) = g(x)dx
Integrate: ∫dy/h(y) = ∫g(x)dx + C
```

### Second-Order with Constant Coefficients

```
ay'' + by' + cy = 0

Characteristic: ar² + br + c = 0

r = (-b ± √(b²-4ac))/2a
```

### Euler's Method (Numerical)

```
yₙ₊₁ = yₙ + f(xₙ,yₙ)·h
```

## Worked Examples

### Example 1: Solving Separable ODE

Solve dy/dx = xy:

```
dy/y = x dx
∫dy/y = ∫x dx
ln|y| = x²/2 + C
y = Ce^(x²/2)
```

### Example 2: First-Order Linear

Solve dy/dx + 2y = e^x:

```
P(x) = 2, Q(x) = e^x
μ(x) = e^(∫2dx) = e^(2x)

e^(2x)y = ∫e^(2x)e^x dx + C = ∫e^(3x)dx + C = e^(3x)/3 + C

y = e^(-2x)(e^(3x)/3 + C) = e^x/3 + Ce^(-2x)
```

### Example 3: Second-Order Homogeneous

Solve y'' - 5y' + 6y = 0:

```
r² - 5r + 6 = 0
(r-2)(r-3) = 0
r = 2, 3

y = C₁e^(2x) + C₂e^(3x)
```

## ASCII Illustrations

### Growth/Decay Models

```
        Exponential Growth    Exponential Decay
        y=e^(kt)           y=e^(-kt)
        
y │                    y │
  │  ╱                   │╲
  │ ╱                    │ ╲
  │╱                      ╲╲
  └────────→ x            └────────→ x
```

### Solution Curves

```
        dy/dx = x - y
        
y │ •───•───•───•
  │       ╱
  │      ╱
  │     ╱
  │    ╱
  └─────────────► x
      -1    0    1    2
```

## AI/ML Applications

- **Dynamical Systems**: Modeling time-series data
- **Control Systems**: ODEs in feedback systems
- **Neural ODEs**: Continuous-time neural networks
- **State Estimation**: Kalman filters use differential equations

---

# 8. Statistics & Probability

## Learning Objectives

- Understand probability theory and distributions
- Master descriptive and inferential statistics
- Apply statistical tests and confidence intervals
- Connect statistics to machine learning

## Key Concepts and Definitions

### Probability

```
P(A) = |A|/|S|    (classical)
0 ≤ P(A) ≤ 1     (always)
P(A∪B) = P(A) + P(B) - P(A∩B)
```

### Random Variables

- **Discrete**: X takes specific values
- **Continuous**: X takes values in an interval

### Expected Value

```
E[X] = Σₓ x·P(X=x)        (discrete)
E[X] = ∫x·f(x)dx          (continuous)
```

### Variance

```
Var(X) = E[(X - μ)²] = E[X²] - μ²
σ = √Var(X)              (standard deviation)
```

## Important Distributions

| Distribution | Parameters | Mean | Variance |
|--------------|------------|------|----------|
| Bernoulli | p | p | p(1-p) |
| Binomial | n, p | np | np(1-p) |
| Poisson | λ | λ | λ |
| Normal | μ, σ² | μ | σ² |
| Exponential | λ | 1/λ | 1/λ² |

### Key Formulas

```
Bayes' Theorem: P(A|B) = P(B|A)·P(A)/P(B)

Central Limit Theorem:
X̄ ~ N(μ, σ²/n) for large n

Chi-Square: χ² = Σ(O-E)²/E
t-statistic: t = (X̄ - μ)/(S/√n)
```

## Worked Examples

### Example 1: Probability Calculation

A bag contains 3 red and 2 blue balls. Find P(red, then blue) with replacement:

```
P(red) = 3/5
P(blue) = 2/5

P(red, then blue) = (3/5) × (2/5) = 6/25
```

### Example 2: Normal Distribution

X ~ N(100, 15²). Find P(X < 85):

```
Z = (85 - 100)/15 = -15/15 = -1

P(Z < -1) = 0.1587
```

### Example 3: Confidence Interval

Sample: n = 25, x̄ = 50, s = 5. Find 95% CI for μ:

```
SE = s/√n = 5/5 = 1
t₀.₀₂₅,₂₄ = 2.064

CI = 50 ± 2.064(1) = (47.94, 52.06)
```

## ASCII Illustrations

### Normal Distribution

```
                    f(x)
                     │
              ╭╮   │   ╭╮
             ╱ ╰╮  │  ╭╯ ╲
            │   ╰╮│ ╭╯   │
           ╱│    ╰╯╮     │╲
          ╱ │        ╲  │ ╲
         ╱  │         ╲ │  ╲
        ╱   │          ╲│   ╲
       ╱    │           ╰─╮   ╲
      ╱     │               ╲  ╲
     ╱      │                ╲  ╲
────╯───────┼─────────────────╯───╲────► x
         μ-3σ    μ   μ+3σ

     68.3%    95.4%   99.7%
```

### Sampling Distribution

```
    Population           Sampling
    ─────────           ─────────
    
    [••••••••]         [•••] x̄₁
    [••••••••]         [•••] x̄₂
    [••••••••]         [•••] x̄₃
    [••••••••]    →    [•••] x̄₄
         μ               x̄ ~ N(μ, σ²/n)
```

## AI/ML Applications

- **A/B Testing**: Statistical hypothesis testing
- **Model Evaluation**: Cross-validation, confidence intervals
- **Bayesian Inference**: Probabilistic models
- **Maximum Likelihood Estimation**: Parameter estimation
- **Naive Bayes Classifier**: Conditional probability

---

# 9. Discrete Mathematics

## Learning Objectives

- Master combinatorics and counting principles
- Understand recurrence relations
- Apply discrete structures to algorithms
- Connect combinatorics to algorithm analysis

## Key Concepts and Definitions

### Counting Principles

```
Product Rule: |A × B| = |A| × |B|
Sum Rule: |A ∪ B| = |A| + |B| (disjoint)
```

### Permutations and Combinations

```
P(n,r) = n!/(n-r)!    (arrangements)
C(n,r) = n!/(r!(n-r)!)  (selections)
```

### Recurrence Relations

```
aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ...     (linear recurrence)
```

### Sets and Relations

```
A = {a₁, a₂, ..., aₙ}
R ⊆ A × A    (binary relation)
```

## Important Formulas and Theorems

### Binomial Coefficients

```
C(n,r) = C(n, n-r)
C(n,0) + C(n,1) + ... + C(n,n) = 2ⁿ
C(n,k) = C(n-1,k) + C(n-1,k-1)
```

### Inclusion-Exclusion

```
|A ∪ B| = |A| + |B| - |A ∩ B|
|A ∪ B ∪ C| = |A| + |B| + |C| 
              - |A∩B| - |A∩C| - |B∩C| 
              + |A∩B∩C|
```

### Pigeonhole Principle

If n items are placed in m containers and n > m, then some container has ≥ 2 items.

## Worked Examples

### Example 1: Counting Permutations

How many ways to arrange 5 books on a shelf?

```
P(5,5) = 5! = 120
```

### Example 2: Combinations

Choose 3 from 10. How many ways?

```
C(10,3) = 10!/(3!7!) = 120
```

### Example 3: Recurrence Relation

Solve aₙ = 2aₙ₋₁ with a₀ = 3:

```
a₁ = 2·3 = 6
a₂ = 2·6 = 12
aₙ = 3·2ⁿ
```

### Example 4: Inclusion-Exclusion

How many integers from 1-100 divisible by 2, 3, or 5?

```
Div by 2: 50
Div by 3: 33
Div by 5: 20
Div by 2&3: 16
Div by 2&5: 10
Div by 3&5: 6
Div by 2&3&5: 3

Total = 50+33+20-16-10-6+3 = 74
```

## ASCII Illustrations

### Permutation Tree

```
         Start
           │
     ┌─────┼─────┐
     │     │     │
    A     B     C        →  P(3,3) = 3! = 6
   / \   / \   / \
  A B C A B C A B C
```

### Binomial Triangle (Pascal)

```
         1          C(0,0)
        1 1        C(1,0), C(1,1)
       1 2 1       C(2,0), C(2,1), C(2,2)
      1 3 3 1      C(3,0), C(3,1), C(3,2), C(3,3)
     1 4 6 4 1     ...
```

## AI/ML Applications

- **Algorithm Complexity**: Big-O notation for counting operations
- **Combinatorial Optimization**: NP-hard problems
- **Counting Arguments**: Proofs in machine learning theory
- **Recurrent Neural Networks**: Discrete time steps

---

# 10. Real Analysis

## Learning Objectives

- Master rigorous analysis of real numbers
- Understand limits, continuity, and differentiability
- Apply epsilon-delta definitions
- Connect real analysis to advanced mathematics

## Key Concepts and Definitions

### Completeness Axiom

Every non-empty set of real numbers bounded above has a least upper bound (supremum).

### Sequences

A sequence is a function a: ℕ → ℝ:

```
(aₙ) = a₁, a₂, a₃, ...
```

### Limits (Supremum/Infimum)

```
lim aₙ = L  ⇔  ∀ε>0, ∃N: |aₙ - L| < ε ∀n > N
```

### Continuity

f is continuous at a if:

```
∀ε>0, ∃δ>0: |x-a| < δ ⇒ |f(x)-f(a)| < ε
```

## Important Formulas and Theorems

### Bolzano-Weierstrass Theorem

Every bounded sequence has a convergent subsequence.

### Intermediate Value Theorem

If f is continuous on [a,b] and f(a) < 0 < f(b), then ∃c ∈ (a,b) with f(c) = 0.

### Mean Value Theorem

If f is continuous on [a,b] and differentiable on (a,b), then ∃c ∈ (a,b) such that:

```
f'(c) = (f(b) - f(a))/(b - a)
```

### Uniform Continuity

f is uniformly continuous if:

```
∀ε>0, ∃δ>0: |x-y| < δ ⇒ |f(x)-f(y)| < ε
```

## Worked Examples

### Example 1: Limit Using Definition

Prove lim(x→2) x² = 4:

```
|x² - 4| = |x-2||x+2|

For |x-2| < 1: |x+2| < 5
|x² - 4| < 5|x-2|

Given ε, choose δ = min(1, ε/5)
```

### Example 2: Proving Continuity

Prove f(x) = x² is continuous at x = 3:

```
|x² - 9| = |x-3||x+3|

For |x-3| < 1: |x+3| < 7
|x² - 9| < 7|x-3|

Given ε, choose δ = min(1, ε/7)
```

### Example 3: Monotone Convergence

Show aₙ = 1 - 1/n converges:

```
aₙ₊₁ - aₙ = (1 - 1/(n+1)) - (1 - 1/n) = 1/n - 1/(n+1) > 0
Monotone increasing, bounded by 1
Limit = 1
```

## ASCII Illustrations

### Epsilon-Delta Continuity

```
        f(x)
         │
       f(a)+ε ────────╲
                     ╲ ╲
                     ╲ ╲
                     ╲ ╲
     f(a) ────────────╲───
                     ╲ ╲
                     ╲ ╲
                     ╲ ╲
       f(a)-ε ────────  ╲──
                     ╲
                     ╲
                     ╲
           a-δ    a    a+δ  → x
```

### Convergence of Sequence

```
aₙ
 │
 │      • • • •
 │     ╱         •
 │    ╱          •
 │   ╱           •
 │  ╱            •
 │ ╱             •
 │╱              •
L ───────────────────────────
 │              •
 │            •
 │          •
 │        •
 ├──────────────────────────► n
```

## AI/ML Applications

- **Function Approximation**: Uniform convergence in learning theory
- **Optimization Theory**: Analysis of loss landscapes
- **Neural Network Theory**: Universal approximation theorems
- **Gradient Flow**: Continuous limits of discrete processes

---

# 11. Abstract Algebra

## Learning Objectives

- Master algebraic structures (groups, rings, fields)
- Understand homomorphisms and isomorphisms
- Apply group theory to symmetry problems
- Connect abstract algebra to coding theory

## Key Concepts and Definitions

### Groups

A group (G, *) is a set with operation satisfying:
- **Closure**: a*b ∈ G ∀a,b ∈ G
- **Associativity**: (a*b)*c = a*(b*c)
- **Identity**: ∃e ∈ G with e*a = a*e = a
- **Inverse**: ∀a ∈ G, ∃a⁻¹ with a*a⁻¹ = e

### Rings

A ring (R, +, ×) has:
- (R, +) is an abelian group
- Multiplication is associative
- Distributivity: a(b+c) = ab + ac

### Fields

A field is a ring where:
- Non-zero elements form a group under multiplication

## Important Formulas and Theorems

### Lagrange's Theorem

For finite group G:

```
|G| = |H| × [G:H]

where H is a subgroup
```

### Cayley's Theorem

Every group of order n is isomorphic to a subgroup of Sₙ (permutations).

### Isomorphism Theorems

```
G/ker(φ) ≅ im(φ)     (First isomorphism)
H/(H∩K) ≅ HK/K     (Second isomorphism)
```

### Fundamental Theorem of Finite Abelian Groups

Every finite abelian group is a direct product of cyclic groups of prime power order.

## Worked Examples

### Example 1: Verifying Group

Show (ℤ, +) is a group:

```
Closure: m + n ∈ ℤ
Associative: (m+n)+p = m+(n+p)
Identity: 0, m+0 = m
Inverse: -m, m+(-m) = 0
```

### Example 2: Cyclic Group

Find generators of ℤ₈:

```
Additive: 1, 3, 5, 7 generate
Multiplicative: 3, 5 generate
```

### Example 3: Quotient Group

Compute ℤ₆/⟨3⟩:

```
⟨3⟩ = {0, 3}
Cosets: {0,3}, {1,4}, {2,5}

ℤ₆/⟨3⟩ ≅ ℤ₃
```

## ASCII Illustrations

### Group Operation Table

```
        *  │   e   a   b   c
       ───┼──────────────
         e │   e   a   b   c
         a │   a   b   c   e
         b │   b   c   e   a
         c │   c   e   a   b
         
    (Klein 4-group)
```

### Subgroup Lattice

```
          e
          │
          │
         ⋊⋉
        ╱ ╲
       H₁  H₂
        ╲ ╱
         ⋌⋏
          │
          G
```

## AI/ML Applications

- **Cryptography**: Group theory in public-key cryptosystems
- **Error-Correcting Codes**: Ring theory in coding theory
- **Symmetry Groups**: CNN architectures with symmetry
- **Neural Network Weights**: Vector spaces over fields

---

# 12. Topology

## Learning Objectives

- Understand topological spaces and continuous maps
- Master connectedness and compactness
- Apply separation axioms
- Connect topology to analysis and geometry

## Key Concepts and Definitions

### Topological Space

A topological space (X, τ) where τ is a collection of open sets satisfying:
- ∅, X ∈ τ
- Arbitrary union of open sets ∈ τ
- Finite intersection of open sets ∈ τ

### Continuous Maps

f: X → Y is continuous if:

```
f⁻¹(U) is open in X for every open U in Y
```

### Homeomorphism

f is a homeomorphism if:
- f is bijective
- f is continuous
- f⁻¹ is continuous

### Basis

A basis B generates topology τ if:
- For each x ∈ X, ∃B ∈ B with x ∈ B
- If x ∈ B₁ ∩ B₂, ∃B₃ with x ∈ B₃ ⊆ B₁ ∩ B₂

## Important Formulas and Theorems

### Urysohn Lemma

X is normal iff there exists continuous f: X → [0,1] separating closed sets.

### Tychonoff Theorem

Product of compact spaces is compact.

### Brouwer Fixed Point Theorem

Every continuous f: Bⁿ → Bⁿ has a fixed point.

### Jordan Curve Theorem

Simple closed curve in ℝ² separates ℝ² into two connected components.

## Worked Examples

### Example 1: Standard Topology

The standard topology on ℝ has basis:

```
B = {(a,b) | a < b}
```

### Example 2: Connectedness

Show ℝ is connected:

```
Assume ℝ = U ∪ V, disjoint nonempty open
Let U be nonempty proper set
Since ℝ is connected, such decomposition impossible
```

### Example 3: Compactness

Show [0,1] is compact:

```
Every open cover has finite subcover
(Heine-Borel: closed bounded sets in ℝ)
```

## ASCII Illustrations

### Topological Mappings

```
    Continuous but not Homeomorphic:
    
    Circle (S¹)    ≠    Figure-8
    
    ●                  ●
   ╱ ╲                ╱╲
  ●   ●              ●  ●
   ╲ ╱               ╲╱
    ●                 ●
```

### Separation Axioms

```
    T₀: Distinct points separable
    T₁: Points separable by neighborhoods  
    T₂ (Hausdorff): Points separable by disjoint neighborhoods
    
         T₀  →  T₁  →  T₂
         
         Less restrictive → More restrictive
```

## AI/ML Applications

- **Manifold Learning**: Topological data analysis
- **Persistent Homology**: Feature extraction from data
- **Neural Network Topology**: Understanding loss landscapes
- **Topological Data Analysis (TDA)**: Shape classification

---

# 13. Complex Analysis

## Learning Objectives

- Master complex numbers and analytic functions
- Understand contour integration
- Apply Cauchy theorems
- Connect complex analysis to physics

## Key Concepts and Definitions

### Complex Numbers

```
z = x + iy
     │
     │   y (imaginary)
     │   │
     │   ├──── x (real)
     │   │
     ▼   ▼
     
|z| = √(x² + y²)    (modulus)
arg(z) = atan2(y, x)  (argument)
z = r(cosθ + isinθ) = re^(iθ)
```

### Analytic Functions

f is analytic at z₀ if it has a complex derivative:

```
f'(z) = lim(h→0) [f(z+h) - f(z)]/h
```

### Cauchy-Riemann Equations

If f(z) = u(x,y) + iv(x,y), then:

```
∂u/∂x = ∂v/∂y
∂u/∂y = -∂v/∂x
```

## Important Formulas and Theorems

### Cauchy's Integral Theorem

If f is analytic in simply connected domain D:

```
∮C f(z)dz = 0
```

### Cauchy's Integral Formula

If f is analytic inside and on C:

```
f(z₀) = (1/2πi)∮C f(z)/(z-z₀) dz
```

### Residue Theorem

```
∮C f(z)dz = 2πi Σ Res(f, ak)
```

### Laurent Series

```
f(z) = Σₙ₌₋∞^∞ aₙ(z-z₀)ⁿ
```

## Worked Examples

### Example 1: Complex Derivative

Find derivative of f(z) = z²:

```
f(z+h) - f(z) = (z+h)² - z² = 2zh + h²
[f(z+h) - f(z)]/h = 2z + h
lim(h→0) = 2z
```

### Example 2: Using Cauchy's Formula

Evaluate ∮C z/(z-1) dz where C is |z| = 2:

```
f(z) = z is analytic
f(1) = 1

∮ = 2πi × 1 = 2πi
```

### Example 3: Finding Residue

Res of f(z) = 1/(z-2) at z = 2:

```
Res = lim(z→2) (z-2)(1/(z-2)) = 1
```

## ASCII Illustrations

### Complex Plane Mapping

```
        w-plane              z-plane
         
         Im(w)                Im(z)
           │                   │
      ────┼────────          ────┼────────
           │                   │
      ────┼────────      ⇔     ────┼────────
           │                   │
           └─────────► Re(w)   └─────────► Re(z)
```

### Contour Integration Path

```
    C₁ ──────────────────► C₂
     ╲                    ╱
      ╲                  ╱
       ╲                ╱
        ╲              ╱
         ╲            ╱
          ╲          ╱
           ╲        ╱
            ╲      ╱
             ╲    ╱
              ╲  ╱
               ╲╱
                C₃
```

## AI/ML Applications

- **Signal Processing**: Fourier transforms in complex plane
- **Control Theory**: Transfer functions
- **Fluid Dynamics**: Complex potential
- **Quantum Mechanics**: Complex wave functions

---

# 14. Number Theory

## Learning Objectives

- Master divisibility and prime distribution
- Understand modular arithmetic and congruences
- Apply number theory to cryptography
- Connect number theory to computational complexity

## Key Concepts and Definitions

### Divisibility

a divides b (a | b) if ∃k ∈ ℤ: b = ak

### Prime Numbers

A prime p has exactly two divisors: 1 and p.

### Congruences

a ≡ b (mod n) if n | (a - b)

### Greatest Common Divisor

```
gcd(a,b) = max{d | d|a and d|b}
```

### Euler's Totient Function

φ(n) = count of 1 ≤ k ≤ n with gcd(k,n) = 1

## Important Formulas and Theorems

### Euclidean Algorithm

```
gcd(a,b) = gcd(b, a mod b)
```

### Fundamental Theorem of Arithmetic

Every n > 1 has unique prime factorization.

### Fermat's Little Theorem

If p is prime and p ∤ a:

```
a^(p-1) ≡ 1 (mod p)
```

### Euler's Theorem

If gcd(a,n) = 1:

```
a^(φ(n)) ≡ 1 (mod n)
```

### Chinese Remainder Theorem

If m,n coprime:

```
x ≡ a (mod m)
x ≡ b (mod mn)

has unique solution modulo mn
```

## Worked Examples

### Example 1: Using Euclidean Algorithm

gcd(48, 18):

```
48 = 18 × 2 + 12
18 = 12 × 1 + 6
12 = 6 × 2 + 0

gcd = 6
```

### Example 2: Chinese Remainder

Solve x ≡ 2 (mod 3), x ≡ 3 (mod 4):

```
3×4 = 12
x = 2 + 3k
3k ≡ 1 (mod 4)
k ≡ 3 (mod 4)

x = 2 + 3(3) = 11 ≡ 11 (mod 12)
```

### Example 3: Euler's Totient

Find φ(12):

```
12 = 2² × 3
φ(12) = 12(1-1/2)(1-1/3) = 12(1/2)(2/3) = 4
```

## ASCII Illustrations

### Prime Distribution (Ulam Spiral)

```
    17  24   1   8  15
    23  25   7  14  16
     5   6  13  19  26
    10  12  18  20  21
    11  22  27  33  34
    
    ●●●●●  Primes form diagonal patterns
```

### Modular Arithmetic on Clock

```
    12  1  2
   ╱    ╲
  11     3
  ╱       ╲
 10  ←──  4
  ╲      ╱
   9  5
    ╲╱
     6
     │
     ▼
   Direction represents +1 mod 12
```

## AI/ML Applications

- **Cryptography**: RSA, elliptic curve crypto
- **Hash Functions**: Cryptographic hashes
- **Random Number Generation**: PRNGs
- **Error-Correcting Codes**: Reed-Solomon codes

---

# 15. Mathematical Logic

## Learning Objectives

- Master propositional and predicate logic
- Understand proof techniques
- Apply logical systems to mathematics
- Connect logic to computational complexity

## Key Concepts and Definitions

### Propositional Logic

```
Atomic propositions: p, q, r
Logical connectives: ∧ (and), ∨ (or), ¬ (not), → (implies), ↔ (iff)
```

### Truth Tables

```
p  q │ p∧q p∨q p→q p↔q
───┼────────────────────
T  T │  T    T   T    T
T  F │  F    T   F    F
F  T │  F    T   T    F
F  F │  F    F   T    T
```

### Predicates

```
P(x): "x is a prime"
∀x P(x)    (for all x)
∃x P(x)   (there exists x)
```

### Quantifiers

```
¬∀x P(x) ≡ ∃x ¬P(x)
¬∃x P(x) ≡ ∀x ¬P(x)
```

## Important Formulas and Theorems

### Modus Ponens

```
P → Q
P
────
Q
```

### Modus Tollens

```
P → Q
¬Q
────
¬P
```

### Deduction Theorem

```
Γ ⊢ P → Q   iff   Γ ∪ {P} ⊢ Q
```

### Compactness Theorem

A set of sentences is satisfiable iff every finite subset is satisfiable.

### Gödel's Completeness Theorem

First-order logic is complete: whatever is logically valid is provable.

### Gödel's Incompleteness Theorem

Any sufficiently powerful consistent system is incomplete.

## Worked Examples

### Example 1: Truth Table Construction

Determine if (p ∧ q) → p is a tautology:

```
p q │ (p∧q) → p
T T │      T
T F │      T
F T │      T
F F │      T

All true → TAUTOLOGY
```

### Example 2: Logical Proof

Prove: P ∧ (P ∨ Q) → P

```
1. P                    (Premise)
2. P ∨ Q               (From 1, Addition)
3. P ∧ (P ∨ Q)         (From 1, 2, Conjunction)
4. P                    (From 3, Simplification)
```

### Example 3: Quantifier Transformation

Negate: ∀x (P(x) → Q(x))

```
¬∀x (P(x) → Q(x))
≡ ∃x ¬(¬P(x) ∨ Q(x))
≡ ∃x (P(x) ∧ ¬Q(x))
```

## ASCII Illustrations

### Proof Tree

```
        Gentzen Natural Deduction
        
              P → Q    P
                   ╱╲
                  ╱  ��
                 ╱    ╲
                ╱     ╲
               Q      Q
        
        By Modus Ponens
```

### Venn Diagram for Logic

```
        P ∧ Q          P ∨ Q
        
        ╱──╲          ╱──╲
       │ ██ │        │███│
       ╲╱──╲╲        ╲╱██╲╲
        │  │          ██│
        └──┘          ──┘
```

## AI/ML Applications

- **Automated Reasoning**: Theorem provers
- **Logic Programming**: Prolog, Datalog
- **Knowledge Representation**: Semantic networks
- **Verification**: Model checking

---

# 16. Information Theory

## Learning Objectives

- Master entropy and information measures
- Understand coding theory
- Apply data compression techniques
- Connect information theory to machine learning

## Key Concepts and Definitions

### Entropy

For discrete random variable X:

```
H(X) = -Σ p(x) log₂ p(x)
     = Σ p(x) log₂(1/p(x))
```

### Joint Entropy

```
H(X,Y) = -Σ p(x,y) log₂ p(x,y)
```

### Conditional Entropy

```
H(Y|X) = Σ p(x) H(Y|X=x)
```

### Mutual Information

```
I(X;Y) = H(X) - H(X|Y)
       = H(Y) - H(Y|X)
```

## Important Formulas and Theorems

### Chain Rule

```
H(X,Y) = H(X) + H(Y|X)
```

### Data Processing Inequality

If Z is a function of Y:

```
I(X;Z) ≤ I(X;Y)
```

### Shannon's Noiseless Coding Theorem

```
H(X) ≤ average codeword length < H(X) + 1
```

### Shannon's Channel Coding Theorem

```
C = maxₚ I(X;Y)   (channel capacity)
```

### Kullback-Leibler Divergence

```
D(P||Q) = Σ p(x) log(p(x)/q(x))
```

## Worked Examples

### Example 1: Entropy Calculation

X takes values {0,1} with P(0)=1/4, P(1)=3/4:

```
H(X) = -(1/4)log₂(1/4) - (3/4)log₂(3/4)
     = 0.5 + 0.811 ≈ 1.811 bits
```

### Example 2: Binary Channel Capacity

Binary symmetric channel with p=0.1:

```
C = 1 + p log₂p + (1-p)log₂(1-p)
  = 1 + 0.1(-3.32) + 0.9(0.152)
  = 1 - 0.332 + 0.137 = 0.805 bits
```

### Example 3: Mutual Information

X,Y joint distribution:
```
     Y=0   Y=1
X=0  0.3   0.1
X=1  0.2   0.4

H(X) = -0.4log₂0.4 - 0.6log₂0.6 = 0.97
H(Y) = -0.5log₂0.5 - 0.5log₂0.5 = 1.0
H(X,Y) = -0.3log₂0.3-0.1log₂0.1-0.2log₂0.2-0.4log₂0.4 = 1.85

I = H(X) + H(Y) - H(X,Y) = 0.97 + 1 - 1.85 = 0.12
```

## ASCII Illustrations

### Entropy as Uncertainty

```
    Low Entropy          High Entropy
    
    ███                 ████████████████████
    ██                  ██████████
    ███                 ██████
    
    Deterministic        Random
```

### Noisy Channel

```
    Source → Encoder → Channel → Decoder → Destination
    
         noise
           ╲
            ╲  Bit Flip
             ╲ (p)
              ╲
               ╲
                ╲
                 ▼
               Bit received with error probability p
```

## AI/ML Applications

- **Decision Trees**: Information gain for splitting
- **Maximum Likelihood**: Entropy-based inference
- **Compression**: Huffman coding, gzip
- **Variational Autoencoders**: KL divergence in latent space

---

# 17. Numerical Analysis

## Learning Objectives

- Master numerical approximation methods
- Understand error analysis
- Apply iterative methods for solving equations
- Connect numerical methods to scientific computing

## Key Concepts and Definitions

### Floating Point Numbers

```
x = ±d₀.d₁d₂...dₚ × βᵉ

where:
- β = base (typically 2)
- p = precision (number of digits)
- e = exponent
```

### Error Types

```
Absolute Error: |x - x̄|
Relative Error: |x - x̄|/|x|

Truncation Error: Approximating infinite by finite
Roundoff Error: Representing exact by floating point
```

### Convergence

An iterative method converges with order r if:

```
|xₙ₊₁ - x| ≤ C|xₙ - x|^r
```

## Important Formulas and Theorems

### Bisection Method

```
Given f(a)f(b) < 0, iterate:
c = (a+b)/2
If f(c) = 0, stop
If f(a)f(c) < 0, b = c
Else a = c

Error ≤ (b-a)/2ⁿ
```

### Newton's Method

```
xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)

Quadratic convergence (under ideal conditions)
```

### Gaussian Elimination

```
Forward elimination → Back substitution
复杂度 O(n³)
```

### Numerical Integration

```
Trapezoidal: ∫f ≈ (h/2)[f₀ + 2f₁ + ... + fₙ]
Simpson's: ∫f ≈ (h/3)[f₀ + 4f₁ + 2f₂ + ... + 4fₙ₋₁ + fₙ]
```

## Worked Examples

### Example 1: Bisection

Find root of f(x) = x² - 2 between 1 and 2:

```
n=0: a=1, b=2, c=1.5, f(c)=0.25>0 → b=1.5
n=1: a=1, b=1.5, c=1.25, f(c)=-0.375 → a=1.25  
n=2: a=1.25,b=1.5, c=1.375, f(c)=-0.109 → a=1.375
n=3: a=1.375,b=1.5, c=1.4375 → √2 ≈ 1.414
```

### Example 2: Newton's Method

Find √2 using f(x) = x² - 2:

```
xₙ₊₁ = xₙ - (xₙ²-2)/(2xₙ) = (xₙ + 2/xₙ)/2

x₀ = 1.5
x₁ = (1.5 + 2/1.5)/2 = 1.4167
x₂ = (1.4167 + 2/1.4167)/2 = 1.4142
```

### Example 3: Lagrange Interpolation

Find quadratic through (1,1), (2,4), (3,9):

```
P(x) = 1·(x-2)(x-3)/((1-2)(1-3)) 
     + 4·(x-1)(x-3)/((2-1)(2-3))
     + 9·(x-1)(x-2)/((3-1)(3-2))
     = x²
```

## ASCII Illustrations

### Newton's Method Convergence

```
    f(x)                    Convergence
       │                       xₙ
       │╲                        │
       │ ╲                       •──► solution
       │  ╲                   •
       │   ╲                 •
       │    ╲               •
       │     ╲            •
       │      ╲         •
       │       ╲      •
       │        ╲   •
       └────────────────► x
         tangent at xₙ
```

### Error in Numerical Integration

```
    Trapezoidal              Simpson's
    
    ╱╲                    ╱──╲
   ╱  ╲    ←── area      ╱     ╲ ←── parabolic
  ╱    ╲                ╱       ╲    approximation
 ╱──────╲              ╱─────────╲   (more accurate)
│        │            │           │
└────────┘            └──────────┘
```

## AI/ML Applications

- **Deep Learning**: GPU-accelerated numerical computation
- **Optimization**: Gradient descent implementations
- **Matrix Operations**: BLAS/LAPACK in neural networks
- **Automatic Differentiation**: Forward/reverse mode

---

# 18. Optimization

## Learning Objectives

- Master optimization theory and methods
- Understand convex and non-convex optimization
- Apply gradient descent and related methods
- Connect optimization to machine learning

## Key Concepts and Definitions

### Optimization Problem

```
minimize f(x)
subject to x ∈ X

where:
- f: ℝⁿ → ℝ (objective)
- X ⊆ ℝⁿ (feasible set)
```

### Convex Sets and Functions

```
Convex set: λx + (1-λ)y ∈ X ∀x,y ∈ X, λ ∈ [0,1]
Convex function: f(λx + (1-λ)y) ≤ λf(x) + (1-λ)f(y)
```

### Lagrange Multipliers

```
min f(x)
subject to g(x) = 0

L(x,λ) = f(x) + λᵀg(x)
∇L = 0 for optimality
```

###KKT Conditions

```
∇f(x*) + ∇g(x*)λ* + ∇h(x*)μ* = 0
g(x*) = 0
h(x*) ≤ 0
λ* ≥ 0
λ*h(x*) = 0
```

## Important Formulas and Theorems

### Gradient Descent

```
xₖ₊₁ = xₖ - α∇f(xₖ)

where α is step size
```

### Newton's Method (Optimization)

```
xₖ₊₁ = xₖ - H⁻¹∇f(xₖ)

where H is Hessian
```

### Conjugate Gradient

```
r = -∇f(xₖ)
β = rₖᵀrₖ/rₖ₋₁ᵀrₖ₋₁
dₖ = rₖ + βdₖ₋₁
xₖ₊₁ = xₖ + αdₖ
```

### Interior Point Method

```
minimize f(x) - tΣ log(-hᵢ(x))
```

## Worked Examples

### Example 1: Finding Minimum

Find minimum of f(x) = x² - 4x + 3:

```
∇f(x) = 2x - 4 = 0
x = 2

Minimum: f(2) = 4 - 8 + 3 = -1
```

### Example 2: Constrained Optimization

Minimize x² + y² subject to x + y = 1:

```
L = x² + y² + λ(x + y - 1)
∂L/∂x = 2x + λ = 0
∂L/∂y = 2y + λ = 0
∂L/∂λ = x + y - 1 = 0

Solving: x = y = 1/2
Minimum: f(1/2,1/2) = 1/4 + 1/4 = 1/2
```

### Example 3: Gradient Descent

Minimize f(x,y) = x² + y² starting from (1,1):

```
∇f = (2x, 2y)
xₖ₊₁ = xₖ - 0.1(2xₖ, 2yₖ)

Step 1: (1,1) - 0.1(2,2) = (0.8, 0.8)
Step 2: (0.8,0.8) - 0.1(1.6,1.6) = (0.64, 0.64)
Converges to (0,0)
```

## ASCII Illustrations

### Optimization Landscape

```
    Convex                      Non-Convex
    
    ╱                         ╱╲
   ╱                         ╱  ╲
  ╱                         ╱    ╲
 ╱                         ╱      ╲
╱                         ╱        ╲    ──┬──
                                ░      ╲  │
                               ░         ╲│
                              ░              ─┼──
                             ░                
                             ───────────────────
```

### Gradient Descent Path

```
    Contour Plot
    
    ╭───────╮
    │ ╲     │
    │  ╲    │
    │   ╲   │──→ optimal
    │    ╲  │        x* 
    │     ╲ │
    │      ╲│
    │  \    │
    │   \   │
    │    \  │
    │     \ │
    └───────╯
        ╱ path
       ╱
```

## AI/ML Applications

- **Training Neural Networks**: Loss minimization
- **Support Vector Machines**: Margin maximization
- **Linear Regression**: Least squares
- **Reinforcement Learning**: Policy optimization

---

# 19. Graph Theory

## Learning Objectives

- Master graph structures and representation
- Understand paths, cycles, and connectivity
- Apply graph algorithms
- Connect graph theory to networks

## Key Concepts and Definitions

### Graph Definition

```
G = (V, E)

where:
- V = {v₁, v₂, ..., vₙ} (vertices)
- E = {e₁, e₂, ..., eₘ} ⊆ V×V (edges)
```

### Types of Graphs

```
Undirected: Edges have no direction
Directed (Digraph): Edges have direction
Weighted: Edges have weights
Simple: No loops or multiple edges
```

### Key Vertices

```
Degree: d(v) = number of edges incident to v
Indegree: d⁻(v) = edges pointing to v
Outdegree: d⁺(v) = edges pointing from v
```

## Important Formulas and Theorems

### Handshaking Lemma

```
Σᵥ d(v) = 2|E|
```

### Eulerian Trails

- Eulerian circuit exists iff all vertices have even degree
- Eulerian path exists iff exactly 0 or 2 vertices have odd degree

###Hamiltonian Path

NP-complete to determine existence.

### Graph Isomorphism

```
G₁ ≅ G₂ if ∃ bijection f: V₁ → V₂ preserving edges
```

### Planar Graphs (Euler's Formula)

```
For connected planar graph:
|V| - |E| + |F| = 2
```

### Shortest Path (Dijkstra)

```
dist[v] = min(dist[u] + w(u,v))
```

## Worked Examples

### Example 1: Finding Degree Sequence

Graph with edges {(1,2), (1,3), (2,3), (3,4)}:

```
d(1) = 2
d(2) = 2  
d(3) = 3
d(4) = 1
```

### Example 2: BFS Shortest Path

Find shortest path from A to D:

```
A ─ B ─ D
│   │
C ── E

Path: A → B → D (length 2)
```

### Example 3: Eulerian Path Check

Is there Eulerian path in graph with degrees {2,2,2,1,1}?

```
Two odd-degree vertices: YES
```

## ASCII Illustrations

### Graph Representations

```
    Adjacency Matrix      Adjacency List
    
    A B C              A: B, C
    A 0 1 1     →     B: A, C
    B 1 0 1            C: A, B
    C 1 1 0
    
    Memory: O(V²)        Memory: O(V+E)
```

### Network Topology

```
     Star          Tree           Ring
        
        ◯            ◯            ◯
       /│\          /│\           ╱ ╲
      ◯ ◯ ◯        ◯ ◯ ◯         ◯   ◯
      /  │          │  ╲         ╱╲ ╱╲
     ◯   ◯         ◯  ◯              ◯
```

## AI/ML Applications

- **Neural Networks**: Computational graphs
- **Knowledge Graphs**: Relational representations
- **Social Networks**: Graph embeddings
- **Graph Neural Networks**: Message passing on graphs

---

# 20. Mathematical Foundations for AI/ML

## Learning Objectives

- Master mathematical foundations of AI/ML
- Understand linear algebra in neural networks
- Apply calculus to optimization
- Connect probability and statistics to machine learning

## Key Concepts and Definitions

### Neural Network Architecture

```
Input Layer    Hidden Layers    Output Layer
    
   x₁
   x₂   ──►   h₁ ──►   y₁
   x₃        h₂        y₂
   ...       ...      ...
              hₖ
```

### Forward Pass

```
z₁ = W₁x + b₁
a₁ = σ(z₁)
z₂ = W₂a₁ + b₂
ŷ = softmax(z₂)  (for classification)
```

### Loss Functions

```
MSE: L = (1/n)Σ(yᵢ - ŷᵢ)²
Cross-Entropy: L = -Σyᵢlog(ŷᵢ)
```

## Mathematics in AI/ML

### 1. Linear Algebra in Neural Networks

```
Layer Computation:

┌                          ┐
│  Input  →  Weight Matrix  →  Output  │
│  (n×1)      (m×n)           (m×1) │
└                          ┘

Matrix multiplication corresponds to:
- Linear transformation of feature vectors
- Combining features across layers
```

### 2. Calculus in Backpropagation

```
Gradient Computation Chain Rule:

        ∂L/∂zᵢ = ∂L/∂aᵢ × σ'(zᵢ)
        
        ∂L/∂Wᵢ = ∂L/∂zᵢ × aᵢ₋₁ᵀ
        
        ∂L/∂bᵢ = ∂L/∂zᵢ
        ├── Each layer passes gradients
        └── Using chain rule for composition
```

### 3. Statistics in Model Evaluation

```
Confusion Matrix:

              Predicted
              Pos    Neg
    Actual 
    Pos      TP    FN
    Neg      FP    TN

Metrics:
- Accuracy = (TP+TN)/(P+N)
- Precision = TP/(TP+FP)
- Recall = TP/(TP+FN)
- F1 = 2×P×R/(P+R)
```

### 4. Probability in Generative Models

```
Maximum Likelihood Estimation:

L(θ) = Πᵢ p(xᵢ|θ)
log L(θ) = Σᵢ log p(xᵢ|θ)

θ* = argmax log L(θ)

Corresponds to minimizing KL divergence
```

### 5. Optimization in Training

```
Gradient Descent Update:

wₜ₊₁ = wₜ - η∇L(wₜ)

        │
        ▼ Gradient points uphill
        │
    ┌───╲
   ╱    ╲← Decreasing loss
  ╱      ╲
 ╱        ╲
╱          ╲
▼            ▼
 Loss       Minima found
 Landscape
```

## Important Formulas

### Backpropagation Equations

```
1. δᴸ = ∇ₐ C ⊙ σ'(zᴸ)
2. δˡ = ((Wˡ⁺¹)ᵀδˡ⁺¹) ⊙ σ'(zˡ)
3. ∂C/∂bˡ = δˡ
4. ∂C/∂Wˡ = δˡ(aˡ⁻¹)ᵀ
```

### Matrix Derivatives

```
∂/∂W Tr(AXB) = AᵀBᵀ
∂/∂X Tr(AXB) = AᵀBᵀ + AXB - AXBᵀ
```

### Activation Function Derivatives

```
Sigmoid: σ'(x) = σ(x)(1-σ(x))
ReLU: σ'(x) = 1 if x>0, else 0
Tanh: σ'(x) = 1 - tanh²(x)
```

## Worked Examples

### Example 1: Single Layer Forward Pass

Given x = [1,2]ᵀ, W = [[1,0],[0,1]], b = [0,0]ᵀ, σ = ReLU:

```
z = Wx + b = [1,2]ᵀ
a = σ(z) = [max(0,1), max(0,2)] = [1,2]ᵀ
```

### Example 2: Gradient Computation

L = (y - ŷ)², ŷ = σ(wx + b), σ(x) = sigmoid:

```
∂L/∂ŷ = -2(y - ŷ)
∂ŷ/∂z = σ(z)(1-σ(z))
∂z/∂w = x
∂z/∂b = 1

∂L/∂w = -2(y-ŷ) × σ(z)(1-σ(z)) × x
```

### Example 3: Computing Attention

Attention scores in transformers:

```
Q = [n×d] query matrix
K = [n×d] key matrix  
V = [n×d] value matrix

Attention(Q,K,V) = softmax(QKᵀ/√d)V

- Matrix multiply QKᵀ combines queries and keys
- Scale by √d for stability
- Softmax normalizes across positions
- Multiply by V gives weighted values
```

## AI/ML Mathematics Visualizations

### Neural Network Architecture

```
    Input     Hidden 1    Hidden 2    Output
    Layer       Layer       Layer       Layer
    
    x₁ ────► h₁¹ ───► h₂¹ ───► y₁
             │        │        │
    x₂ ───► h₁² ───► h₂² ───► y₂
             │        │        │
    x₃ ───► h₁³ ───► h₂³ ───► y₃
    
    Weights: W¹ (3×3), W² (3×3), W³ (3×3)
```

### Gradient Descent in Loss Landscape

```
    Loss Surface (2D slice)
    
         ▲
         │
    high │      ╱╲
         │     ╱  ╲
         │    ╱    ╲         ╱╲
         │   ╱      ╲       ╱  ╲
         │  ╱        ╲     ╱    ╲
         │ ╱          ╲  ╱      ╲       • minimum
         │╱            ╲╱        ╲    ◯
         ├───────────────────────────► 
          low                   w
          
          Gradient descent follows negative gradient
```

### Backpropagation Flow

```
    Forward Pass          Backward Pass
    
    x ──► W₁ ──► a₁ ──► W₂ ──► a₂ ──► Loss
    
                    Loss ◄── δ₂ ◄── δ₁ ◄── 
                          
    Information flows    Gradients flow backward
    forward             propagating error
```

### Transformer Self-Attention

```
    Multi-Head Attention
    
    Query Q ─┬─► Attention ──► Output
              │
    Key   K ─┤
              │
    Value V ──┘
    
    QKᵀ measures similarity
    Softmax normalizes
    V weights by similarity
```

### Convolutional Neural Network

```
    2D Convolution
    
    Input (5×5)       Filter (3×3)      Output (3×3)
    
    ┌─────┐          
    │ ███ │          ┌───┬───┬───┐
    │ ███ │  *       │ 1 │ 0 │-1 │
    │ ███ │          ├───┼───┼───┤
    │ ███ │          │ 2 │ 0 │-2 │
    │ ███ │          ├───┼───┼───┤
    └─────┘          │ 1 │ 0 │-1 │
                     └───┴───┴───┘
                     
    Sliding filter computes local features
```

## Mathematical Topics in AI

| Topic | AI/ML Application |
|-------|-------------------|
| Linear Algebra | Neural network layers, embeddings |
| Calculus | Gradient descent, backpropagation |
| Probability | Generative models, VAEs |
| Statistics | Model evaluation, hypothesis testing |
| Optimization | Loss minimization, parameter tuning |
| Information Theory | Entropy losses, mutual information |
| Graph Theory | GNNs, knowledge graphs |
| Numerical Analysis | GPU computation, automatic differentiation |

---

# Conclusion

This mathematics curriculum provides a comprehensive foundation spanning from basic arithmetic through advanced topics essential for understanding modern artificial intelligence and machine learning.

**Key Takeaways:**

1. **Linear Algebra** provides the language for representing neural networks, images, and data
2. **Calculus** enables optimization through gradient descent and backpropagation
3. **Probability and Statistics** form the basis for inference, uncertainty quantification, and model evaluation
4. **Optimization Theory** provides algorithms for training ML models
5. **Discrete Mathematics** underpins algorithm design and computational complexity

**AI/ML Mathematics Roadmap:**

```
    Foundation
         │
    ┌────┼────┐
    │    │    │
    ▼    ▼    ▼
 Algebra Calc Stats
    │    │    │
    ▼    ▼    ▼
 Neural Networks + Optimization
    ��
    ▼
 Deep Learning Applications
```

The mathematical concepts presented here are interconnected and build upon each other, providing the rigorous foundation necessary for advancing in artificial intelligence and machine learning research and applications.

---

*Document Version: 1.0*
*Created: Comprehensive Mathematics Reference*

*Related Notes:*
- [[05-AI-Research/AI Fundamentals]]
- [[03-Resources/Knowledge Management System]]
- [[07-Cybersecurity/Cryptography Math]]
- [[09-Knowledge/Mathematical Foundations of CS]]
