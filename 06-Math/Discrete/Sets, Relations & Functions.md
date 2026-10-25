---
tags: [math, discrete-math, sets, relations, functions, cs-foundations, reference]
aliases: [Sets, Relations, Functions, Equivalence Relations, Partial Orders, Lattices]
unit: "Discrete Mathematics — Unit 2"
level: undergraduate
focus: [set-algebra, cardinality, relations, functions, equivalence, partial-orders, zermelo-fraenkel]
updated: 2026
status: reference
---

# Sets, Relations & Functions

> [!abstract] What this note covers
> Sets are the atoms of the subject; relations say how elements of sets connect; functions are the *special* relations that power computation. Together they underlie databases, data structures, type systems, and the "structure-preserving maps" of algebra. Master this note and the rest of discrete math is *about* things you've already met here.
>
> **CS payoffs:**
> - Sets → `set` types in every language, `HashSet`, SQL `IN/NOT IN`, database *relations*.
> - Functions → pure functions in functional programming; `Callable`, `std::function`, `typedef func(...)` in C++.
> - Equivalence relations → **hashing** (a good hash is an equivalence by key-value), **type unification**, **state merging**.
> - Partial orders → **C3 linearization**, **MRO**, **topological sorts**, **module versioning**, **lattice of types**.
> - Relations → **SQL joins**, **graph edges** (a graph is literally a set of vertices plus a binary relation on it).

## 1. Set Notation & Basic Operations

- A **set** is a *collection of distinct objects* (order irrelevant, duplicates collapse).
- `x ∈ A`: "x is an element of A." `x ∉ A`: "x is not in A."
- **Listing:** `A = {1, 2, 3}` or **set-builder:** `A = {x ∈ ℤ : x > 0 ∧ x < 5}`.
- **Key number sets:**
  - `ℕ` = {0, 1, 2, …} (or starts at 1 — check your course)
  - `ℤ` = integers (… , −1, 0, 1, …)
  - `ℚ` = rationals, `ℝ` = reals, `ℂ` = complex.

### 1.1 Subset, equality, empty set

- `A ⊆ B` iff every element of A is in B.
- `A ⊂ B` (proper subset) iff `A ⊆ B` **and** `A ≠ B`.
- `∅` (empty set) is a subset of every set.
- **Equality:** `A = B` iff `A ⊆ B` **and** `B ⊆ A` (the "double-inclusion" proof trick).

> [!example] Prove `A ∩ B ⊆ A ∪ B`.
> Let x ∈ A∩B. By definition x∈A and x∈B. In particular x∈A, so x∈A∪B. Done.
> (Note: this is an *implication* proof — the subset test is just the direct-proof technique from [[Logic & Proof Techniques]] applied to sets.)

### 1.2 Standard operations

| Operation | Notation | Meaning |
|---|---|---|
| Union | `A ∪ B` | elements in A **or** B |
| Intersection | `A ∩ B` | elements in A **and** B |
| Difference | `A − B` | in A, not in B |
| Symmetric difference | `A △ B = (A−B) ∪ (B−A)` | in exactly one |
| Complement | `Ā` (or `Aᶜ`) | in universal set U, not in A |
| Power set | `𝒫(A)` | set of **all** subsets of A |

**De Morgan for sets** (mirror the logic ones):
- `¬(A ∪ B) = Ā ∩ B̄`
- `¬(A ∩ B) = Ā ∪ B̄`

> [!tip] `|𝒫(A)| = 2^{|A|}`
> For a set of n elements there are exactly 2ⁿ subsets (each element in or out). This "power-set size" is why brute-force "try every subset" algorithms are exponential.

## 2. Set Identities & Proof

A "set proof" is done by **double inclusion** (show both directions) or **element chase** (pick an arbitrary element, walk the membership).

### 2.1 The identities you should *know*

| Identity | Name |
|---|---|
| `A ∪ B = B ∪ A` · `A ∩ B = B ∩ A` | commutative |
| `(A∪B)∪C = A∪(B∪C)` · `(A∩B)∩C = A∩(B∩C)` | associative |
| `A∪(B∩C) = (A∪B)∩(A∪C)` | distributive |
| `A∪∅ = A` · `A∩∅ = ∅` | identity |
| `A∪Ā = U` · `A∩Ā = ∅` | complement |
| `A∪A = A` · `A∩A = A` | idempotent |
| `A ⊆ B ⇒ A∩B = A` | absorption |

