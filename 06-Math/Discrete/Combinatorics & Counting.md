---
tags: [math, discrete-math, combinatorics, counting, cs-foundations, reference]
aliases: [Combinatorics, Counting, Permutations, Combinations, Binomial Theorem, Pigeonhole, Generating Functions]
unit: "Discrete Mathematics — Unit 3"
level: undergraduate
focus: [product-rule, permutations, combinations, binomial, pigeonhole, inclusion-exclusion, generating-functions]
updated: 2026
status: reference
---

# Combinatorics & Counting

> [!abstract] What counting *really* is
> Combinatorics answers one question: **"how many?"** — but it's never "just count them one by one." It's about finding a *formula* for the size of a big set without enumerating it. The discipline is really four meta-skills:
>
> 1. **Build the object step by step** (product rule).
> 2. **Map two sets to each other** (bijection) to count one by counting the other.
> 3. **Use complement/pigeonhole** when "counting what you want" is hard.
> 4. **Count twice** (double counting) to prove identities.
>
> The **first** move in any counting problem is to *name the method* you're using — "this is a C(n,k) situation because order doesn't matter and selection is without replacement." Naming the tool before the arithmetic is what earns marks and prevents errors.

## 1. The Fundamental Rules

### 1.1 Addition & Multiplication rules

- **Addition rule:** disjoint cases → add. `|A ∪ B| = |A| + |B|` when `A ∩ B = ∅`.
- **Multiplication (product) rule:** independent choices → multiply. "Choose a shirt (5) then a tie (3)" ⇒ `5·3 = 15`.

> [!tip] If it's "AND" → multiply; if it's "OR" (disjoint) → add.
> That one-sentence heuristic solves most naive counting. "At least one" problems are where it breaks — use complement (§1.4).

### 1.2 Factorials & Permutations

- `n! = n·(n−1)·…·1`, with `0! = 1` (the empty product).
- **Permutation** `P(n,k) = _nP_k = n!/(n−k)!` = ordered selection of k from n.
  - Example: top-3 finishers in a race of 10 = `P(10,3) = 10·9·8 = 720`.

> [!note] "Ordered" vs "unordered" is *the* decision that picks the formula
> | Situation | Method |
> |---|---|
> | Order **matters**, no repeats | Permutation `n!/(n−k)!` |
> | Order **doesn't matter**, no repeats | Combination `C(n,k)` |
> | Order matters, **repeats allowed** | `n^k` |
> | Order doesn't matter, **repeats allowed** | `C(n+k−1, k)` (stars & bars) |

### 1.3 Binomial coefficients

`C(n, k) = n! / (k!(n−k)!)` = ways to choose k items from n, **order irrelevant**.

**Core identities** (each is a two-line double-counting argument):
- Symmetry: `C(n,k) = C(n, n−k)` (choosing who's *in* vs who's *out*).
- Pascal: `C(n,k) = C(n−1,k−1) + C(n−1,k)`.
- **Sum:** `Σ_{k=0}^{n} C(n,k) = 2ⁿ` (the power set is a "2ⁿ" because each of n elements is in-or-out).
- **Vandermonde:** `Σ_k C(r,k)C(s,n−k) = C(r+s, n)`.

> [!example] `C(n,k)` grows to its maximum at k = n/2
> Since `C(n,k) = C(n,n−k)` and the row peaks in the middle (binomial distribution shape), `C(20,10) = 184756` is the largest term in row 20. This "peak at the middle" is why the *most* ways to split n people is half-and-half.

## 2. The Pigeonhole Principle (revisited & sharpened)

Recall from [[Sets, Relations & Functions]] §6.1: `m` objects into `n` boxes, `m > n` ⇒ some box holds ≥ 2. Generalized: some box holds ≥ `⌈m/n⌉`.

**The hard part is *choosing the boxes*.** The principle itself is trivial; the skill is inventing the right "boxes."

> [!example] Among any 37 people, 3 share a birth-month *and* birth-weekday.
> 12 months × 7 weekdays = 84 "boxes." 37 < 84, so we *can't* use the plain pigeonhole here. (This is why "37 is enough to guarantee 2 share a month" — ⌈37/12⌉ = 4 — is the right claim, not 3-with-both.)
> Careful: **the boxes you pick determine the conclusion.**

