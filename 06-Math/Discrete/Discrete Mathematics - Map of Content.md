---
tags: [math, discrete-math, cs-foundations, campus, reference]
aliases: [Discrete Math MOC, Discrete Mathematics, DM]
unit: "Discrete Mathematics"
level: undergraduate
focus: [logic, proof, sets, relations, combinatorics, number-theory, recurrence, graph-theory]
updated: 2026
status: reference
---

# Discrete Mathematics — Map of Content

> [!abstract] What this branch is
> Discrete math is the mathematics of **separated, countable things** — the opposite of calculus (continuous). It is the foundation of computer science, logic, and most of modern "proof-based" mathematics. If you study AI/CS, this is the unit that teaches you *how to reason rigorously*, not just how to compute.
>
> It pairs with the continuous side already in this vault: see [[Mathematics for ML]] (linear algebra + calculus) and [[06-Math/Calculus/mathematics_master]] — discrete and continuous are the two halves of the math you actually use.
>
> **Study order** (each note is self-contained but reads best in this sequence):
>
> 1. [[Logic & Proof Techniques]] — the *language* of math: propositions, logic, and how to prove things.
> 2. [[Sets, Relations & Functions]] — the *objects* math talks about.
> 3. [[Combinatorics & Counting]] — *counting* things systematically.
> 4. [[Number Theory & Recurrence Relations]] — integers, divisibility, and sequences that solve themselves.
> 5. [[Graph Theory]] — networks, connectivity, and "what can you reach?"
>
> Then loop back and redo the **Self‑Test** toggles at the end of each note before exams.

**Why CS majors need this:** logic → programs; sets/relations → databases & functions; combinatorics → algorithm running times & cryptography; number theory → hashing, cryptography, checksums; graphs → networks, maps, social media, dependency resolution. Every topic below has a concrete CS payoff spelled out in its note.

---

## The Standard Campus Unit, Mapped

Most undergraduate "Discrete Mathematics" (e.g., Rosen's *Discrete Mathematics and Its Applications*) runs these six blocks. Each is one of the notes in this folder.

| Block | Note | The one-sentence takeaway |
|---|---|---|
| **1. Logic & Proofs** | [[Logic & Proof Techniques]] | How to build and verify rigorous arguments — propositional + predicate logic, truth tables, and the five proof techniques. |
| **2. Sets & Relations** | [[Sets, Relations & Functions]] | The basic data structures of math: sets, and how elements relate to each other (functions, equivalence, partial orders). |
| **3. Counting** | [[Combinatorics & Counting]] | Exact ways to count: permutations, combinations, the pigeonhole principle, inclusion–exclusion, and the binomial theorem. |
| **4. Number Theory & Recurrences** | [[Number Theory & Recurrence Relations]] | Divisibility, the Euclidean algorithm, modular arithmetic, and solving recurrences (Fibonacci and its ilk). |
| **5. Graphs** | [[Graph Theory]] | Vertices + edges: connectivity, Euler/Hamilton paths, trees, coloring, and planar graphs. |
| *(supporting)* | [[Logic & Proof Techniques]] §7 | Mathematical induction lives here but is *used* in recurrences, combinatorics, and graph proofs. |

---

## How the Topics Connect

```
                 Logic & Proof Techniques
                 (propositions, predicates, proofs, induction)
                            │  enables reasoning everywhere
        ┌───────────────┬───┴───────┬──────────────────┐
        ▼               ▼           ▼                  ▼
  Sets/Relations  Counting   Number Theory      Graph Theory
  (objects &       (counting  (integers,        (networks,
   mappings)       structures) divisibility,    trees, paths)
        │          │           recurrence)            │
        └──────────┴──────────────────────────────────┘
                       all built on the same logic
```

- **Induction** (Logic §5) is the proof engine behind combinatorial identities, recurrence solutions, and graph properties (e.g., a tree on n vertices has n−1 edges).
- **Equivalence relations** (Sets §4) underlie congruence (Number Theory) and state minimization.
- **Counting** feeds the *running-time* bounds that graphs and algorithms rely on.

---

## What a Serious Student Should Be Able to Prove (the exam bar)

> [!warning] "Knowing" vs "can prove"
> In a proof-based discrete course, you're not marked on the answer, you're marked on a *valid argument*. The minimum bar:
> - Translate English math statements into logical form and check validity.
> - Prove a statement by **direct proof, contradiction, contrapositive, and induction** — and name which you're using.
> - Manipulate sets with union/intersection/complement and prove set equalities.
> - Solve a counting problem by **name the method first** (product rule, pigeonhole, inclusion–exclusion, bijection) before computing.
> - Find a closed form for a recurrence and *verify* it by substitution/induction.
> - Decide whether a graph is connected / has an Euler path / is a tree, and justify it.

---

## Self‑Study Loop (how to actually use these notes)

1. Read a note top-to-bottom **once** for the big picture.
2. Do the `> [!question]` self-tests **from memory**, then reveal.
3. Work the `[!example]` worked examples by hand *before* reading the solution.
4. Revisit a week later; the spaced-recall is what makes it stick (see [[03-Resources/Knowledge Management System]]).

---

## Related Notes (across the vault)

- [[Mathematics for ML]] — the continuous/linear side.
- [[06-Math/Calculus/mathematics_master]] · [[06-Math/Calculus/math_formulas_comprehensive]] — calculus.
- [[class_AI/Mathematics_for_AI_Weeks_2-4]] · [[class_AI/probability_and_statistics]] — the AI-adjacent math.
- [[09-Knowledge/Study Plan/Mathematics Roadmap]] — the schedule; add this discrete branch to it.
- [[Generative AI - Map of Content]] — the wider study cluster this supports.
