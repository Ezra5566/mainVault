---
tags: [physics, kinematics, mechanics, undergraduate, reference]
domain: science
category: 01
count: 12
unit: "Physics — Unit 1: Kinematics"
level: undergraduate
focus: [position, velocity, acceleration, constant acceleration, free fall, projectile motion]
updated: 2026
status: reference
---

# Kinematics

> [!abstract] Why kinematics is first
> Kinematics is the study of **motion without considering its causes**. You describe *where* something is, *how fast* it's moving, and *how its speed is changing*, using pure geometry and algebra. All of dynamics (forces → acceleration) builds on the kinematic foundation. If you can't read a velocity-versus-time graph or write the three constant-acceleration equations from memory, you'll struggle everywhere else in this course.
>
> **CS payoff:** robot arm path planning, projectile-target leading, physics-engine parameter tuning, and anything involving trajectories (game AI, drone delivery, satellite deployment).

## 1. Position, Displacement, and Vectors

A **position vector** $\vec{r}$ specifies where a particle is relative to an origin. In 1D we write $x$; in 2D/3D we use $\vec{r} = (x, y)$ or $\vec{r} = (x, y, z)$.

|| Symbol | Meaning | Typical units |
|---|---|---|
| $\vec{r}$ | position vector | m |
| $x, y, z$ | Cartesian components | m |
| $\Delta \vec{r}$ | displacement | m |
| $s$ | distance traveled (scalar) | m |

> [!question] Displacement vs. distance
> A jogger runs around a circular track of radius $R = 50\,\text{m}$ and completes exactly one lap. What are (a) the displacement, and (b) the distance traveled?
> *(click to reveal)*
>
> **Reveal:** (a) $\Delta \vec{r} = \vec{0}$ (back where they started); (b) distance $= 2\pi R \approx 314\,\text{m}$.

## 2. Velocity (Instantaneous and Average)

**Average velocity:** $\vec{v}_{\text{avg}} = \dfrac{\Delta \vec{r}}{\Delta t}$.

**Instantaneous velocity:** the time derivative,
$$\vec{v}(t) = \lim_{\Delta t \to 0} \frac{\Delta \vec{r}}{\Delta t} = \frac{d\vec{r}}{dt}.$$

In 1D we drop the vector arrow and write $v = dx/dt$. The **speed** is $v = |v|$.

> [!question] Sign of velocity
> A particle moves along the $x$-axis. Its position is $x(t) = t^3 - 6t^2 + 9t$. At $t = 2\,\text{s}$, is the velocity positive, negative, or zero?
> *(click to reveal)*
>
> **Reveal:** $v = dx/dt = 3t^2 - 12t + 9$; at $t = 2$, $v = 12 - 24 + 9 = -3 < 0$, so velocity is negative (moving left).

## 3. Acceleration (Instantaneous and Average)

**Average acceleration:** $\vec{a}_{\text{avg}} = \dfrac{\Delta \vec{v}}{\Delta t}$.

**Instantaneous acceleration:** the time derivative,
$$\vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}.$$

In 1D: $a = dv/dt = d^2x/dt^2$.

> [!question] Constant acceleration
> If $a = -9.8\,\text{m/s}^2$ (free fall, upward positive), and a ball is thrown upward with $v_0 = 15\,\text{m/s}$ from $y_0 = 0$, how long until it hits the ground? Use Python to verify.
> *(click to reveal)*
>
> **Reveal:** Python:
> ```python
> import numpy as np
> g = 9.8
> v0 = 15.0
> # y(t) = y0 + v0*t - 1/2*g*t^2; solve y=0
> coeff = [-0.5*g, v0, 0]   # a*t^2 + v*t + y0  (but y0=0 so constant term vanishes)
> # Actually y(t) = v0*t - 0.5*g*t^2 = t*(v0 - 0.5*g*t)
> roots = np.roots([-0.5*g, v0, 0])  # one root is t=0, the other is t = 2*v0/g
> t_land = roots[1]
> print(f"t_land = {t_land:.2f} s")  # ≈ 3.06 s
> ```

## 4. The Three Constant-Acceleration Equations (SUVAT)

These are the workhorse formulas for any problem where $a$ is constant.

| Equation | When to use |
|---|---|
| $v = v_0 + a t$ | You know $v_0, a, t$ and want $v$. |
| $x = x_0 + v_0 t + \frac{1}{2} a t^2$ | You know $x_0, v_0, a, t$ and want $x$. |
| $v^2 = v_0^2 + 2a (x - x_0)$ | You know $v_0, a, \Delta x$ and want $v$ (no $t$ needed). |

