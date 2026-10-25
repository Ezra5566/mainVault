---
tags: [math, discrete-math, logic, proof, cs-foundations, reference]
aliases: [Logic, Propositional Logic, Predicate Logic, Proof Techniques, Proofs]
unit: "Discrete Mathematics — Unit 1"
level: undergraduate
focus: [propositions, connectives, tautologies, predicates, quantifiers, proof-techniques, induction]
updated: 2026
status: reference
---

# Logic & Proof Techniques

> [!abstract] Why this is first
> Everything else in discrete math is written in the language of **logic**. If you can't translate a sentence like "there exists a prime larger than n" into formal symbols, you can't prove anything reliably. This note gives you the **vocabulary** (propositional & predicate logic) and the **five tools** you'll use to prove almost anything else in this course.
>
> The CS payoff is direct: propositional logic *is* the design of logic gates and digital circuits; predicate logic is what database queries (SQL `WHERE`) and theorem provers operate in; and induction is how you prove a program correct by loop size.

## 1. Propositions

A **proposition** is a statement that is either *true* or *false* (never both, never neither). Its value is called its **truth value**.

| Example | Proposition? | Why |
|---|---|---|
| `2 + 3 = 5` | ✅ | Has a definite truth value (true) |
| `n > 10` | ❌ | A **predicate** — depends on `n` |
| `The moon is made of cheese` | ✅ | False, but definite |
| `x is an integer` | ❌ | Open variable, no value yet |

Variables `p, q, r, ...` stand for propositions. `T`/`⊤` = true, `F`/`⊥` = false.

## 2. Logical Connectives (Propositional Logic)

| Symbol | Name | Meaning | `p⊕q` true when… |
|---|---|---|---|
| `¬p` | negation | not p | p is false |
| `p ∧ q` | conjunction | and | **both** true |
| `p ∨ q` | disjunction | or (inclusive) | at least one true |
| `p ⊕ q` | exclusive or | exactly one | exactly one true |
| `p → q` | implication | if p then q | p false, or q true |
| `p ↔ q` | biconditional | iff | p and q agree |

> [!warning] The two traps that fail exams
> 1. **Inclusive vs exclusive "or."** In math/logic, `∨` is *inclusive* (true when both are true). "Coffee or tea" in a menu is exclusive (XOR); `p ⊕ q` is true only when *exactly one* holds.
> 2. **Implication is not "cause."** `p → q` is *false only* when p is true and q is false (a "broken promise"). If `p` is false, `p → q` is **true** no matter what `q` is. This is called *vacuous truth*. Example: "If 1=2, then the moon is in the Pacific" is **true** — the premise is false.

> [!tip] Read `p → q` as "p is sufficient for q, q is necessary for p."
> "If it rains, the ground gets wet": rain *suffices* for wet ground; wet ground is *necessary* only in the sense that we're asserting this rule.

### 2.1 Tautologies, Contradictions, Satisfiability

- A formula is a **tautology** if true in *every* row of its truth table (e.g., `p ∨ ¬p`, the law of excluded middle).
- A **contradiction** is false in every row (e.g., `p ∧ ¬p`).
- **Satisfiable** = has at least one true row; **unsatisfiable** = no true rows.
- Two formulas **p, q** are **logically equivalent** (`p ≡ q`) iff their truth tables match — equivalently, `p ↔ q` is a tautology.

**Common equivalences you must recognize instantly:**

| Identity | Statement |
|---|---|
| `p → q ≡ ¬p ∨ q` | the workhorse for moving implications |
| `p → q ≡ ¬q → ¬p` | **contrapositive** (always equivalent) |
| De Morgan: `¬(p∧q) ≡ ¬p ∨ ¬q` | negate-and → or |
| De Morgan: `¬(p∨q) ≡ ¬p ∧ ¬q` | negate-or → and |
| `¬(p → q) ≡ p ∧ ¬q` | how to falsify an implication |
| `p → q ∧ p → r ≡ p → (q ∧ r)` | "distribute" implication |

> [!example] Proving an equivalence
> Show `¬(p → q) ≡ p ∧ ¬q`.
> LHS: `p→q ≡ ¬p∨q`, so `¬(¬p∨q) ≡ p ∧ ¬q` (De Morgan). ∎
> Intuition: the only way "if p then q" is *false* is "p true AND q false."

## 3. Predicate Logic (Quantifiers)

A **predicate** `P(x)` is a statement with free variables. Quantifiers bind them:

