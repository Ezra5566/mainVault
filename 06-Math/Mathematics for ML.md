# Mathematics for Machine Learning

## Linear Algebra

### Vectors & Vector Spaces
- **Vectors** - Ordered lists of numbers representing magnitude and direction
- **Vector Operations** - Addition, subtraction, scalar multiplication, dot product
- **Norms** - L1 (Manhattan), L2 (Euclidean), L-infinity (max)
- **Orthogonality** - Perpendicular vectors (dot product = 0)
- **Linear Independence** - No vector can be written as combination of others
- **Basis** - Minimal set of linearly independent vectors spanning the space
- **Dimension** - Number of vectors in a basis

### Matrices & Matrix Operations
- **Matrix Multiplication** - ROW × COLUMN = element
- **Special Matrices**
  - Identity (I) - Doesn't change vector when multiplied
  - Diagonal - Non-zero only on main diagonal
  - Symmetric - A = A^T
  - Orthogonal - Q^T Q = I (preserves lengths and angles)
  - Positive Definite - x^T A x > 0 for all non-zero x
- **Matrix Properties**
  - Rank - Dimension of column/row space
  - Determinant - Volume scaling factor (det=0 means singular)
  - Trace - Sum of diagonal elements
  - Inverse - A^-1 exists iff det(A) ≠ 0

### Key Concepts for ML
- **Change of Basis** - Representing vectors in different coordinate systems
- **Eigenvalues & Eigenvectors** - Av = λv (v doesn't change direction under A)
  - Eigenvalues indicate scaling factor
  - Eigenvectors indicate principal directions
  - Applications: PCA, spectral clustering
- **Singular Value Decomposition (SVD)** - A = UΣV^T
  - Universal decomposition (works for any matrix)
  - Σ contains singular values (strength of components)
  - U and V contain left/right singular vectors
  - Applications: dimensionality reduction, recommendation systems
- **Matrix Factorizations**
  - LU Decomposition - For solving linear systems
  - QR Decomposition - For least squares problems
  - Cholesky Decomposition - For symmetric positive definite matrices

## Calculus

### Derivatives & Differentiation
- **Derivative** - Instantaneous rate of change: f'(x) = lim(h→0) [f(x+h)-f(x)]/h
- **Partial Derivatives** - Derivative with respect to one variable, others constant
- **Gradient** - Vector of partial derivatives (∇f), points in direction of steepest ascent
- **Jacobian Matrix** - Matrix of all first-order partial derivatives
- **Hessian Matrix** - Matrix of second-order partial derivatives
- **Chain Rule** - Essential for backpropagation in neural networks

### Important Derivative Rules
- Power rule: d/dx [x^n] = nx^(n-1)
- Product rule: d/dx [f(x)g(x)] = f'(x)g(x) + f(x)g'(x)
- Quotient rule: d/dx [f(x)/g(x)] = [f'(x)g(x)-f(x)g'(x)]/[g(x)]^2
- Chain rule: d/dx [f(g(x))] = f'(g(x))g'(x)

### Optimization Concepts
- **Critical Points** - Where gradient = 0 (potential minima, maxima, saddle points)
- **Second Derivative Test** - Use Hessian to classify critical points
- **Convex Functions** - f(θx+(1-θ)y) ≤ θf(x)+(1-θ)f(y) for θ∈[0,1]
  - Any local minimum is global minimum
  - Hessian is positive semi-definite everywhere
- **Gradient Descent** - Iterative optimization: θ_{t+1} = θ_t - α∇f(θ_t)
  - Learning rate (α) controls step size
  - Variants: Batch, Stochastic, Mini-batch, Momentum, Adam

## Probability & Statistics

### Probability Fundamentals
- **Sample Space** - Set of all possible outcomes (Ω)
- **Events** - Subsets of sample space
- **Probability Axioms**
  - 0 ≤ P(A) ≤ 1
  - P(Ω) = 1
  - For disjoint events: P(A∪B) = P(A) + P(B)
- **Conditional Probability** - P(A|B) = P(A∩B)/P(B) (if P(B)>0)
- **Bayes' Theorem** - P(A|B) = [P(B|A)P(A)]/P(B)
- **Independence** - P(A∩B) = P(A)P(B) ⇔ P(A|B) = P(A)

### Random Variables & Distributions
- **Discrete Random Variables** - Countable outcomes (Bernoulli, Binomial, Poisson)
- **Continuous Random Variables** - Uncountable outcomes (Uniform, Normal, Exponential)
- **Probability Mass Function (PMF)** - P(X=x) for discrete
- **Probability Density Function (PDF)** - f(x) where P(a≤X≤b) = ∫_a^b f(x)dx
- **Cumulative Distribution Function (CDF)** - F(x) = P(X≤x)

### Key Distributions in ML
- **Bernoulli** - Binary outcomes (coin flip)
- **Binomial** - Number of successes in n trials
- **Poisson** - Number of events in fixed interval
- **Uniform** - Equal probability over interval
- **Normal (Gaussian)** - Bell curve, ubiquitous due to CLT
- **Exponential** - Time between events in Poisson process
- **Beta** - Distribution over probabilities [0,1]
- **Dirichlet** - Generalization of Beta to multiple dimensions

### Expectation & Variance
- **Expected Value (Mean)** - E[X] = Σ xp(x) or ∫ xf(x)dx
- **Variance** - Var(X) = E[(X-μ)^2] = E[X^2] - (E[X])^2
- **Standard Deviation** - σ = √Var(X)
- **Covariance** - Measures joint variability: Cov(X,Y) = E[(X-μ_X)(Y-μ_Y)]
- **Correlation** - Normalized covariance: ρ = Cov(X,Y)/(σ_Xσ_Y) ∈ [-1,1]

### Important Inequalities & Limits
- **Law of Large Numbers** - Sample average converges to expected value
- **Central Limit Theorem** - Sum of i.i.d. variables approaches normal distribution
- **Chebyshev's Inequality** - P(|X-μ|≥kσ) ≤ 1/k^2
- **Markov's Inequality** - P(X≥a) ≤ E[X]/a for a>0, X≥0
- **Jensen's Inequality** - f(E[X]) ≤ E[f(x)] for convex f

## Information Theory

### Entropy & Information
- **Entropy (Shannon)** - H(X) = -Σ p(x)log₂ p(x)
  - Measures uncertainty/surprise in random variable
  - Maximum when uniform distribution
  - Minimum (0) when deterministic
- **Conditional Entropy** - H(Y|X) = -Σ p(x,y)log₂ p(y|x)
- **Mutual Information** - I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)
  - Measures reduction in uncertainty about Y from knowing X
  - Symmetric: I(X;Y) = I(Y;X)
  - Zero iff X and Y are independent