> [!question] Which SUVAT?
> A car traveling at $20\,\text{m/s}$ brakes with $a = -5\,\text{m/s}^2$. How far does it travel before stopping?
> *(click to reveal)*
>
> **Reveal:** We know $v_0 = 20$, $v = 0$, $a = -5$, and we want $\Delta x$. The equation $v^2 = v_0^2 + 2a\Delta x$ gives $0 = 400 + 2(-5)\Delta x \Rightarrow \Delta x = 40\,\text{m}$.

## 5. Free Fall (Constant $g$)

Near Earth's surface, $g \approx 9.81\,\text{m/s}^2$ downward. With "up = positive":

- $a = -g$
- $v(t) = v_0 - g t$
- $y(t) = y_0 + v_0 t - \frac{1}{2} g t^2$

> [!question] Peak height
> A ball is thrown vertically upward with $v_0 = 20\,\text{m/s}$. (a) How high does it go? (b) How long is it in the air?
> *(click to reveal)*
>
> **Reveal:** (a) At the peak $v = 0$, so $0 = v_0 - g t_{\text{peak}} \Rightarrow t_{\text{peak}} = v_0/g = 20/9.81 \approx 2.04\,\text{s}$. Then $y_{\text{peak}} = v_0 t_{\text{peak}} - \frac{1}{2}g t_{\text{peak}}^2 \approx 20.4\,\text{m}$. (b) Total time in air $= 2 t_{\text{peak}} \approx 4.08\,\text{s}$ (symmetry of parabola).

> [!example] Python verification of peak height
> ```python
> v0, g = 20.0, 9.81
> t_peak = v0/g
> y_peak = v0*t_peak - 0.5*g*t_peak**2
> print(f"peak height = {y_peak:.2f} m (expect ~20.4)")
> # Also check total time
> t_total = 2*t_peak
> print(f"total time   = {t_total:.2f} s (expect ~4.08)")
> ```

## 6. Projectile Motion (2D Constant Acceleration)

Treat horizontal and vertical motions **independently**. Horizontal: $a_x = 0$, so $v_x = v_{0x}$ is constant. Vertical: $a_y = -g$.

- $x(t) = x_0 + v_{0x} t$
- $y(t) = y_0 + v_{0y} t - \frac{1}{2} g t^2$
- Range (level ground, launch speed $v_0$, angle $\theta$): $R = \dfrac{v_0^2 \sin(2\theta)}{g}$, maximum at $\theta = 45^\circ$.

> [!question] Projectile range
> A projectile is launched at $v_0 = 25\,\text{m/s}$, $\theta = 30^\circ$. What is the range $R$? (Neglect air resistance.)
> *(click to reveal)*
>
> **Reveal:** $R = \dfrac{25^2 \sin(60^\circ)}{9.81} = \dfrac{625 \cdot \sqrt{3}/2}{9.81} \approx 55.1\,\text{m}$.

> [!example] Python range calculation
> ```python
> v0, theta, g = 25.0, np.radians(30), 9.81
> R = v0**2 * np.sin(2*theta) / g
> print(f"range = {R:.2f} m (expect ~55.1)")
> ```

## Summary Table: Kinematics Symbols

|| Symbol | Meaning | SI Unit |
|---|---|---|
| $x, y, z$ | Position coordinates | m |
| $\vec{r}$ | Position vector | m |
| $v, v_0$ | Speed / initial speed | m/s |
| $\vec{v}$ | Velocity vector | m/s |
| $a, a_0$ | Acceleration / initial acceleration | m/s² |
| $\vec{a}$ | Acceleration vector | m/s² |
| $t$ | Time | s |
| $g$ | Acceleration due to gravity | m/s² |

## Self‑Test (cover the answers, then reveal)

1. **Define** displacement and distinguish it from distance traveled.
2. **Derive** $v = v_0 + a t$ from the definition of constant acceleration (hint: $a = \Delta v / \Delta t$).
3. **Problem:** A truck accelerates from rest at $3\,\text{m/s}^2$. How far does it travel in $t = 8\,\text{s}$?
4. **Problem:** A stone is dropped (thrown downward at $v_0 = 2\,\text{m/s}$) from a $45\,\text{m}$ cliff. How long until it hits the ground? (Use the quadratic formula; Python can check.)
5. **Problem:** A soccer ball is kicked at $15\,\text{m/s}$ at $35^\circ$ above horizontal. Find the time of flight, maximum height, and range. (Neglect air resistance.)

> [!tip] How to use these self-tests: cover the right side of each `> [!question]` box, answer from memory, then reveal. If you can't, re-read the subsection and try again tomorrow — the spaced‑recall is what makes it stick.

## Related

- [[06-Math/Physics/Physics - Map of Content]] — the hub for the full course.
- [[06-Math/Calculus]] — derivatives and integrals that turn $x(t)$ ↔ $v(t)$ ↔ $a(t)$.
- [[06-Math/Discrete]] — the proof logic; conservation of energy and momentum are proved there.