> [!example] Prove: in any set of n+1 integers from {1, …, 2n}, two are in a divisibility relation.
> **Boxes:** group by "odd part." Every integer m = 2^a · (odd). There are only n distinct odd parts (1,3,5,…,2n−1) in {1,…,2n}. By pigeonhole, two of the n+1 chosen share an odd part, so one divides the other. A beautiful "right boxes" example.

## 3. Inclusion–Exclusion (counting with overlaps)

When sets *overlap*, "add and subtract" to avoid double-counting:

```
|A ∪ B|                    = |A| + |B| − |A∩B|
|A ∪ B ∪ C|                = |A| + |B| + |C|
                             − |A∩B| − |A∩C| − |B∩C|
                             + |A∩B∩C|
```

General form:
```
|∪_{i} A_i| =  Σ|A_i|  −  Σ|A_i∩A_j|  +  Σ|A_i∩A_j∩A_k|  −  …  (+/−)
```
(add singletons, subtract pairs, add triples, …; sign `=(−1)^(m−1)` for m-fold intersections.)

> [!tip] "At least one" = total − "none" (the complement shortcut)
> Instead of inclusion–exclusion over many sets, often easiest: **count the complement.** "How many 5-card hands have *at least one* spade?" = `C(52,5) − C(39,5)` (subtract the hands with *no* spade).

> [!example] Derangements (the "no fixed points" count)
> `!n` = permutations of n with no element in its original position (a "derangement"). Inclusion–exclusion gives:
> `!n = n! · Σ_{k=0}^{n} (−1)^k / k!`
> - `!1 = 0`, `!2 = 1`, `!3 = 2`, `!4 = 9`.
> - `!n ≈ n!/e` (rounded). This is why the "wrong-hat problem" probability → `1/e` as n grows.

## 4. The Binomial Theorem

```
(x + y)^n =  Σ_{k=0}^{n}  C(n,k) · x^{n−k} · y^{k}
```

**Why it's true (the combinatorial argument):** `(x+y)^n` is the product of n copies of `(x+y)`. Expanding means picking x *or* y from each copy. The term `x^{n−k}y^k` arises by choosing y from exactly k of the n factors — that's `C(n,k)` choices. Sum over k. ∎

> [!example] `(1 + x)^5 = 1 + 5x + 10x² + 10x³ + 5x⁴ + x⁵`
> Coefficients 1,5,10,10,5,1 are row 5 of Pascal's triangle.

### 4.1 Negative / fractional exponents (generalized binomial)

For `|x| < 1`:
```
(1 + x)^r =  Σ_{k=0}^{∞}  C(r,k) x^k,      where C(r,k) = r(r−1)…(r−k+1)/k!
```
Example: `1/√(1−x) = Σ C(n, n−1) x^n` type expansions — used in counting *repeated* selections (see §5.3).

## 5. Advanced Counting

### 5.1 Stars and Bars (combinations with repetition)

> [!abstract] Number of ways to put `n` *identical* items into `k` *distinct* boxes
> = `C(n + k − 1, k − 1)` = `C(n + k − 1, n)`.
>
> **The bijection:** each solution of `x₁ + x₂ + … + x_k = n` (xᵢ ≥ 0) corresponds to placing `n` stars and `k−1` bars among `n + k − 1` positions; choosing where the `k−1` bars go.

> [!example] Flavors of ice cream
> 7 scoops, 5 flavors, repeats allowed = `C(7 + 5 − 1, 7) = C(11, 7) = C(11,4) = 330`.

### 5.2 The Inclusion–Exclusion "hat-check" identity

`Σ_{k=0}^{n} (−1)^k C(n,k) = 0` (from `P(n,0) + P(n,1) + … ` style, or binomial theorem at x = −1). The derangement formula above is the "weighted" version.

### 5.3 Generating functions (turn counting into algebra)

A **generating function** packages a sequence `(a_0, a_1, a_2, …)` into a formal power series:
```
A(x) =  a_0 + a_1 x + a_2 x² + …  =  Σ a_n x^n
```
**The trick:** multiplying generating functions *counts* products of choices.