### 2.2 Inclusion–exclusion for two & three sets

- `|A ∪ B| = |A| + |B| − |A ∩ B|`
- `|A ∪ B ∪ C| = Σ|·| − Σ|pair intersections| + |A∩B∩C|`

> [!example] In a class of 50: 30 like Math, 25 like CS, 10 like both.
> `|M ∪ CS| = 30 + 25 − 10 = 45`. 5 students like neither.

## 3. Cardinality & Countability

The **cardinality** of a set is its "size." For infinite sets, size is subtle:

- **Countably infinite:** bijective with `ℕ` (enumerable). `ℤ` and `ℚ` are countable; `ℝ` is **not** (Cantor's diagonal argument).
- **Uncountable:** `|ℝ| = 𝔠` (continuum), strictly larger than `|ℕ|`.

> [!tip] Why `ℚ` is countable (a classic to know)
> Pair each rational p/q with (p,q) ∈ ℤ², then enumerate ℤ² by "diagonals" (the standard zig-zag). This shows ℚ is a **countably infinite** set — same size as ℕ. Cantor proved `ℝ` is strictly bigger; that result underpins the "reals can't be listed."

> [!warning] Beware "diagonalization" claims
> Cantor's argument: assume you have a *list* `r_1, r_2, r_3, …` of all reals in [0,1]. Define `d` whose nth digit differs from r_n's nth digit. Then d is a real in [0,1] not on the list. Contradiction. So no such listing exists — the reals are **uncountable**.

## 4. Relations

A **relation** on a set S is a *subset of S × S*. A **binary relation** R between A and B is a subset of A × B; if (a,b) ∈ R, we write `a R b`.

> [!tip] A relation is literally just "a bag of ordered pairs"
> `R ⊆ A × B` means R is *any* collection of (a,b) pairs. No other structure is required. This simple fact is why graph theory and relation theory look alike: **a directed graph is (V, E) where E ⊆ V × V** — a relation.

### 4.1 Properties of relations

| Property | Condition | Example |
|---|---|---|
| **Reflexive** | ∀a, aRa | "≤" on ℝ |
| **Symmetric** | aRb ⇒ bRa | "≈" (equivalence) |
| **Antisymmetric** | aRb ∧ bRa ⇒ a=b | "≤" on ℕ |
| **Transitive** | aRb ∧ bRc ⇒ aRc | "∼" (same residue mod n) |
| **Irreflexive** | ∀a, ¬(aRa) | ">" on ℕ |

> [!note] Reflexive vs symmetric vs transitive — the three "big three" properties
> A relation can have any subset of these. The combinations that matter:
> - **Reflexive + symmetric + transitive = equivalence relation** (see §5).
> - **Irreflexive + transitive + antisymmetric = strict partial order.**
> - **Reflexive + antisymmetric + transitive = (non-strict) partial order.**

### 4.2 Composition of relations

Given `R ⊆ A×B`, `S ⊆ B×C`, the **composition** `S∘R ⊆ A×C`:
```
(S ∘ R) = {(a,c) : ∃b. (a,b)∈R ∧ (b,c)∈S}
```
Composition is **associative** but **not commutative**.

## 5. Equivalence Relations (the one that matters most)

An **equivalence relation** on S is a relation that is **reflexive, symmetric, transitive**. It partitions S into **equivalence classes**:

- `[a] = {x ∈ S : x ~ a}`.
- `a ~ b` **iff** `[a] = [b]`.
- The set of all classes is the **quotient** `S/~`.

> [!example] `a ~ b` iff "a and b have the same remainder mod 3"
> Partitions ℤ into 3 classes: `{…, −6, −3, 0, 3, 6, …}`, `{…, −5, −2, 1, 4, 7, …}`, `{…, −4, −1, 2, 5, 8, …}`. Each is a **residue class modulo 3**.

### 5.1 Why equivalence relations matter in CS

1. **Hashing.** A good hash `h: S → K` induces `x ~ y` iff `h(x)=h(y)`. Equivalence classes are the buckets; collisions *are* the class membership.
2. **Type systems.** `T1 ≡ T2` (equivalence) vs `T1 <: T2` (subtyping, a partial order).
3. **Program equivalence.** "These two programs behave the same" is an equivalence relation (modulo observability).
4. **Quotient types** in dependently-typed languages (Idris, Coq, Agda) are literally S/~.

## 6. Functions (special relations: "each input has exactly one output")

A **function** `f: A → B` is a relation where every a∈A is related to **exactly one** b∈B.

- **Domain:** A. **Codomain:** B. **Range/Image:** `f(A) = {b ∈ B : ∃a. b=f(a)}`.
- **Injective (one-to-one):** `f(a₁)=f(a₂) ⇒ a₁=a₂`. Distinct inputs map to distinct outputs.
- **Surjective (onto):** `f(A) = B`. Every codomain element is hit.
- **Bijective:** injective + surjective. Then `f⁻¹` exists and is also a function.
- **Identity:** `id_A: A → A`, `id_A(x)=x`.

> [!tip] Quick tests
> - **Injective:** try to find a, b with a≠b and f(a)=f(b). If none, injective.
> - **Surjective:** for a *generic* y∈B, solve f(x)=y. If you can always find such x, surjective.
> - **Bijective:** prove both.
> - `|A| > |B|` ⇒ **not surjective** onto B. `|A| < |B|` ⇒ **not injective** into B.

### 6.1 Pigeonhole principle (a corollary of cardinality)

> [!abstract] The pigeonhole principle
> If m items go into n boxes and m > n, some box holds ≥ 2 items.
>
> **Generalized:** If m items go into n boxes, some box holds ≥ ⌈m/n⌉ items.
>
> *Use:* proving existence, pigeonhole-lower-bound for collisions in hashes, "13 people ⇒ 2 share a birthday month" (13>12).

> [!example] Hash collision lower bound
> Hash an n-element set into a k-bit key. Pigeonhole: if n > 2^k, **two elements share a hash**. Any k-bit hash of n > 2^k keys *must* collide. That's why "random-looking" keys of 128 bits can still have a birthday attack at ~2^64 inputs.

### 6.2 Inverse images & preimages

- **Inverse image of b:** `f⁻¹(b) = {a ∈ A : f(a) = b}`. A set, even when f isn't invertible.
- **Inverse function** `f⁻¹: B → A` exists **iff** f is bijective; `f⁻¹ ∘ f = id_A`.

### 6.3 Composite functions & inverses of functions

`(f ∘ g)(x) = f(g(x))` — apply g first. `(f ∘ g)⁻¹ = g⁻¹ ∘ f⁻¹` (order reverses!).

> [!example] `(sin)⁻¹(sin(x)) = x`? Only when x is in `[−π/2, π/2]`.
> The inverse *function* of sin (on the restricted domain) is `asin`. But `sin(asin(x)) = x` for x∈[−1,1] always. The two directions differ because functions are bijective only on their chosen domains.

## 7. Partial Orders & Lattices (where "order" generalizes)

A **partial order** `≤` on S: reflexive, antisymmetric, transitive. A **total (linear) order** additionally: any two elements are comparable.

- **Top element:** `∃t. ∀a. a ≤ t` (written ⊤).
- **Bottom element:** `∃b. ∀a. b ≤ a` (⊥).
- A **lattice:** every pair has a join (∨, LUB = maximum) and meet (∧, GLB = minimum).

> [!tip] CS uses these everywhere
> - **Program verification:** a pre/postcondition pair is a Galois connection.
> - **MRO (Python method resolution):** linearization of a lattice of classes.
> - **Effect systems in Haskell:** `IO`, `State`, etc., form a lattice of effects.
> - **Lattice of types:** `int < float < any` is a lattice; type inference walks it.
> - **Dependency resolution:** cargo/pip/solver pick a "maximal" compatible version = join of constraints.

## 8. Set Theorist's Toolkit: Cantor, FizzBuzz, and ZFC

> [!note] Just enough set theory
> - **ZFC axioms** are a *conservative* framework: the standard Zermelo-Fraenkel + Choice. "Choice" lets you pick an element from every member of a collection of nonempty sets. It's independent of the other axioms (Gödel, Cohen proved both ZF and ZF+C consistent relative to each other).
> - **Cantor's theorem:** For any set A, `|𝒫(A)| > |A|`. No set is as big as its power set. This proves the existence of *transfinite* cardinals — `ℵ₀, ℵ₁, ℵ₂, …`.
> - **Diagonalization:** The general method: assume a *complete* list of things in some class; construct one thing that's not on the list; contradiction. Works for reals, for self-referential programs (halting problem!), and for cardinalities.

> [!tip] Diagonalization is the proof technique behind the **halting problem**
> Assume a program H(p, x) decides whether p halts on x. Then D(p) = "if H(p, p) = 'halts', loop forever; else halt." Now ask H(D, D): if it halts, D loops; if it loops, D halts. Contradiction. No such H exists.

## 9. Summary Table

| Concept | One-line test / definition |
|---|---|
| Subset | `a∈B ⇒ a∈A` (for A⊆B) |
| Union/Intersection | OR / AND |
| `A − B` | `A ∩ B̄` |
| Symmetric difference | `(A∪B) − (A∩B)` |
| Power set | All subsets; size `2^n` |
| Reflexive | `∀a. aRa` |
| Symmetric | `aRb ⇒ bRa` |
| Antisymmetric | `aRb ∧ bRa ⇒ a=b` |
| Transitive | `aRb ∧ bRc ⇒ aRc` |
| Equivalence | Reflexive + Symmetric + Transitive |
| Injective | `f(a₁)=f(a₂) ⇒ a₁=a₂` |
| Surjective | `∀b. ∃a. f(a)=b` |
| Bijective | Both; inverse exists |
| Pigeonhole | `n+1 items, n boxes ⇒ 2 in one` |
| Partial order | Reflexive + Antisymmetric + Transitive |
| Lattice | Every pair has a LUB and a GLB |

## 10. Related & Next

- **Prereq:** [[Logic & Proof Techniques]] (proofs of set identities use the same tools).
- **Next:** [[Combinatorics & Counting]] — count the structures we just defined.
- **Cross-links:**
  - Equivalence relations & hashing: see [[class_AI/AI_Foundations_Weeks_1-2]] for applied examples.
  - Pigeonhole in cryptography: see [[class_AI/probability_and_statistics]] (birthday paradox).
  - Graphs: a *directed graph* is literally a binary relation on a vertex set — [[Graph Theory]].

## 11. Self‑Test (active recall)

> [!question] Prove `A ∪ B = B ∪ A` by double inclusion.
> `⊆`: let x∈A∪B. Then x∈A or x∈B. Either way x∈B∪A. `⊇` is the same argument with A, B swapped. So equality.

> [!question] When does a function have an inverse?
> **Bijective** (injective + surjective). Injective: distinct inputs → distinct outputs. Surjective: every codomain element is hit. Both required.

> [!question] Why is "every equivalence relation is transitive" *independent* of "reflexive and symmetric"?
> Reflexive + symmetric do *not* imply transitive. Counterexample: on {a, b, c}, R = {(a,a),(b,b),(c,c),(a,b),(b,a)}. R is reflexive and symmetric but **not** transitive: (a,b)∈R and (b,c)∉R doesn't help, but (a,c)∉R while "a~b" and "b~c" would need "a~c". In fact the transitive closure of R is the universal relation.

> [!question] State Cantor's theorem and prove the finite case (`|𝒫(A)| = 2^{|A|} > |A|` for finite A).
> Finite case: label elements a₁…aₙ; each subset corresponds to a bit-string of length n. There are 2ⁿ strings, so 2ⁿ subsets, and 2ⁿ > n for all n ≥ 0 (induction on n). Infinite case: diagonalize.

> [!question] Pigeonhole: 100 people, 12 months. What can you say?
> ⌈100/12⌉ = 9 — at least 9 share a birthday *month*. Stronger form: some month has ≥ 9 people born in it.

> [!question] What is the *inverse image* of a point under a non-invertible function?
> A *set* of all preimages. E.g., `f⁻¹(4)` for `f(x)=x²` on `ℝ` is `{−2, 2}`. The inverse image is well-defined even when no inverse *function* exists.
