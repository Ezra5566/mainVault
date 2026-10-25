---
tags: [math, discrete-math, number-theory, recurrences, cryptography, cs-foundations, reference]
aliases: [Number Theory, Recurrence Relations, Euclidean Algorithm, Modular Arithmetic, Discrete Logarithms]
unit: "Discrete Mathematics — Unit 4"
level: undergraduate
focus: [divisibility, euclidean, congruence, modular, primes, recurrence, characteristic-equation, closed-forms]
updated: 2026
status: reference
---

# Number Theory & Recurrence Relations

> [!abstract] Two topics, one reason they sit together
> Both are about **integers** and **sequences that build on themselves**. Number theory gives you the raw material (divisibility, congruences, primes) and recurrences give you the machinery to solve "what is the nth term?" — which is exactly the question behind algorithm running times. The bridge: **generating functions** (seen in [[Combinatorics & Counting]] §5.3) turn a recurrence into a closed form.
>
> **CS payoffs:**
> - **Modular arithmetic** → `clock` arithmetic, `hash % table_size`, `x & (n−1)`, cyclic buffers.
> - **Euclidean GCD** → cryptography (RSA uses the extended GCD to find modular inverses).
> - **Primes** → RSA, elliptic-curve crypto, prime-based hash tables, Miller–Rabin primality tests.
> - **Recurrences** → *directly* the analysis of divide-and-conquer (`T(n) = 2T(n/2) + O(n)`), which is the Master Theorem's territory. If you study algorithms, this note is the warm-up.

## 1. Divisibility & Fundamentals

- **`a | b`** (read "a divides b"): ∃k ∈ ℤ with b = ak.
- **Greatest common divisor** `gcd(a, b)` = largest integer dividing both.
- **Relatively prime (coprime):** `gcd(a, b) = 1`.
- **Prime** `p > 1`: divisors are exactly 1 and p.

### 1.1 The Division Algorithm

For integers `a` and `b > 0`: there exist *unique* integers `q, r` with
```
a = b·q + r,    0 ≤ r < b
```
where `q = ⌊a/b⌋` and `r = a mod b`. This is the foundation of **every** modular-arithmetic fact below.

> [!note] `a mod b` is **not** "the remainder of a ÷ b" in the naive sense — it's a *class* of integers.
> In Python, `(-7) % 4 == 1` (the result is always non-negative for positive b). In C, `-7 % 4 == -3`. The *math* convention uses the non-negative representative in `[0, b)`.

### 1.2 The Euclidean Algorithm (★ GCD in practice)

**Claim:** `gcd(a, b) = gcd(b, a mod b)`. Iterate until remainder 0.

```
gcd(48, 18):
  48 = 2·18 + 12
  18 = 1·12 +  6
  12 = 2· 6 +  0
  ⇒ gcd(48, 18) = 6
```

> [!tip] Why this works (one line)
> Any common divisor of a, b divides `a − (a mod b)·q = b·q + r − r = b·q`… no wait, cleaner: a = bq + r, so gcd(a,b) = gcd(b, a−bq) = gcd(b, r).

### 1.3 Bézout's identity & the Extended Euclidean Algorithm

If `g = gcd(a, b)`, there exist **integers x, y** with `ax + by = g`. The extended algorithm (same recursion, carry the coefficients back) finds them:

```python
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y

print(egcd(48, 18))   # (6, -1, 3)  because 48(-1) + 18(3) = 6
```

> [!tip] Use this to solve `ax + by = c` — the Diophantine equation
> `ax + by = c` has *integer* solutions **iff** `gcd(a,b) | c`. If it does, every solution is a "particular" + `(b/g)·t` shifts in x, `(-a/g)·t` shifts in y.

## 2. Congruences & Modular Arithmetic

### 2.1 Definitions

- `a ≡ b (mod m)` (or `a ≡ b mod m`): **m | (a − b)**.
- `[a]` = the residue class of a modulo m = `{k ∈ ℤ : k ≡ a (mod m)}`.

### 2.2 The arithmetic rules

