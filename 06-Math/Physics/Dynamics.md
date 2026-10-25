---
tags: [physics, dynamics, mechanics, newtons-laws, undergraduate, reference]
domain: science
category: 02
count: 14
unit: "Physics — Unit 2: Dynamics"
level: undergraduate
focus: [newtons-laws, friction, circular-motion, drag, inertial-frames]
updated: 2026
status: reference
---

# Dynamics

> [!abstract] Why dynamics follows kinematics
> Kinematics tells you *how* things move; dynamics tells you *why*. The cornerstone is **Newton's three laws**. Once you can draw a correct free-body diagram and apply $\sum \vec{F} = m\vec{a}$, you can solve for accelerations, forces, and the resulting motion. This is the notes section where most students spend the most study time — it's also where the CS payoff is most direct (robot arm dynamics, vehicle collision simulation, physics engine design).

> **CS payoff:** robot joint torque calculation, vehicle crash simulation, game physics (collision resolution), drone flight control.

## 1. Newton's Three Laws (in Your Own Words)

| Law | Statement | What it lets you do |
|---|---|---|
| **1st** (Inertia) | An object at rest stays at rest, and an object in motion stays in motion with constant velocity, unless a net external force acts. | Identify *equilibrium* problems ($\sum \vec{F} = \vec{0}$). |
| **2nd** (F = ma) | The acceleration of an object is $\vec{a} = \sum \vec{F} / m$. | Relate net force to acceleration; solve for any of the three. |
| **3rd** (Action–Reaction) | Forces always come in pairs: if A pushes B, B pushes A with equal magnitude and opposite direction. | Analyse interaction pairs (tension, normal, drag). |

> [!question] Which law?
> You press against a wall with your hands. Which of Newton's laws explains why your hands feel the wall pushing back?
> *(click to reveal)*
>
> **Reveal:** Newton's 3rd Law: the force your hands exert on the wall and the force the wall exerts on your hands are an action–reaction pair.

## 2. Force Diagrams (Free-Body Diagrams)

The single most important skill in dynamics: **isolate the object** of interest, then draw every *real* force acting on it.

