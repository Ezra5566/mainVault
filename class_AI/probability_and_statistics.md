---
title: Probability & Statistics for AI
tags: [math, probability, statistics, week2-4, ai-foundations]
week: 2
---

## Why Probability & Statistics Matter in AI
- **Uncertainty Quantification** – Models must express confidence in predictions.  
- **Learning from Data** – Algorithms infer patterns from sample distributions.  
- **Decision Making** – Expected value, risk, and hypothesis testing guide actions.

## Core Concepts

### 1. Probability Foundations
| Concept | Notation | Intuition |
|---------|----------|-----------|
| **Sample Space (Ω)** | – | All possible outcomes of an experiment. |
| **Event** | \(E \subseteq \Omega\) | A set of outcomes we care about. |
| **Probability of an Event** | \(P(E)\) | Likelihood of the event, \(0 \le P(E) \le 1\). |
| **Complement** | \(E^c\) | Outcomes not in \(E\); \(P(E^c)=1-P(E)\). |
| **Union & Intersection** | \(E \cup F,\; E \cap F\) | “Or” and “And” of events. |
| **Conditional Probability** | \(P(E|F)=\frac{P(E\cap F)}{P(F)}\) | Probability of \(E\) given that \(F\) occurred. |
| **Independence** | \(P(E\cap F)=P(E)P(F)\) | Knowing \(F\) does not change the chance of \(E\). |

### 2. Random Variables (RVs)
- **Discrete RV** – Takes countable values (e.g., roll of a die).  
  - **Probability Mass Function (PMF)**: \(P(X = x)\).  
- **Continuous RV** – Takes values in a continuum (e.g., height).  
  - **Probability Density Function (PDF)**: \(f_X(x)\); \(P(a \le X \le b)=\int_a^b f_X(x)dx\).  
- **Expected Value (Mean)**  
  - Discrete: \(\mathbb{E}[X]=\sum_x x\,P(X=x)\)  
  - Continuous: \(\mathbb{E}[X]=\int x\,f_X(x)dx\)  
- **Variance & Standard Deviation**  
  - \(\operatorname{Var}(X)=\mathbb{E}[(X-\mu)^2]\)  
  - \(\sigma_X=\sqrt{\operatorname{Var}(X)}\)

### 3. Common Distributions Used in AI
| Distribution | Type | Typical AI Use‑Case |
|--------------|------|---------------------|
| **Bernoulli** | Discrete (binary) | Modeling binary outcomes (e.g., click/no‑click). |
| **Binomial** | Discrete (counts) | Number of successes in \(n\) trials (e.g., correct answers). |
| **Multinoulli (Categorical)** | Discrete (K outcomes) | Classification labels. |
| **Gaussian (Normal)** | Continuous | Modeling measurement errors, latent variables in VAEs. |
| **Multivariate Gaussian** | Continuous (vector) | Covariance modeling, Gaussian processes. |
| **Poisson** | Discrete (counts) | Event rates (e.g., arrivals per unit time). |
| **Beta / Dirichlet** | Continuous (probabilities) | Prior distributions for multinomial parameters (Bayesian inference). |

### 4. Key Theorems
- **Law of Large Numbers** – Sample average converges to the expected value as data grows.  
- **Central Limit Theorem** – Sum of i.i.d. variables approximates a Gaussian distribution.  
- **Bayes’ Theorem** – Updates belief about hypotheses given evidence:  
  \[
  P(H|D)=\frac{P(D|H)P(H)}{P(D)}
  \]  
  Used in Naïve Bayes classifiers, Bayesian networks, and posterior inference.

### 5. Statistical Inference
- **Estimation** – Point estimates (e.g., maximum likelihood) vs. interval estimates (confidence intervals).  
- **Hypothesis Testing** – Null vs. alternative; p‑value, Type I/II errors.  
- **P‑value & Significance** – Probability of observing data as extreme as recorded under the null hypothesis.

## Connection to AI Projects
- **Model Uncertainty** – Use predictive variances (e.g., Bayesian Neural Networks) to flag out‑of‑distribution inputs.  
- **Evaluation Metrics** – Accuracy, precision, recall, F1 derive from counts (TP, FP, FN) rooted in probabilistic definitions.  
- **Sampling & Data Augmentation** – Monte‑Carlo sampling, bootstrapping to generate training data.  
- **Probabilistic Programming** – PyMC3, Stan for hierarchical models that capture complex dependencies.

## Quick Exercises
1. If a fair coin is tossed 100 times, what is the expected number of heads?  
2. Compute the expected value of a Binomial(n=10, p=0.2) distribution.  
3. Using Bayes’ theorem, calculate \(P(\text{Spam}|\text{Word}=“free”) \) given:  
   - \(P(\text{Spam}) = 0.2\)  
   - \(P(\text{Word}=“free”|\text{Spam}) = 0.1\)  
   - \(P(\text{Word}=“free”) = 0.05\)  

---

> **Tip:** When coding, leverage libraries such as `numpy`, `scipy.stats`, and `torch.distributions` to instantiate these distributions and compute probabilities, expectations, and gradients automatically.

---

> **Cluster hub:** see [[Generative AI - Map of Content]] for the full AI/ML map of content and study path.
