---
tags: [physics, university-intro, mechanics, thermodynamics, waves, eandm, reference]
domain: science
category: 06
count: 30
updated: 2026
status: reference
parent: "[[06-Math - Map of Content]]"
focus: [kinematics, dynamics, energy-momentum, rotational-motion, thermodynamics, waves-eandm]
level: undergraduate
---

# Physics — Map of Content

> [!abstract] What this branch is
> Introductory university physics (typically two semesters: **Mechanics + Thermal & Waves**, with a second semester of **Electricity & Magnetism + Optics**). The goal here is the same as the discrete-math notes: give you a **self-contained reference** you can return to and learn from, not a shortcut. Each note covers one major topic, with the key equations, the underlying physical intuition, and a few runnable Python examples so you can verify you have the algebra right.
>
> This branch pairs with [[06-Math/Calculus]] (the continuous math you'll use to derive everything) and [[06-Math/Discrete]] (the rigorous proof logic). Think of it as the "applied math for the physical world."

> [!tip] Study order (recommended)
> 1. [[Kinematics]] — describe motion (position, velocity, acceleration) without asking why.
> 2. [[Dynamics]] — forces and Newton's laws; why things move the way they do.
> 3. [[Energy & Momentum]] — work-energy theorem, conservation laws, collisions.
> 4. [[Rotational Motion]] — extended bodies, torque, angular momentum.
> 5. [[Thermodynamics]] — temperature, heat, entropy, engines.
> 6. [[Waves & E&M]] — oscillations, waves, electric & magnetic fields (second-semester topics).

> Why CS / AI majors should care:
> - **Mechanics** → robot arm kinematics, physics engines, projectile-target leading.
> - **Energy / Momentum** → conservation laws appear in gradient-descent step sizes, collision detection, robot dynamics.
> - **Thermodynamics** → entropy & information theory, bounds on computation (Landauer's principle).
> - **Waves / E&M** → signal processing, electromagnetic radiation, optics for computer vision.

> Then loop back and **re-do the `> [!question]` self-tests** at the end of each note before an exam or project kickoff.

## The Standard Intro Unit, Mapped

|| Block | Note | The one-sentence takeaway |
|---|---|---|---|
| **1. Kinematics** | [[Kinematics]] | Motion described by $x(t), v(t), a(t)$; the three constant-acceleration equations are your Swiss Army knife. |
| **2. Dynamics** | [[Dynamics]] | $F = ma$; forces explain the *why* of motion; friction, circular motion, and drag. |
| **3. Energy & Momentum** | [[Energy & Momentum]] | Work–energy theorem + momentum conservation; elastic vs. inelastic collisions. |
| **4. Rotational Motion** | [[Rotational Motion]] | $\tau = I\alpha$; moment of inertia, rolling without slip, angular momentum. |
| **5. Thermodynamics** | [[Thermodynamics]] | $Q = \Delta U + W$; first & second law, entropy, ideal-gas PV diagrams, engines. |
| **6. Waves & E&M** | [[Waves & E&M]] | Superposition & interference; Coulomb's law, Gauss's law, circuits, Faraday's law. |

*(supporting)* | [[Kinematics]] §2 | Projectile motion is just constant-acceleration in 2D with $g$ vertical. |

## How the Topics Connect

```text
Kinematics → (positions → velocities →) 
   │                                   │
   ▼                                   ▼
Dynamics    Energy & Momentum →  Rotational Motion
   │                                   │
   ▼                                   ▼
Thermodynamics →  Waves & E&M
```

All of these are unified under one core idea: **a system’s state is specified by a minimal set of variables, and the laws of physics tell you how those variables evolve.**

## Self‑Study Loop (how to actually use these notes)

1. Read a note top‑to‑bottom **once** for the big picture.
2. Do the `> [!question]` self‑tests **from memory**, then reveal.
3. Work the `> [!example]` worked examples by hand *before* reading the solution.
4. If a Python snippet is included, run it and check the output against a hand-calculated sanity check.
5. Revisit a week later; the spaced‑recall is what makes it stick (see [[03-Resources/Knowledge Management System]]).

## Related Notes (across the vault)

- [[06-Math/Calculus]] — the continuous math (derivatives, integrals) you’ll use to go from $a(t)$ → $v(t)$ → $x(t)$, and from forces → work → energy.
- [[06-Math/Discrete]] — the rigorous proof logic; conservation laws are typically proved by Noether’s theorem or by isolating a closed system.
- [[03-Resources/Knowledge Management System]] — the spaced‑recall system for sticking these long-term.
- [[Generative AI - Map of Content]] — the wider study cluster this supports.

---

Individual notes follow. Each one uses the same pattern: YAML frontmatter with `tags:`, `aliases:`, `unit:`, `level:`, `focus:`, `updated:`, `status:`; an opening `> [!abstract]` callout; numbered sections with tables of key symbols; `> [!question]` self-test toggles; and `> [!example]` worked examples with runnable Python where appropriate.