- `∀x P(x)` — "for all x, P(x)" (**universal**; ∃ = "there exists").
- `∃x P(x)` — "there exists an x with P(x)" (**existential**).

> [!warning] Order of quantifiers *changes the statement*
> - `∀x ∃y (y > x)`: "for every x there's a bigger y" — **true** in reals.
> - `∃y ∀x (y > x)`: "there's a single y bigger than every x" — **false** (no maximum).
>
> Swapping `∀∃` with `∃∀` is *not* allowed. Negating:
> `¬∀x P(x) ≡ ∃x ¬P(x)` and `¬∃x P(x) ≡ ∀x ¬P(x)` (a universal negated is an existential negation, and vice versa).

## 4. Rules of Inference (valid argument forms)

An **argument** is premises → conclusion. **Valid** means: whenever the premises are true, the conclusion must be.

| Name | Form | Status |
|---|---|---|
| **Modus ponens** | `p→q, p ⊢ q` | ✅ valid |
| **Modus tollens** | `p→q, ¬q ⊢ ¬p` | ✅ valid |
| **Hypothetical syllogism** | `p→q, q→r ⊢ p→r` | ✅ valid |
| **Disjunctive syllogism** | `p∨q, ¬p ⊢ q` | ✅ valid |
| **Addition** | `p ⊢ p∨q` | ✅ valid |
| **Simplification** | `p∧q ⊢ p` | ✅ valid |
| **Affirming the hypothesis** | `p→q, p ⊢ q` | ✅ (this is modus ponens) |
| **Denying the hypothesis** | `p→q, ¬p ⊢ ¬q` | ❌ **fallacy** |
| **Affirming the consequent** | `p→q, q ⊢ p` | ❌ **fallacy** |

> [!warning] The two classic fallacies
> - **Affirming the consequent:** "If it's a dog it barks. It barks. Therefore it's a dog." No — cats don't bark, but other animals might; barking doesn't prove dog.
> - **Denying the hypothesis:** "If it's a dog it barks. It's not a dog. Therefore it doesn't bark." No — it might be a lion.
>
> Recognizing these is how you grade a *wrong* proof.

## 5. The Five Proof Techniques (the core skill of the unit)

### 5.1 Direct proof
Assume the hypothesis `p`, deduce the conclusion `q` using definitions and known results.

> [!example] "If n is even, n² is even."
> Let n even ⇒ n = 2k. Then n² = (2k)² = 4k² = 2(2k²). Since 2k² is an integer, n² = 2·(integer) is even. ∎

### 5.2 Proof by contrapositive
To prove `p → q`, prove `¬q → ¬p` (equivalent). Use when the negation is easier.

> [!example] "If n² is odd, n is odd."
> Contrapositive: "If n is even, n² is even." That's the even case in 5.1 above — done. ∎

### 5.3 Proof by contradiction (reductio ad absurdum)
Assume the statement is *false* (i.e., assume `¬S`), derive something impossible (like `0 = 1`), conclude `S`.

> [!example] "√2 is irrational."
> Assume √2 = a/b in lowest terms, a,b integers, b≠0. Then 2b² = a², so a² even ⇒ a even ⇒ a = 2k. Then 2b² = 4k² ⇒ b² = 2k² ⇒ b even. Both even contradicts "lowest terms." ∎

### 5.4 Proof by cases
Partition the domain into cases; prove the statement in each case.

> [!example] "For all integers n, |n−1| + |n| ≥ 1."
> Case n ≤ 0: |n−1| = 1−n, |n| = −n, sum = 1−2n ≥ 1.
> Case 0 < n < 1: impossible for integer n.
> Case n ≥ 1: |n−1| = n−1, |n| = n, sum = 2n−1 ≥ 1. All cases hold. ∎

### 5.5 Mathematical induction (★ the must-know)

Prove `P(n)` for all positive integers n:
1. **Base case:** show `P(1)` (or `P(0)`).
2. **Inductive step:** assume `P(k)` (the *inductive hypothesis*) for an arbitrary k; show `P(k+1)`.
> By induction, `P(n)` holds for all n.

> [!example] Sum of first n integers
> **Claim:** `1 + 2 + … + n = n(n+1)/2`.
> **Base:** n=1 → 1 = 1·2/2 = 1. ✓
> **Step:** assume `1+…+k = k(k+1)/2`. Then
> `1+…+(k+1) = k(k+1)/2 + (k+1) = (k+1)(k/2 + 1) = (k+1)(k+2)/2 = (k+1)((k+1)+1)/2`. ✓
> Hence true for all n. ∎
>
> *Pattern:* to prove `P(k+1)`, add the `(k+1)`-th term to the `P(k)` sum and factor.