|| Force type | Symbol in FBD | Direction | When it appears |
|---|---|---|---|
| Gravity (weight) | $\vec{w} = m\vec{g}$ | Downward (toward Earth's center) | Always, near Earth's surface |
| Normal force | $\vec{n}$ | Perpendicular to the surface, pointing *out* of the surface | Surfaces in contact, no friction |
| Friction (static or kinetic) | $\vec{f}$ | Parallel to the surface, opposing relative motion (or tendency) | Surfaces in contact; static if "not moving", kinetic if sliding |
| Tension | $\vec{T}$ | Along the rope/string, pulling *away* from the object | Massless ropes, pulleys, cables |
| Applied force | $\vec{F}_a$ | Whatever direction the pusher/puller applies | Hand, engine, rocket thrust |
| Air/drag resistance | $\vec{D}$ | Opposite to velocity direction; $\|\vec{D}\| = \frac{1}{2}\rho C_d A v^2$ (high speed) | projectiles, vehicles at speed |

> [!question] FBD for a block on an incline
> A block of mass $m$ rests on a frictionless incline of angle $\theta$. Draw the FBD and identify the three forces. What is the acceleration?
> *(click to reveal)*
>
> **Reveal:** Three forces: (1) weight $mg$ downward, (2) normal $n$ perpendicular to the incline, (3) no friction. Resolution: $a = g \sin\theta$ down the incline.

## 3. Newton's Second Law in 1D and 2D

**1D:** $F_{\text{net}} = m a$ (scalar, with sign convention).

**2D:** Break into components:
$$F_{x,\text{net}} = m a_x, \qquad F_{y,\text{net}} = m a_y.$$

> [!example] Python: sliding block with friction
> ```python
> m, g, theta, mu_k = 3.0, 9.81, np.radians(30), 0.25
> # Incline: mg sinθ down, mg cosθ normal, friction = mu_k * n opposite motion
> n = m * g * np.cos(theta)              # normal force
> f_k = mu_k * n                         # kinetic friction magnitude
> a_x = g * np.sin(theta) - f_k / m    # net acceleration along incline
> print(f"a = {a_x:.2f} m/s² down the incline")
> # If a_x < 0 the block slides down; otherwise it won't start moving.
> ```

## 4. Problem-Solving Strategy (the "4-Step Method")

1. **Draw the FBD** — isolate the object, list all real forces (no "ma" forces).
2. **Choose a coordinate system** — usually align axes with the incline or direction of motion.
3. **Write $\sum F_x = m a_x$ and $\sum F_y = m a_y$** — then solve.
4. **Check:** Does the sign make sense? Is the magnitude reasonable?

> [!question] 4-step check
> A $5\,\text{kg}$ block is pushed up a $20^\circ$ frictionless incline by a $40\,\text{N}$ horizontal force. Use the 4-step method to find the acceleration.
> *(click to reveal)*
>
> **Reveal:** (1) FBD: applied force horizontal, weight downward, normal perpendicular. (2) Axes: $x$ parallel to incline (up the slope positive), $y$ perpendicular. (3) $\sum F_x = F\cos20^\circ - mg\sin20^\circ = m a_x$ → $a_x \approx 1.98\,\text{m/s}^2$ up the incline. (4) Positive → makes sense (force overcomes gravity component).

## 5. Special Cases

### Apparent Weight in an Elevator

If an elevator accelerates upward with $a$, the scale reads $m(g + a)$. If it accelerates downward (free fall, $a = g$), the scale reads zero (weightlessness).

### Drag & Terminal Velocity

For an object falling through air, drag $\propto v^2$ at high speed. Terminal velocity $v_t$ satisfies $mg = \frac{1}{2}\rho C_d A v_t^2$, so $v_t = \sqrt{\frac{2mg}{\rho C_d A}}$.

> [!question] Terminal velocity
> A skydiver of mass $m = 80\,\text{kg}$ has drag coefficient $C_d \approx 1.0$ and cross-sectional area $A \approx 0.7\,\text{m}^2$. Air density $\rho \approx 1.225\,\text{kg/m}^3$. What is $v_t$?
> *(click to reveal)*
>
> **Reveal:** $v_t = \sqrt{\frac{2 \cdot 80 \cdot 9.81}{1.225 \cdot 1.0 \cdot 0.7}} \approx 54\,\text{m/s}$ (≈ 120 mph).

> [!example] Python terminal-velocity check
> ```python
> m, g, rho, Cd, A = 80.0, 9.81, 1.225, 1.0, 0.7
> vt = np.sqrt(2*m*g / (rho*Cd*A))
> print(f"terminal velocity = {vt:.1f} m/s (expect ~54)")
> ```

## Summary Table: Newton's Second Law

|| Concept | Equation | Notes |
|---|---|---|---|
| **Second Law** | $\sum \vec{F} = m \vec{a}$ | Net force = mass × acceleration |
| **1D** | $F_{\text{net}} = m a$ | Scalar with sign |
| **2D** | $\sum F_x = m a_x$, $\sum F_y = m a_y$ | Components independently |
| **Elevator (apparent weight)** | $F_{\text{scale}} = m(g \pm a)$ | Up = $+$, down = $-$ |
| **Terminal speed** | $v_t = \sqrt{2mg/(\rho C_d A)}$ | High-speed drag $\propto v^2$ |

## Self‑Test (cover the answers, then reveal)

1. **State** Newton's three laws in your own words.
2. **Problem:** A $10\,\text{kg}$ block rests on a horizontal table. The coefficient of static friction is $\mu_s = 0.6$. What minimum horizontal force must you apply to start the block moving?
3. **Problem:** Two blocks, $m_1 = 3\,\text{kg}$ on a frictionless table and $m_2 = 2\,\text{kg}$ hanging over a pulley (massless rope, frictionless pulley). Find the acceleration of the system and the tension in the rope.
4. **Problem:** An elevator of mass $1000\,\text{kg}$ accelerates upward at $2\,\text{m/s}^2$. What does the scale read for a $70\,\text{kg}$ person standing inside?
5. **Problem:** A car of mass $1500\,\text{kg}$ traveling at $25\,\text{m/s}$ locks its brakes (coefficient of kinetic friction $\mu_k = 0.6$). How far does it slide before stopping?

> [!tip] Self-test method: write your answer on scratch paper, then uncover. If any step is shaky, re-read that subsection and retry the next day.

## Related

- [[06-Math/Physics/Physics - Map of Content]] — the hub.
- [[06-Math/Physics/Kinematics]] — the motion description you'll attach forces to.
- [[06-Math/Calculus]] — derivatives (instantaneous velocity/acceleration) and integrals (work, impulse).
- [[06-Math/Discrete]] — proofs of conservation laws (Noether's theorem, closed-system reasoning).