> [!example] Ways to make $n with coins
> A single coin of value v contributes a factor `1 + x^v + x^{2v} + … = 1/(1−x^v)`.
> Using $1, $2, $5 coins: the generating function is
> `1 / [(1−x)(1−x²)(1−x⁵)]`, and the coefficient of `x^n` is the number of ways to make $n.
>
> The **coefficient-extraction** operation is written `[x^n]`. E.g., `[x^3] 1/((1−x)(1−x²)(1−x⁵))` = 3 (the ways: 1+1+1, 1+2, … enumerate: {1,1,1}, {2,1} , {2,?} … the coefficient is 3).

> [!tip] The standard *geometric* GFs you'll use constantly
> | Structure | GF |
> |---|---|
> | "0 or 1 or 2 or … of something of weight w" | `1 + x^w + x^{2w} + … = 1/(1−x^w)` |
> | "exactly one of a menu" | a polynomial sum |
> | Fibonacci numbers | `Σ F_n x^n = x/(1 − x − x²)` |

The Fibonacci GF is a beautiful worked example — deriving it:

> [!example] `Σ_{n≥0} F_n x^n = x/(1 − x − x²)`
> `F_{n} = F_{n−1} + F_{n−2}` (with F₀=0, F₁=1).
> Let `G = Σ F_n x^n`. Then `xG = Σ F_n x^{n+1} = Σ F_{n−1} x^n` and `x²G = Σ F_{n−2} x^n`. So `G − xG − x²G = F_0 + F_1 x = x` (since F₀=0, F₁=1). Thus `G(1−x−x²) = x`, i.e. `G = x/(1−x−x²)`. ∎

## 6. A Python sanity check (count big binomials exactly)

```python
from math import comb

# C(52, 5) = number of 5-card poker hands
n_cards, choose = 52, 5
total = comb(n_cards, choose)          # exact integer
print("5-card hands:", total)          # 2598960

# Inclusion–exclusion: hands with AT LEAST ONE card of value 'A'
# = total − (hands with NO ace)
no_ace = comb(48, choose)              # 48 non-ace cards
at_least_one_ace = total - no_ace
print("hands with >=1 ace:", at_least_one_ace)

# Stars & bars: 7 identical scoops into 5 flavors = C(7+5-1, 7)
print("ice cream:", comb(7 + 5 - 1, 7))

# Pigeonhole lower bound: guarantee 2 people share a birth-month
people, boxes = 13, 12
import math
print("worst single month >= ", math.ceil(people / boxes))  # 2
```

## 7. Related & Next

- **Prereqs:** [[Logic & Proof Techniques]] (double-counting *is* proof by bijection), [[Sets, Relations & Functions]] (bijection, pigeonhole).
- **Next:** [[Number Theory & Recurrence Relations]] — counting meets integers; generating functions (§5.3) solve the recurrences there.
- **Applied:** running-time bounds in algorithms come from counting inputs (`n log n` etc.) — see the CS side of [[Generative AI - Map of Content]] when you study algorithms.
- **Hub:** [[Discrete Mathematics - Map of Content]].

## 8. Self‑Test (active recall)

> [!question] Ordered or unordered? Repeats allowed? — Pick the formula for "top 3 of 10 racers."
> **Ordered, no repeats** ⇒ Permutation `P(10,3) = 10·9·8 = 720`.

> [!question] `C(20, 10)` vs `C(20, 19)` — which is bigger?
> `C(20,10)` (184756). By symmetry `C(20,19)=C(20,1)=20`. The middle of the row is the peak.

> [!question] Use the **complement** to count "at least one ace in a 5-card hand."
> `C(52,5) − C(48,5) = 2,598,960 − 1,712,304 = 886,656`.

> [!question] Stars & bars: nonneg solutions to `a+b+c+d = 10`.
> `C(10 + 4 − 1, 4 − 1) = C(13,3) = 286`.

> [!question] What is the coefficient of `x^4` in `1/(1−x)(1−x²)`?
> = "ways to make 4 with $1 and $2 coins" = {1,1,1,1}, {2,1,1}, {2,2} = 3.

> [!question] Prove by double counting that `Σ C(n,k) = 2^n`.
> LHS: sum of "ways to choose a k-subset of an n-set" for all k = "all subsets." RHS: each of n elements independently in/out = `2^n`. Both count the power set. ∎