> [!tip] Strong vs weak induction
> **Weak** induction assumes `P(k)` only; **strong** induction assumes `P(1)…P(k)` all true and proves `P(k+1)`. Use strong when `P(k+1)` depends on more than `P(k)` (e.g., the Fibonacci recurrence, the Euclidean algorithm's correctness, unique factorization).

## 6. Common Pitfalls

> [!warning] Watch for these
> - **Induction: proving `P(1)` but the step shows `P(k)→P(k+1)`** — you need *both* the base and the step, linked by the hypothesis. A step with no base proves nothing; a base with no step proves only that one value.
> - **Circular reasoning (assuming the conclusion):** "We want to show x = y. Since x = y, we are done." Not a proof.
> - **Dividing by a possibly-zero quantity:** "multiply both sides by 1/a" when a might be 0 — invalid.
> - **Confusing "for some" (∃) with "for all" (∀)** — a universally-quantified statement is proved for an *arbitrary* element; an existential one by *exhibiting* a witness.

## 7. Truth-Table Method (decision tool)

For any propositional formula, list all 2ⁿ assignments, compute the formula row by row. Use it to:
- Decide **tautology / contradiction / satisfiable** (count true rows).
- Check **equivalence** (`p≡q` ⇔ `p↔q` all-true).
- Find a **CNF/DNF** form (useful for SAT and circuit design).

> [!example] Is `p → (p ∨ q)` a tautology?
> Table (rows ppq): `T T T`→T, `T F T`→T, `F T F`→F, `F F F`→F. All true ⇒ tautology. (Indeed `p→(p∨q) ≡ ¬p∨(p∨q) ≡ ¬p∨p ≡ T`, absorption.)

## 8. Links & Related

- Next: [[Sets, Relations & Functions]] — apply this logic to the basic math objects.
- Induction reappears in [[Combinatorics & Counting]] (identities) and [[Number Theory & Recurrence Relations]] (recurrences).
- Predicate/quantifier form is used throughout [[Graph Theory]] proofs.
- The continuous counterpart (limits, ε‑δ, "for all… there exists") lives in [[06-Math/Calculus/mathematics_master]] — the same quantifier discipline.
- Hub: [[Discrete Mathematics - Map of Content]].

## 9. Self‑Test (active recall)

> [!question] What does `p → q` mean in words, and when is it *false*?
> "If p then q." False only when p is **true** and q is **false**. (Vacuously true when p is false.)

> [!question] State De Morgan's laws.
> `¬(p∧q) ≡ ¬p∨¬q` and `¬(p∨q) ≡ ¬p∧¬q`.

> [!question] What's the difference between `∀x∃y` and `∃y∀x`?
> Order matters: "for each x there's *some* y" vs "there's a *single* y that works for every x." The second is much stronger.

> [!question] Name the five standard proof techniques and when each shines.
> Direct (assume p, get q) · Contrapositive (when ¬q is easier) · Contradiction (when "false" leads to absurdity) · Cases (split the domain) · Induction (prove ∀n by base+step).

> [!question] Why is "∃x: x is even" *not* the same as "∀x: x is even"?
> One claims at least one even number exists (exhibit: 2); the other claims *every* number is even (false). Universal proofs use an arbitrary element; existential proofs exhibit a witness.

> [!question] Prove by induction: `2 + 4 + … + 2n = n(n+1)`.
> **Base n=1:** 2 = 1·2 ✓. **Step:** assume `2+…+2k = k(k+1)`. Then `2+…+2k+2(k+1) = k(k+1)+2(k+1) = (k+1)(k+2)`. Hence true for k+1. ∎

> [!question] Prove "if 7 ∣ n² then 7 ∣ n" (you may use that 7 is prime).
> **Contradiction:** assume 7 ∤ n. Since 7 prime, 7 doesn't divide n's factorization, so 7 doesn't divide n² — but it does (given). Contradiction. Hence 7 ∣ n. (This generalizes: for prime p, p∣n²⇒p∣n.)

> [!question] Identify the fallacy: "If a number is divisible by 4, it's even. It's not even, so it's not divisible by 4."
> Actually **valid** — that's modus tollens (`p→q, ¬q ⊢ ¬p`), not a fallacy. The *fallacy* would be denying the hypothesis ("it's not divisible by 4, so it's not even").