Congruence is compatible with addition/multiplication:
```
a ≡ b, c ≡ d (mod m)  ⇒  a+c ≡ b+d,  a·c ≡ b·d  (mod m)
```
And **exponentiation**: if `a ≡ b (mod m)` then `a^n ≡ b^n (mod m)` for n ≥ 0.

> [!tip] The "simplify-and-check" trick
> To compute a huge power mod m, peel off digits base-by-base. E.g. `3^100 mod 7`: `3^1 = 3, 3^2 = 2, 3^3 = 6 ≡ -1, 3^6 ≡ 1`. Since 6 | 100… no, 6 ∤ 100. Use `3^6 ≡ 1`, so `3^96 ≡ 1`, `3^100 ≡ 3^4 ≡ 4`.

### 2.3 Fermat's Little Theorem

For prime `p` and `a` with `p ∤ a`:
```
a^(p-1) ≡ 1 (mod p)
```
Equivalent: `a^p ≡ a (mod p)` for **all** integers a.

> [!example] `3^7 mod 7`? Fermat says `3^6 ≡ 1`, so `3^7 ≡ 3`.
> This is the backbone of **modular exponentiation** (a fast pow mod m in O(log n) via squaring) — Python's built-in `pow(a, n, m)` uses exactly this.

### 2.4 Euler's theorem (Fermat generalized)

For any `a` coprime to `m`:
```
a^(φ(m)) ≡ 1 (mod m)
```
where `φ(m)` = Euler's totient (count of integers in `[1, m]` coprime to m).
- For prime `p`, `φ(p) = p − 1` (Fermat).
- For `m = p^k`, `φ(m) = p^k − p^{k−1} = p^{k−1}(p−1)`.
- **Multiplicative:** `φ(pq) = φ(p)φ(q)` when p, q are distinct primes.

### 2.5 Chinese Remainder Theorem (CRT)

> [!abstract] Theorem
> If `m₁, m₂` are **coprime** and
> ```
> x ≡ a (mod m₁)
> x ≡ b (mod m₂)
> ```
> then there is a **unique** `x (mod m₁m₂)` solving both.
>
> Generalizes to n pairwise-coprime moduli.

**How it's used in CS:**
- **RSA:** encryption is a pair of congruences (one mod p, one mod q). CRT makes RSA keygen ~4× faster.
- **Hashing with combined prime moduli:** "give me a residue that's 3 mod 7 and 5 mod 11" is the CRT question.
- **Distributing work:** parallel computations mod pairwise-coprime primes can be combined at the end.

> [!example] Solve `x ≡ 3 (mod 7)` and `x ≡ 5 (mod 11)`.
> `x = 3 + 7k`. Need `3 + 7k ≡ 5 (mod 11) ⇒ 7k ≡ 2 (mod 11)`. Inverse of 7 mod 11: `7·8 = 56 ≡ 1`, so `k ≡ 16 ≡ 5 (mod 11)`. So `k = 5 + 11j` and `x = 3 + 7(5+11j) = 38 + 77j`. Answer: `x ≡ 38 (mod 77)`.

## 3. Primes & Their Arithmetic

### 3.1 Unique factorization (Fundamental Theorem of Arithmetic)

> [!abstract] Every integer n ≥ 2 is a **unique** product of primes (up to ordering).
> `n = p₁^{e₁} · p₂^{e₂} · … · p_k^{e_k}` with p₁ < p₂ < … < p_k primes.
>
> This is **the** theorem number theory is built on. "Uniqueness" means the exponents are also unique.

> [!note] Why uniqueness is non-obvious (a common exam question)
> The *existence* of a factorization is trivial (factor a composite repeatedly). **Uniqueness** is the hard part — it's false for some non-integral domains (e.g., in the ring `ℤ[√−5]`, `6 = 2·3 = (1+√−5)(1−√−5)` is *two* different prime factorizations). The theorem is special to `ℤ`.

### 3.2 Density of primes & the prime number theorem