- **KL Divergence** - D_KL(P||Q) = Σ p(x)log₂[p(x)/q(x)]
  - Measures how one distribution diverges from another
  - Not symmetric, not a true distance
  - Always ≥ 0, equals 0 iff P=Q

### Applications in ML
- **Decision Trees** - Information gain for feature selection
- **Maximum Likelihood Estimation** - Minimize KL divergence to empirical distribution
- **Variational Inference** - Minimize KL divergence to true posterior
- **Autoencoders** - Minimize reconstruction error related to entropy
- **Generative Models** - VAEs, GANs involve information-theoretic objectives

## Optimization Techniques

### Convex Optimization
- **Convex Sets** - Line segment between any two points lies in set
- **Convex Functions** - Epigraph is convex set
- **Properties** - Any local minimum is global minimum
- **Common Forms**
  - Least Squares - ||Ax-b||²₂
  - Linear Programming - cᵀx subject to Ax≤b
  - Quadratic Programming - ½xᵀQx + cᵀx subject to constraints
  - Semidefinite Programming - Optimization over PSD matrices

### Optimization Algorithms
- **Gradient-Based Methods**
  - Gradient Descent - θ ← θ - α∇f(θ)
  - Stochastic Gradient Descent (SGD) - Use mini-batch gradient
  - Momentum - Accelerate SGD in relevant direction
  - Nesterov Momentum - Look ahead before updating
  - Adagrad - Adaptive learning rates per parameter
  - RMSprop - Addresses Adagrad's diminishing learning rates
  - Adam - Combines momentum and RMSprop advantages
- **Second-Order Methods**
  - Newton's Method - Uses Hessian for quadratic approximation
  - Quasi-Newton (BFGS) - Approximates Hessian
  - Conjugate Gradient - For large sparse systems
- **Constrained Optimization**
  - Lagrange Multipliers - Convert constrained to unconstrained
  - Karush-Kuhn-Tucker (KKT) Conditions - Necessary for optimality
  - Projected Gradient Descent - Project onto feasible set after gradient step

### Practical Considerations
- **Learning Rate Scheduling** - Decrease α over time (step decay, exponential, cosine)
- **Regularization** - Prevent overfitting (L1/L2, dropout, early stopping)
- **Batch Normalization** - Normalize layer inputs for stable training
- **Initialization** - Xavier/Glorot, He initialization for neural networks
- **Gradient Clipping** - Prevent exploding gradients in RNNs

---

*Related Notes:*
- [[05-AI-Research/AI Fundamentals]]
- [[mathematics_master]]
- [[03-Resources/Knowledge Management System]]
- [[07-Cybersecurity/Cryptography Math]]
- [[09-Knowledge/Mathematical Foundations of CS]]

*Last updated: May 14, 2026*