- `π(n)` = number of primes ≤ n.
- **Prime Number Theorem:** `π(n) ~ n/ln n` and `p_n ~ n ln n` as n → ∞.
- **Consequence:** primes are "sparse" (probability that n is prime ≈ 1/ln n).

### 3.3 Gaps, twin primes, Mersenne, and the famous open questions

- **Twin primes:** pairs `(p, p+2)` — conjectured infinitely many (open).
- **Mersenne primes:** `2^p − 1` prime ⇒ p prime (converse fails).
- **Goldbach:** every even > 2 is a sum of two primes (open for 300+ years).
- **Riemann Hypothesis:** all non-trivial zeros of ζ(s) have real part 1/2 — implies the "best possible" error term on `π(n)`.

### 3.4 Computational primality testing

- **Trial division:** O(√n). Good only for n < 10^12 or so.
- **Miller–Rabin:** probabilistic, O(k log²n). "Almost certainly prime" — the standard for large numbers.
- **AKS:** deterministic polynomial time (2002), but impractical.

> [!tip] In cryptography, keys are *large* primes (RSA is ~2048-bit)
> You don't find primes by trial division. You pick a random odd number, increment by 2 until Miller–Rabin says "probably prime," then use the **Proth / Lucas** primality tests to prove it. RSA security rests on the **hardness of factoring** `pq`, not on the *existence* of primes.

## 4. Recurrence Relations (the "solve me" part)

### 4.1 What is a recurrence?

A **recurrence** defines a sequence by giving initial terms and a rule linking later terms to earlier ones.

Examples:
- **Fibonacci:** `F_0 = 0, F_1 = 1, F_n = F_{n-1} + F_{n-2}`.
- **Linear:** `a_0 = 1, a_n = 2 a_{n-1} + 3` ⇒ solve for closed form.

The goal: find a **closed-form** expression `a_n = f(n)` that gives the nth term *directly* (no recursion needed).

### 4.2 Linear recurrences with constant coefficients

A **linear homogeneous recurrence of order k**:
```
a_n = c₁ a_{n-1} + c₂ a_{n-2} + … + c_k a_{n-k}
```
with k initial conditions.

**Method:**
1. Write the **characteristic equation**: `r^k − c₁ r^{k-1} − … − c_k = 0`.
2. Find its roots `r₁, …, r_k`.
3. General solution: `a_n = A₁ r₁^n + A₂ r₂^n + … + A_k r_k^n` (for **distinct** roots).
4. Use the k initial conditions to solve for `A₁ … A_k`.

> [!example] Solve `a_n = 3 a_{n-1} − 2 a_{n-2}`, with `a_0 = 1, a_1 = 4`.
> **Characteristic:** `r² = 3r − 2`, i.e. `r² − 3r + 2 = 0`, roots `r = 1, 2`.
> **General form:** `a_n = A·1^n + B·2^n = A + B 2^n`.
> **Conditions:** `a_0 = A + B = 1`; `a_1 = A + 2B = 4`. Subtract: `B = 3`, `A = −2`.
> **Answer:** `a_n = −2 + 3·2^n`.
> **Check:** `a_0 = −2 + 3 = 1` ✓; `a_1 = −2 + 6 = 4` ✓; `a_2 = −2 + 12 = 10`, and recurrence gives `a_2 = 3·4 − 2·1 = 10` ✓.

### 4.3 Repeated roots

If root `r` has multiplicity m, the solution includes terms `(A_1 + A_2 n + … + A_m n^{m−1}) r^n`.

> [!example] `a_n = 4 a_{n-1} − 4 a_{n-2}`, `a_0 = 1, a_1 = 2`.
> Characteristic: `r² − 4r + 4 = (r−2)²`, repeated root `r = 2`.
> General form: `a_n = (A + Bn) 2^n`.
> `a_0 = A = 1`; `a_1 = (A + B)·2 = 2(A+B) = 2` ⇒ `A+B = 1` ⇒ `B = 0`.
> So `a_n = 1 · 2^n = 2^n`. Simple answer, but the *technique* (repeated root ⇒ polynomial factor in n) is what matters.

### 4.4 Non-homogeneous recurrences (with a forcing term)

`a_n = c a_{n-1} + f(n)` where `f(n)` is, say, a constant, linear, polynomial, exponential, or sinusoid.

**Method (undetermined coefficients / annihilator):**
1. Solve the **homogeneous** part `b_n = c b_{n-1}` ⇒ `b_n = C·c^n`.
2. Find a **particular** solution `p_n` of the full recurrence (guess the shape from `f`).
3. General solution: `a_n = b_n + p_n`.

> [!example] `a_n = 2 a_{n-1} + 1`, `a_0 = 1`.
> Homogeneous: `a_n^(h) = C·2^n`.
> Try a constant particular `p_n = A` (since f = 1 is constant): `A = 2A + 1` ⇒ `A = −1`.
> General: `a_n = C·2^n − 1`. `a_0 = C − 1 = 1` ⇒ `C = 2`.
> **Answer:** `a_n = 2^{n+1} − 1`. (This is the "1, 3, 7, 15, …" sequence: 2ⁿ−1 shifted.)

### 4.5 Generating functions to the rescue (revisited)

When the characteristic equation is painful (e.g., Fibonacci), use the GF technique:
```
G(x) = Σ a_n x^n
```
Multiply by `(1 − c₁x − c₂x²)` (the characteristic polynomial's *reversed* version) and the right side telescopes to a rational function of `x`. Then **partial fractions** give you `a_n` as a linear combination of geometric series.

> [!example] Fibonacci GF (worked out fully in [[Combinatorics & Counting]] §5.3)
> `F_0 = 0, F_1 = 1, F_n = F_{n-1} + F_{n-2}` gives `G(x) = x/(1 − x − x²)`.
> Partial fractions over `1 − x − x² = (1 − αx)(1 − βx)` (roots `α = (1+√5)/2`, `β = (1−√5)/2`) gives:
> `F_n = (α^n − β^n)/√5` (Binet's formula).
> The `√5` in the denominator makes it *integer* despite the irrational pieces — because `α^n − β^n` is always divisible by `√5` (an induction argument on n).

### 4.6 The Master Theorem preview (where this connects to CS)

**Algorithms** recurrences usually look like:
```
T(n) = a·T(n/b) + f(n)      (divide into a subproblems of size n/b, do f(n) work)
```
**Master Theorem** (a *tool*, not derived in this course usually):
- If `f(n) = O(n^{log_b a − ε})` for some ε > 0, `T(n) = Θ(n^{log_b a})`.
- If `f(n) = Θ(n^{log_b a})`, `T(n) = Θ(n^{log_b a} log n)`.
- If `f(n) = Ω(n^{log_b a + ε})` and regular, `T(n) = Θ(f(n))`.

> [!example] Merge sort: `T(n) = 2T(n/2) + O(n)`. Here `a = 2, b = 2`, `log_b a = 1`. `f(n) = Θ(n^1)` = case 2, so `T(n) = Θ(n log n)`.
> Quicksort (average): `T(n) = 2T(n/2) + O(n)` → same recurrence, same Θ(n log n) on average.
> Strassen's matrix mult: `T(n) = 7T(n/2) + O(n²)` → `log₂ 7 ≈ 2.807` → Θ(n^2.807).

## 5. A Python sanity check (compute a recurrence exactly)

```python
def egcd(a, b):
    """Extended Euclidean algorithm. Returns (g, x, y) with a*x + b*y = g = gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y

# Bézout coefficients for 48, 18:
print(egcd(48, 18))   # (6, -1, 3)

# Modular inverse of 7 mod 11 via extended gcd:
g, x, _ = egcd(7, 11)
print(g, x)            # 1, -3   (inverse is -3 ≡ 8 (mod 11), since 7·8 = 56 = 5·11 + 1)

# Solve x ≡ 3 (mod 7), x ≡ 5 (mod 11) via CRT:
x1, m1, x2, m2 = 3, 7, 5, 11
# Full CRT construction:
# x = x1 + m1 * t; need m1*t ≡ x2 - x1 (mod m2)
inv_m1_mod_m2 = None
for t in range(m2):
    if (m1 * t) % m2 == (x2 - x1) % m2:
        inv_m1_mod_m2 = t
        break
x = x1 + m1 * inv_m1_mod_m2
print("CRT x =", x, "mod", m1 * m2)   # 38 mod 77
```

## 6. Related & Next

- **Prereqs:** [[Logic & Proof Techniques]] §5 (induction is how you verify a recurrence's closed form), [[Combinatorics & Counting]] §5 (generating functions).
- **Next:** [[Graph Theory]] — recurrences on trees / DAGs (e.g., dynamic programming) live in graph land.
- **Applied:**
  - **Master Theorem** is *the* running-time tool for divide-and-conquer algorithms; see the algorithms track of [[Generative AI - Map of Content]] when you study it.
  - **RSA key generation** uses `φ(n)`, the extended GCD, and fast modular exponentiation — all from this note.
  - **Cryptographic protocol design** (key exchange, signatures) is a direct application of modular arithmetic + Euler's theorem.
- **Hub:** [[Discrete Mathematics - Map of Content]].

## 7. Self‑Test (active recall)

> [!question] What is `3^200 mod 7`?
> Fermat: `3^6 ≡ 1 (mod 7)`. `200 = 6·33 + 2`, so `3^200 ≡ 3² = 9 ≡ 2 (mod 7)`.

> [!question] Solve `x ≡ 2 (mod 5)` and `x ≡ 3 (mod 7)` by CRT.
> `x = 2 + 5t`. `2 + 5t ≡ 3 (mod 7)` ⇒ `5t ≡ 1 (mod 7)`. Inverse of 5 mod 7: `5·3 = 15 ≡ 1`, so `t ≡ 3 (mod 7)`. `x = 2 + 5·3 = 17`. Check: `17 ≡ 2 (mod 5)` ✓, `17 ≡ 3 (mod 7)` ✓.

> [!question] Solve the recurrence `a_n = 2 a_{n-1} + 3`, `a_0 = 0`, by the method of undetermined coefficients.
> Homogeneous: `b_n = C·2^n`. Try particular `p_n = A` (constant, since f = 3 is constant): `A = 2A + 3` ⇒ `A = −3`. General: `a_n = C·2^n − 3`. `a_0 = C − 3 = 0` ⇒ `C = 3`. **Answer:** `a_n = 3·2^n − 3`.

> [!question] Why does the extended GCD give a modular inverse?
> `a·x + b·y = gcd(a,b)`. If `gcd(a,b) = 1`, then `a·x ≡ 1 (mod b)`. So `x` is the inverse of `a mod b`. This is *exactly* how RSA and Diffie–Hellman compute `d` (private exponent) from `e` (public exponent) — `e·d ≡ 1 (mod φ(n))`.

> [!question] `F_10 = ?`
> `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55`. `F_10 = 55`. Binet: `(φ^10 − ψ^10)/√5` where `φ = (1+√5)/2 ≈ 1.618` and `ψ = (1−√5)/2 ≈ −0.618`. Both powers grow as `|φ|^10 ≈ 122.99` and `|ψ|^10 ≈ 0.0081`. Difference ≈ 122.98. Divide by `√5 ≈ 2.236` gives ≈ 55.0. ✓

> [!question] Merge sort recurrence `T(n) = 2T(n/2) + O(n)` — what's T(n)?
> Master Theorem case 2: `a = 2, b = 2`, `log_b a = 1`, `f(n) = Θ(n^1)` → `T(n) = Θ(n log n)`.

> [!question] Why does unique factorization fail in `ℤ[√−5]`?
> `6 = 2 · 3 = (1 + √−5)(1 − √−5)`. Each factor is *irreducible* in that ring, yet the two factorizations are distinct. So the "Fermat's theorem" of that ring — uniqueness — is false. (The ring is not a UFD.)
