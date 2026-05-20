# Comprehensive Mathematics Guide: Algebra and Calculus

This guide provides a thorough exploration of algebraic and calculus formulas, their explanations, examples, and how these two fundamental branches of mathematics work together to solve complex real-world problems.

---

# Part 1: Algebra

## 1.1 Basic Algebraic Operations

### 1.1.1 The Distributive Property

**Formula:** $a(b + c) = ab + ac$

**Explanation:** The distributive property states that when multiplying a number by a sum, you can distribute the multiplication to each term inside the parentheses. This is fundamental to expanding expressions and simplifying calculations.

**Examples:**

*Example 1: Basic distribution*
$$3(x + 4) = 3x + 12$$

*Example 2: With negative terms*
$$-2(x - 5) = -2x + 10$$

*Example 3: Multiple terms*
$$4(2x + 3y - 5) = 8x + 12y - 20$$

### 1.1.2 The Commutative Property

**Formulas:**
- Addition: $a + b = b + a$
- Multiplication: $ab = ba$

**Explanation:** The order in which you add or multiply numbers doesn't change the result. This property is essential for rearranging terms in equations.

**Examples:**
$$7 + 3 = 3 + 7 = 10$$
$$4 \times 5 = 5 \times 4 = 20$$

### 1.1.3 The Associative Property

**Formulas:**
- Addition: $(a + b) + c = a + (b + c)$
- Multiplication: $(ab)c = a(bc)$

**Explanation:** When adding or multiplying three or more numbers, the way you group them doesn't affect the result. This allows us to simplify complex expressions.

**Examples:**
$$(2 + 3) + 4 = 2 + (3 + 4) = 9$$
$$(2 \times 3) \times 4 = 2 \times (3 \times 4) = 24$$

---

## 1.2 Linear Equations

### 1.2.1 Slope-Intercept Form

**Formula:** $y = mx + b$

Where:
- $m$ = slope (rate of change)
- $b$ = y-intercept (where the line crosses the y-axis)

**Explanation:** This form makes it easy to graph linear equations and identify the slope and y-intercept quickly. The slope tells us how steep the line is and the direction it goes.

**Examples:**

*Example 1: Graphing $y = 2x + 3$*
- Slope $m = 2$ (rises 2 units for every 1 unit run)
- Y-intercept $b = 3$ (passes through point (0, 3))

```
    y
    │
  9 │              ●
    │           ●
  6 │        ●
    │     ●
  3 │●─────────────── x
    │
    0              3
```

*Example 2: $y = -\frac{1}{2}x + 4$*
- Slope $m = -\frac{1}{2}$ (falls 1 unit for every 2 units run)
- Y-intercept $b = 4$

### 1.2.2 Point-Slope Form

**Formula:** $y - y_1 = m(x - x_1)$

Where $(x_1, y_1)$ is a known point on the line.

**Explanation:** This form is useful when you know a point on the line and the slope, but not the y-intercept.

**Examples:**

*Given point (2, 3) and slope 4:*
$$y - 3 = 4(x - 2)$$
$$y - 3 = 4x - 8$$
$$y = 4x - 5$$

### 1.2.3 Standard Form

**Formula:** $Ax + By = C$

Where $A$, $B$, and $C$ are integers, and $A \geq 0$.

**Explanation:** This form is useful for finding x and y intercepts easily.

**Examples:**

*Convert $y = \frac{2}{3}x - 4$ to standard form:*
$$y = \frac{2}{3}x - 4$$
$$3y = 2x - 12$$
$$-2x + 3y = -12$$
$$2x - 3y = 12$$

---

## 1.3 Quadratic Equations

### 1.3.1 Standard Form

**Formula:** $ax^2 + bx + c = 0$

Where $a \neq 0$, and $a$, $b$, $c$ are constants.

**Explanation:** A quadratic equation is a second-degree polynomial (highest exponent is 2). The solutions (roots) represent where the parabola crosses the x-axis.

### 1.3.2 The Quadratic Formula

**Formula:** 
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Explanation:** This formula provides the solutions to any quadratic equation $ax^2 + bx + c = 0$. The expression under the square root ($b^2 - 4ac$) is called the **discriminant** and determines the nature of the roots:
- If $b^2 - 4ac > 0$: Two distinct real roots
- If $b^2 - 4ac = 0$: One repeated real root
- If $b^2 - 4ac < 0$: Two complex roots

**Examples:**

*Example 1: Solve $x^2 - 5x + 6 = 0$*
- Here $a = 1$, $b = -5$, $c = 6$
- Discriminant: $(-5)^2 - 4(1)(6) = 25 - 24 = 1$
- $x = \frac{5 \pm \sqrt{1}}{2} = \frac{5 \pm 1}{2}$
- $x = 3$ or $x = 2$

*Example 2: Solve $2x^2 + 4x - 6 = 0$*
- $a = 2$, $b = 4$, $c = -6$
- Discriminant: $4^2 - 4(2)(-6) = 16 + 48 = 64$
- $x = \frac{-4 \pm \sqrt{64}}{4} = \frac{-4 \pm 8}{4}$
- $x = 1$ or $x = -3$

### 1.3.3 Factoring Quadratics

**Formulas:**

1. **Difference of Squares:** $a^2 - b^2 = (a + b)(a - b)$
2. **Perfect Square Trinomials:**
   - $a^2 + 2ab + b^2 = (a + b)^2$
   - $a^2 - 2ab + b^2 = (a - b)^2$
3. **General Trinomial:** $x^2 + (a+b)x + ab = (x + a)(x + b)$

**Examples:**

*Example 1: Factor $x^2 - 9$*
$$x^2 - 9 = (x + 3)(x - 3)$$

*Example 2: Factor $x^2 + 7x + 12$*
Find two numbers that multiply to 12 and add to 7: 3 and 4
$$x^2 + 7x + 12 = (x + 3)(x + 4)$$

*Example 3: Factor $4x^2 - 12x + 9$*
$$4x^2 - 12x + 9 = (2x - 3)^2$$

### 1.3.4 Completing the Square

**Formula:** $x^2 + bx = (x + \frac{b}{2})^2 - (\frac{b}{2})^2$

**Explanation:** This technique transforms a quadratic expression into a perfect square trinomial plus a constant, which is essential for converting to vertex form.

**Examples:**

*Example: Complete the square for $x^2 + 6x + 5 = 0$*
$$x^2 + 6x = -5$$
$$x^2 + 6x + 9 = -5 + 9$$
$$(x + 3)^2 = 4$$
$$x + 3 = \pm 2$$
$$x = -1 \text{ or } x = -5$$

### 1.3.5 Vertex Form

**Formula:** $y = a(x - h)^2 + k$

Where $(h, k)$ is the vertex of the parabola.

**Explanation:** This form reveals the vertex (maximum or minimum point) of the parabola directly.

**Examples:**

*Convert $y = x^2 + 6x + 8$ to vertex form:*
$$y = (x^2 + 6x + 9) + 8 - 9$$
$$y = (x + 3)^2 - 1$$
Vertex at $(-3, -1)$

---

## 1.4 Polynomial Operations

### 1.4.1 Adding and Subtracting Polynomials

**Explanation:** Combine like terms (terms with the same variable and exponent).

**Examples:**

*Example: $(3x^2 + 2x + 1) + (x^2 - 4x + 5)$*
$$= 3x^2 + x^2 + 2x - 4x + 1 + 5$$
$$= 4x^2 - 2x + 6$$

### 1.4.2 Multiplying Polynomials

**Formulas:**

1. **Monomial × Polynomial:** $a(x + y) = ax + ay$
2. **FOIL Method (binomials):** $(a + b)(c + d) = ac + ad + bc + bd$
3. **Special Products:**
   - $(a + b)^2 = a^2 + 2ab + b^2$
   - $(a - b)^2 = a^2 - 2ab + b^2$
   - $(a + b)(a - b) = a^2 - b^2$

**Examples:**

*Example 1: Multiply $(x + 3)(x - 2)$ using FOIL*
$$= x \cdot x + x \cdot (-2) + 3 \cdot x + 3 \cdot (-2)$$
$$= x^2 - 2x + 3x - 6$$
$$= x^2 + x - 6$$

*Example 2: $(2x + 3)^2$*
$$= (2x + 3)(2x + 3)$$
$$= 4x^2 + 6x + 6x + 9$$
$$= 4x^2 + 12x + 9$$

### 1.4.3 Dividing Polynomials

**Long Division:** Similar to long division with numbers.

**Synthetic Division:** A shortcut for dividing by linear factors $(x - c)$.

**Examples:**

*Divide $x^2 + 5x + 6$ by $(x + 2)$:*

Using synthetic division with $c = -2$:
```
-2 |  1   5   6
   |     -2  -6
   --------------
     1   3   0
```

Result: $x + 3$ with remainder 0.

---

## 1.5 Factoring Techniques

### 1.5.1 Greatest Common Factor (GCF)

**Explanation:** Factor out the largest common factor from all terms.

**Examples:**

*Example: Factor $12x^3 + 18x^2 - 24x$*
- GCF = $6x$
- $12x^3 + 18x^2 - 24x = 6x(2x^2 + 3x - 4)$

### 1.5.2 Grouping

**Explanation:** Group terms to reveal common factors.

**Examples:**

*Factor $ax + ay + bx + by$*
$$= a(x + y) + b(x + y)$$
$$= (a + b)(x + y)$$

### 1.5.3 Sum and Difference of Cubes

**Formulas:**
- $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$
- $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$

**Examples:**

*Factor $x^3 + 27$*
$$x^3 + 27 = x^3 + 3^3 = (x + 3)(x^2 - 3x + 9)$$

---

## 1.6 Exponents and Radicals

### 1.6.1 Laws of Exponents

**Formulas:**

| Rule | Formula |
|------|---------|
| Product | $a^m \cdot a^n = a^{m+n}$ |
| Quotient | $\frac{a^m}{a^n} = a^{m-n}$ |
| Power of Power | $(a^m)^n = a^{mn}$ |
| Power of Product | $(ab)^n = a^n b^n$ |
| Power of Quotient | $(\frac{a}{b})^n = \frac{a^n}{b^n}$ |
| Zero Exponent | $a^0 = 1$ (where $a \neq 0$) |
| Negative Exponent | $a^{-n} = \frac{1}{a^n}$ |

**Examples:**

*Example 1: Simplify $x^3 \cdot x^4$*
$$x^{3+4} = x^7$$

*Example 2: Simplify $\frac{x^5}{x^2}$*
$$x^{5-2} = x^3$$

*Example 3: Simplify $(2x^3)^4$*
$$2^4 \cdot x^{3 \cdot 4} = 16x^{12}$$

### 1.6.2 Laws of Radicals

**Formulas:**

| Rule | Formula |
|------|---------|
| Product | $\sqrt{ab} = \sqrt{a} \cdot \sqrt{b}$ |
| Quotient | $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$ |
| Rationalizing | $\frac{1}{\sqrt{a}} = \frac{\sqrt{a}}{a}$ |

**Examples:**

*Example 1: Simplify $\sqrt{50}$*
$$\sqrt{50} = \sqrt{25 \cdot 2} = 5\sqrt{2}$$

*Example 2: Simplify $\frac{3}{\sqrt{12}}$*
$$= \frac{3}{2\sqrt{3}} = \frac{3\sqrt{3}}{2 \cdot 3} = \frac{\sqrt{3}}{2}$$

### 1.6.3 Converting Between Exponents and Radicals

**Formulas:**
- $a^{\frac{m}{n}} = \sqrt[n]{a^m} = (\sqrt[n]{a})^m$
- $\sqrt[n]{a^m} = a^{\frac{m}{n}}$

**Examples:**

*Example 1: Write $x^{\frac{2}{3}}$ as a radical*
$$= \sqrt[3]{x^2} = (\sqrt[3]{x})^2$$

*Example 2: Write $\sqrt{x^5}$ using exponents*
$$= x^{\frac{5}{2}}$$

---

## 1.7 Logarithms

### 1.7.1 Definition of Logarithm

**Formula:** If $b^y = x$, then $\log_b(x) = y$

Where:
- $b$ = base (must be positive and $b \neq 1$)
- $x$ = argument (must be positive)
- $y$ = logarithm

**Examples:**

*Example 1: $\log_2(8) = 3$ because $2^3 = 8$*

*Example 2: $\log_{10}(100) = 2$ because $10^2 = 100$*

*Example 3: $\ln(e) = 1$ (natural log, base $e$)*

### 1.7.2 Laws of Logarithms

**Formulas:**

| Rule | Formula |
|------|---------|
| Product | $\log_b(xy) = \log_b(x) + \log_b(y)$ |
| Quotient | $\log_b(\frac{x}{y}) = \log_b(x) - \log_b(y)$ |
| Power | $\log_b(x^n) = n \cdot \log_b(x)$ |
| Change of Base | $\log_b(x) = \frac{\log_a(x)}{\log_a(b)}$ |

**Examples:**

*Example 1: Expand $\log_2(8x)$*
$$= \log_2(8) + \log_2(x) = 3 + \log_2(x)$$

*Example 2: Condense $\log(x) + \log(5)$*
$$= \log(5x)$$

*Example 3: Evaluate $\log_2(32)$*
$$= \log_2(2^5) = 5 \cdot \log_2(2) = 5$$

### 1.7.3 Solving Logarithmic Equations

**Examples:**

*Solve $\log_2(x + 3) = 4$*
$$x + 3 = 2^4$$
$$x + 3 = 16$$
$$x = 13$$

---

## 1.8 Systems of Equations

### 1.8.1 Substitution Method

**Explanation:** Solve one equation for one variable, then substitute into the other equation.

**Examples:**

*Solve the system:*
$$\begin{cases} y = 2x + 1 \\ x + y = 7 \end{cases}$$

Substitute: $x + (2x + 1) = 7$
$$3x + 1 = 7$$
$$3x = 6$$
$$x = 2$$
Then $y = 2(2) + 1 = 5$
Solution: $(2, 5)$

### 1.8.2 Elimination Method

**Explanation:** Add or subtract equations to eliminate one variable.

**Examples:**

*Solve the system:*
$$\begin{cases} 2x + y = 10 \\ x - y = 2 \end{cases}$$

Add equations: $3x = 12$
$$x = 4$$
Substitute: $4 - y = 2$
$$y = 2$$
Solution: $(4, 2)$

### 1.8.3 Graphical Method

**Explanation:** Find where the lines intersect.

```
    y
    │
  8 │              ● (4, 2)
    │           /
  6 │        /
    │     /
  4 │  /
    │/
  2 │●─────────────── x
    │   \        /
  0 │    \    /
    │     \/
   -2│
    └──────────────
      0   2   4   6
```

---

## 1.9 Inequalities

### 1.9.1 Linear Inequalities

**Formulas:**

| Original Inequality | Solution |
|---------------------|----------|
| $ax + b > c$ | $x > \frac{c-b}{a}$ (if $a > 0$) |
| $ax + b < c$ | $x < \frac{c-b}{a}$ (if $a > 0$) |

**Important:** Reverse the inequality sign when multiplying or dividing by a negative number.

**Examples:**

*Solve $3x - 2 < 7$*
$$3x < 9$$
$$x < 3$$

*Solve $-2x + 4 \geq 10$*
$$-2x \geq 6$$
$$x \leq -3$$ (sign reversed!)

### 1.9.2 Compound Inequalities

**Formulas:**

- AND (intersection): $a < x < b$ means $x > a$ AND $x < b$
- OR (union): $x < a$ or $x > b$ means $x$ is less than $a$ OR greater than $b$

**Examples:**

*Solve $2 < 3x - 1 \leq 8$*
Break into two parts:
$$2 < 3x - 1 \Rightarrow 3 < 3x \Rightarrow x > 1$$
$$3x - 1 \leq 8 \Rightarrow 3x \leq 9 \Rightarrow x \leq 3$$
Combined: $1 < x \leq 3$

### 1.9.3 Quadratic Inequalities

**Examples:**

*Solve $x^2 - 4 > 0$*
Factor: $(x + 2)(x - 2) > 0$

Test intervals:
- $x < -2$: both negative → product positive ✓
- $-2 < x < 2$: one negative → product negative ✗
- $x > 2$: both positive → product positive ✓

Solution: $x < -2$ or $x > 2$

---

## 1.10 Sequences and Series

### 1.10.1 Arithmetic Sequences

**Formula:** $a_n = a_1 + (n-1)d$

Where:
- $a_1$ = first term
- $d$ = common difference
- $n$ = term number

**Examples:**

*Find the 10th term of 2, 5, 8, 11, ...*
- $a_1 = 2$, $d = 3$
- $a_{10} = 2 + 9(3) = 2 + 27 = 29$

### 1.10.2 Geometric Sequences

**Formula:** $a_n = a_1 \cdot r^{n-1}$

Where:
- $a_1$ = first term
- $r$ = common ratio

**Examples:**

*Find the 6th term of 3, 6, 12, 24, ...*
- $a_1 = 3$, $r = 2$
- $a_6 = 3 \cdot 2^{5} = 3 \cdot 32 = 96$

### 1.10.3 Arithmetic Series Sum

**Formula:** $S_n = \frac{n(a_1 + a_n)}{2} = \frac{n(2a_1 + (n-1)d)}{2}$

**Examples:**

*Find the sum of 2 + 5 + 8 + ... + 47*
- First term: 2, last term: 47, number of terms?
- $47 = 2 + (n-1)3 \Rightarrow 45 = 3(n-1) \Rightarrow n = 16$
- $S_{16} = \frac{16(2 + 47)}{2} = \frac{16 \cdot 49}{2} = 392$

### 1.10.4 Geometric Series Sum

**Formula:** $S_n = a_1 \frac{1 - r^n}{1 - r}$ (for $r \neq 1$)

**Examples:**

*Find the sum of 3 + 6 + 12 + 24 + ... + 384*
- $a_1 = 3$, $r = 2$, $a_n = 384$
- $384 = 3 \cdot 2^{n-1} \Rightarrow 128 = 2^{n-1} \Rightarrow n-1 = 7 \Rightarrow n = 8$
- $S_8 = 3 \frac{1 - 2^8}{1-2} = 3 \frac{1 - 256}{-1} = 3(255) = 765$

---

# Part 2: Calculus

## 2.1 Limits

### 2.1.1 Definition of a Limit

**Formula:** $\lim_{x \to a} f(x) = L$

This means as $x$ approaches $a$, $f(x)$ approaches $L$.

**Properties:**

If $\lim_{x \to a} f(x) = L$ and $\lim_{x \to a} g(x) = M$, then:
- $\lim_{x \to a} [f(x) + g(x)] = L + M$
- $\lim_{x \to a} [f(x) - g(x)] = L - M$
- $\lim_{x \to a} [f(x) \cdot g(x)] = L \cdot M$
- $\lim_{x \to a} [\frac{f(x)}{g(x)}] = \frac{L}{M}$ (if $M \neq 0$)

### 2.1.2 Limit Laws

**Basic Limits:**
- $\lim_{x \to a} c = c$ (constant)
- $\lim_{x \to a} x = a$
- $\lim_{x \to 0} \frac{\sin x}{x} = 1$
- $\lim_{x \to \infty} \frac{1}{x} = 0$

**Examples:**

*Example 1: $\lim_{x \to 3} (2x^2 - 5x + 1)$*
$$= 2(3)^2 - 5(3) + 1 = 18 - 15 + 1 = 4$$

*Example 2: $\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$*
Factor the numerator: $\frac{(x+2)(x-2)}{x-2} = x + 2$
$$\lim_{x \to 2} (x + 2) = 4$$

*Example 3: $\lim_{x \to 0} \frac{\sin(3x)}{x}$*
Using $\lim_{x \to 0} \frac{\sin x}{x} = 1$:
$$\lim_{x \to 0} \frac{\sin(3x)}{x} = \lim_{x \to 0} \frac{3\sin(3x)}{3x} = 3 \cdot 1 = 3$$

### 2.1.3 One-Sided Limits

**Formulas:**
- Left-hand limit: $\lim_{x \to a^-} f(x) = L$
- Right-hand limit: $\lim_{x \to a^+} f(x) = L$

**Examples:**

*Evaluate $\lim_{x \to 0} \frac{|x|}{x}$*
- As $x \to 0^+$: $\frac{x}{x} = 1$
- As $x \to 0^-$: $\frac{-x}{x} = -1$
- Since one-sided limits differ, the limit does not exist.

---

## 2.2 Derivatives

### 2.2.1 Definition of the Derivative

**Formula:** $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$

The derivative represents:
- Instantaneous rate of change
- Slope of the tangent line
- Velocity (in physics)

### 2.2.2 Basic Derivative Rules

| Function | Derivative |
|----------|------------|
| $c$ (constant) | $0$ |
| $x^n$ | $nx^{n-1}$ |
| $cf(x)$ | $cf'(x)$ |
| $f(x) + g(x)$ | $f'(x) + g'(x)$ |
| $f(x) - g(x)$ | $f'(x) - g'(x)$ |
| $f(x) \cdot g(x)$ | $f'g + fg'$ |
| $\frac{f(x)}{g(x)}$ | $\frac{f'g - fg'}{g^2}$ |

### 2.2.3 Chain Rule

**Formula:** If $y = f(g(x))$, then $\frac{dy}{dx} = f'(g(x)) \cdot g'(x)$

**Alternative notation:** $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$

**Examples:**

*Example 1: Find the derivative of $f(x) = (3x^2 + 1)^5$*
- Let $u = 3x^2 + 1$, then $y = u^5$
- $\frac{dy}{du} = 5u^4$, $\frac{du}{dx} = 6x$
- $f'(x) = 5(3x^2 + 1)^4 \cdot 6x = 30x(3x^2 + 1)^4$

*Example 2: Find the derivative of $f(x) = \sqrt{2x^3 + 4}$*
$$= (2x^3 + 4)^{\frac{1}{2}}$$
$$f'(x) = \frac{1}{2}(2x^3 + 4)^{-\frac{1}{2}} \cdot 6x^2 = \frac{3x^2}{\sqrt{2x^3 + 4}}$$

### 2.2.4 Derivatives of Trigonometric Functions

| Function | Derivative |
|----------|------------|
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\csc x$ | $-\csc x \cot x$ |
| $\sec x$ | $\sec x \tan x$ |
| $\cot x$ | $-\csc^2 x$ |

**Examples:**

*Example: $f(x) = \sin x + \cos x$*
$$f'(x) = \cos x - \sin x$$

### 2.2.5 Derivatives of Exponential and Logarithmic Functions

| Function | Derivative |
|----------|------------|
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\log_a x$ | $\frac{1}{x \ln a}$ |

**Examples:**

*Example 1: $f(x) = e^{3x}$*
$$f'(x) = e^{3x} \cdot 3 = 3e^{3x}$$

*Example 2: $f(x) = \ln(2x^2 + 1)$*
$$f'(x) = \frac{1}{2x^2 + 1} \cdot 4x = \frac{4x}{2x^2 + 1}$$

### 2.2.6 Product Rule

**Formula:** $(fg)' = f'g + fg'$

**Visual Representation:**
```
    f'g + fg'
    ↗      ↖
   f  ·  g
```

**Examples:**

*Find the derivative of $f(x) = x^2 \sin x$*
- $f(x) = x^2$, $g(x) = \sin x$
- $f'(x) = 2x$, $g'(x) = \cos x$
- $f'(x) = 2x \sin x + x^2 \cos x$

### 2.2.7 Quotient Rule

**Formula:** $(\frac{f}{g})' = \frac{f'g - fg'}{g^2}$

**Memory Aid:** "Low d-high minus high d-low, over low squared"

**Examples:**

*Find the derivative of $f(x) = \frac{x^2 + 1}{x - 3}$*
- $f'(x) = \frac{(2x)(x-3) - (x^2+1)(1)}{(x-3)^2}$
- $= \frac{2x^2 - 6x - x^2 - 1}{(x-3)^2}$
- $= \frac{x^2 - 6x - 1}{(x-3)^2}$

### 2.2.8 Implicit Differentiation

**Explanation:** Used when $y$ is not explicitly solved for $x$.

**Procedure:**
1. Differentiate both sides with respect to $x$
2. Treat $y$ as a function of $x$: $\frac{d}{dx}[y] = y'$
3. Solve for $y'$

**Examples:**

*Find $y'$ for $x^2 + y^2 = 25$*
Differentiate:
$$2x + 2yy' = 0$$
$$2yy' = -2x$$
$$y' = -\frac{x}{y}$$

### 2.2.9 Higher Order Derivatives

**Formula:**
- Second derivative: $f''(x) = \frac{d^2y}{dx^2}$
- Third derivative: $f'''(x)$

**Examples:**

*Find the second derivative of $f(x) = 3x^4 - 2x^2 + 5$*
- $f'(x) = 12x^3 - 4x$
- $f''(x) = 36x^2 - 4$

---

## 2.3 Applications of Derivatives

### 2.3.1 Related Rates

**Procedure:**
1. Identify what is changing and at what rate
2. Write an equation relating the variables
3. Differentiate implicitly with respect to time
4. Substitute known values and solve

**Examples:**

*A ladder 10 feet long slides down a wall. If the bottom is sliding away at 2 ft/s, how fast is the top sliding down when the bottom is 6 feet from the wall?*

Let $x$ = distance from wall to bottom of ladder
Let $y$ = distance from ground to top of ladder

Given: $\frac{dx}{dt} = 2$ ft/s, find $\frac{dy}{dt}$ when $x = 6$

Equation: $x^2 + y^2 = 10^2$
Differentiate:
$$2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$$
When $x = 6$: $36 + y^2 = 100 \Rightarrow y = 8$
$$2(6)(2) + 2(8)\frac{dy}{dt} = 0$$
$$24 + 16\frac{dy}{dt} = 0$$
$$\frac{dy}{dt} = -\frac{24}{16} = -1.5 \text{ ft/s}$$

The top is sliding down at 1.5 ft/s.

### 2.3.2 Optimization

**Procedure:**
1. Identify the quantity to optimize
2. Write a function for this quantity
3. Find the domain
4. Find critical points ($f'(x) = 0$ or undefined)
5. Use first/second derivative test to find extrema
6. Check endpoints

**Examples:**

*Find the rectangle of maximum area with perimeter 100 cm.*

Let $x$ = length, $y$ = width
Perimeter: $2x + 2y = 100 \Rightarrow y = 50 - x$
Area: $A = xy = x(50 - x) = 50x - x^2$

Find critical points:
$$A' = 50 - 2x = 0 \Rightarrow x = 25$$

Check second derivative: $A'' = -2 < 0$ (maximum)

Then $y = 50 - 25 = 25$

Maximum area: $25 \times 25 = 625 \text{ cm}^2$

### 2.3.3 Motion Along a Line

**Formulas:**
- Position: $s(t)$
- Velocity: $v(t) = s'(t)$
- Acceleration: $a(t) = s''(t)$

**Examples:**

*A particle's position is given by $s(t) = t^3 - 6t^2 + 9t$. Find velocity and acceleration at $t = 2$.*

Velocity: $v(t) = 3t^2 - 12t + 9$
$$v(2) = 3(4) - 12(2) + 9 = 12 - 24 + 9 = -3$$

Acceleration: $a(t) = 6t - 12$
$$a(2) = 12 - 12 = 0$$

---

## 2.4 Integrals

### 2.4.1 Definition of the Integral

**Formulas:**

- **Indefinite Integral (Antiderivative):** $\int f(x) dx = F(x) + C$
- **Definite Integral:** $\int_a^b f(x) dx = F(b) - F(a)$

Where $F'(x) = f(x)$ and $C$ is the constant of integration.

### 2.4.2 Basic Integration Rules

| Function | Integral |
|----------|----------|
| $x^n$ | $\frac{x^{n+1}}{n+1} + C$ ($n \neq -1$) |
| $\frac{1}{x}$ | $\ln|x| + C$ |
| $e^x$ | $e^x + C$ |
| $a^x$ | $\frac{a^x}{\ln a} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sec^2 x$ | $\tan x + C$ |

### 2.4.3 Integration Rules

**Constant Multiple Rule:**
$$\int cf(x) dx = c \int f(x) dx$$

**Sum/Difference Rule:**
$$\int [f(x) \pm g(x)] dx = \int f(x) dx \pm \int g(x) dx$$

**Power Rule:**
$$\int x^n dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)$$

**Examples:**

*Example 1: $\int 3x^2 dx$*
$$= 3 \cdot \frac{x^3}{3} = x^2 + C$$

*Example 2: $\int (2x^3 - 5x + 7) dx$*
$$= \frac{2x^4}{4} - \frac{5x^2}{2} + 7x + C$$
$$= \frac{x^4}{2} - \frac{5x^2}{2} + 7x + C$$

### 2.4.4 u-Substitution (Reverse Chain Rule)

**Formula:** If $u = g(x)$, then $\int f(g(x)) \cdot g'(x) dx = \int f(u) du$

**Procedure:**
1. Identify the "inner" function
2. Let $u$ = inner function
3. Find $du$
4. Substitute and integrate
5. Substitute back

**Examples:**

*Example 1: $\int 2x(x^2 + 1)^3 dx$*
Let $u = x^2 + 1$, then $du = 2x dx$
$$= \int u^3 du = \frac{u^4}{4} + C = \frac{(x^2 + 1)^4}{4} + C$$

*Example 2: $\int \sin(3x) dx$*
Let $u = 3x$, then $du = 3 dx$, so $dx = \frac{du}{3}$
$$= \int \sin(u) \cdot \frac{du}{3} = -\frac{1}{3}\cos(u) + C = -\frac{1}{3}\cos(3x) + C$$

### 2.4.5 Integration by Parts

**Formula:** $\int u dv = uv - \int v du$

**LIATE Rule:** Choose $u$ in this order:
- L: Logarithmic
- I: Inverse trigonometric
- A: Algebraic
- T: Trigonometric
- E: Exponential

**Examples:**

*Example: $\int x e^x dx$*
Choose: $u = x$, $dv = e^x dx$
Then: $du = dx$, $v = e^x$

$$\int x e^x dx = x e^x - \int e^x dx = x e^x - e^x + C = e^x(x - 1) + C$$

### 2.4.6 Definite Integrals

**Formula:** $\int_a^b f(x) dx = F(b) - F(a)$

**Fundamental Theorem of Calculus:**
If $F(x) = \int_a^x f(t) dt$, then $F'(x) = f(x)$

**Examples:**

*Example: $\int_0^2 (x^2 + 1) dx$*
Find antiderivative: $\frac{x^3}{3} + x$
Evaluate at bounds:
$$= [\frac{2^3}{3} + 2] - [\frac{0^3}{3} + 0] = \frac{8}{3} + 2 = \frac{14}{3}$$

---

## 2.5 Applications of Integration

### 2.5.1 Area Under a Curve

**Formula:** Area from $a$ to $b$ = $\int_a^b f(x) dx$ (where $f(x) \geq 0$)

**Examples:**

*Find the area under $y = x^2$ from $x = 0$ to $x = 2$*

```
    y
    │
  4 │       ┌───────────
    │       │███████████
  3 │       │███████████
    │       │███████████
  2 │       │███████████
    │       │███████████
  1 │███████│███████████
    │███████│███████████
  0 │███████│───────────●── x
    └─────────────────────
      0   1   2   3   4
```

$$\int_0^2 x^2 dx = [\frac{x^3}{3}]_0^2 = \frac{8}{3}$$

### 2.5.2 Area Between Curves

**Formula:** Area = $\int_a^b [f(x) - g(x)] dx$ (where $f(x) \geq g(x)$)

**Examples:**

*Find the area between $y = x$ and $y = x^2$*

```
    y
    │
  1 │     ╱───────● (1,1)
    │   ╱     ╱
  0.5│  ●─────
    │ ╱   ╱
  0 │╱   ╱
    └───────────────── x
      0   0.5  1   1.5
```

Find intersection: $x = x^2 \Rightarrow x = 0$ or $x = 1$

Area = $\int_0^1 (x - x^2) dx$
$$= [\frac{x^2}{2} - \frac{x^3}{3}]_0^1 = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$$

### 2.5.3 Volume of Solids of Revolution

**Disk Method:**
$$V = \pi \int_a^b [f(x)]^2 dx$$

**Washer Method:**
$$V = \pi \int_a^b ([f(x)]^2 - [g(x)]^2) dx$$

**Examples:**

*Find the volume of the solid obtained by rotating $y = \sqrt{x}$ from $x = 0$ to $x = 4$ about the x-axis.*

$$V = \pi \int_0^4 (\sqrt{x})^2 dx = \pi \int_0^4 x dx = \pi [\frac{x^2}{2}]_0^4 = \pi \cdot 8 = 8\pi$$

### 2.5.4 Average Value of a Function

**Formula:** $f_{avg} = \frac{1}{b-a} \int_a^b f(x) dx$

**Examples:**

*Find the average value of $f(x) = x^2$ on [0, 3]*

$$f_{avg} = \frac{1}{3-0} \int_0^3 x^2 dx = \frac{1}{3} [\frac{x^3}{3}]_0^3 = \frac{1}{3} \cdot 9 = 3$$

---

## 2.6 Advanced Calculus Topics

### 2.6.1 L'Hôpital's Rule

**Formula:** If $\lim_{x \to a} \frac{f(x)}{g(x)}$ gives $\frac{0}{0}$ or $\frac{\infty}{\infty}$, then:
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

**Examples:**

*Example: $\lim_{x \to 0} \frac{\sin x}{x}$*
$$= \lim_{x \to 0} \frac{\cos x}{1} = 1$$

*Example: $\lim_{x \to \infty} \frac{x^2}{e^x}$*
$$= \lim_{x \to \infty} \frac{2x}{e^x} = \lim_{x \to \infty} \frac{2}{e^x} = 0$$

### 2.6.2 Taylor Series

**Formula:** $f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots$

**Examples:**

*The Taylor series for $e^x$ at $x = 0$:*
$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$

### 2.6.3 Partial Derivatives

For $z = f(x, y)$:
- $\frac{\partial z}{\partial x}$ = treat $y$ as constant, differentiate with respect to $x$
- $\frac{\partial z}{\partial y}$ = treat $x$ as constant, differentiate with respect to $y$

**Examples:**

*Find $\frac{\partial z}{\partial x}$ and $\frac{\partial z}{\partial y}$ for $z = x^2y + 3xy^2$*

$$\frac{\partial z}{\partial x} = 2xy + 3y^2$$
$$\frac{\partial z}{\partial y} = x^2 + 6xy$$

### 2.6.4 Multiple Integrals

**Double Integral:** $\iint_R f(x, y) dA$

**Examples:**

*Evaluate $\int_0^1 \int_0^2 xy \, dy \, dx$*

$$\int_0^1 [\int_0^2 xy \, dy] dx = \int_0^1 [x \cdot \frac{y^2}{2}]_0^2 dx = \int_0^1 \frac{x \cdot 4}{2} dx = \int_0^1 2x dx = [x^2]_0^1 = 1$$

---

# Part 3: Integration of Algebra and Calculus

## 3.1 How Algebra and Calculus Connect

Algebra and calculus are deeply interconnected disciplines. Algebra provides the foundational tools (equations, functions, expressions) that calculus manipulates through differentiation and integration. Understanding this connection is essential for solving complex problems in physics, engineering, economics, and data science.

### Key Connections:

| Algebra Concept | Calculus Application |
|----------------|---------------------|
| Functions | Domain, range, and continuous behavior |
| Equations | Solving for critical points |
| Factoring | Simplifying integrands |
| Graphing | Understanding behavior of derivatives |
| Exponents/Logarithms | Exponential growth/decay models |
| Trigonometry | Wave motion and periodic phenomena |

---

## 3.2 Problem-Solving Approaches

### 3.2.1 Finding Maximum and Minimum Values

**Algebraic Approach (Completing the Square):**

Find the maximum value of $f(x) = -2x^2 + 8x + 3$

1. Factor out the coefficient of $x^2$:
$$f(x) = -2(x^2 - 4x) + 3$$

2. Complete the square:
$$f(x) = -2[(x^2 - 4x + 4) - 4] + 3$$
$$f(x) = -2[(x - 2)^2 - 4] + 3$$
$$f(x) = -2(x - 2)^2 + 8 + 3$$
$$f(x) = -2(x - 2)^2 + 11$$

Maximum value = 11 (at $x = 2$)

**Calculus Approach (Derivative):**

Find where $f(x) = -2x^2 + 8x + 3$ has its maximum:

1. Find the derivative:
$$f'(x) = -4x + 8$$

2. Set derivative equal to zero:
$$-4x + 8 = 0$$
$$x = 2$$

3. Verify it's a maximum (second derivative test):
$$f''(x) = -4 < 0$$ (negative, so maximum)

Maximum value = $f(2) = -2(4) + 8(2) + 3 = -8 + 16 + 3 = 11$

```
    y
    │
 11 │────────────●── Maximum at (2, 11)
    │         ╱   
  8 │       ╱     
    │     ╱      
  5 │   ╱        
    │ ╱         
  3 │●─────────────── x
    │   2   4
```

---

### 3.2.2 Area and Distance Problems

**Problem:** A car accelerates from rest at a constant rate of $3 \, m/s^2$. Find:
1. The velocity after 5 seconds
2. The distance traveled in 5 seconds

**Solution:**

*Using calculus (integration):*

The acceleration is constant: $a(t) = 3 \, m/s^2$

1. Velocity (integral of acceleration):
$$v(t) = \int 3 \, dt = 3t + C$$
Since the car starts from rest, $v(0) = 0$, so $C = 0$
$$v(t) = 3t$$

At $t = 5$: $v(5) = 3(5) = 15 \, m/s$

2. Distance (integral of velocity):
$$s(t) = \int 3t \, dt = \frac{3t^2}{2} + C$$
Since $s(0) = 0$, so $C = 0$
$$s(t) = \frac{3t^2}{2}$$

At $t = 5$: $s(5) = \frac{3(25)}{2} = \frac{75}{2} = 37.5 \, m$

*Using algebra (kinematic equations):*

For constant acceleration:
- $v = v_0 + at = 0 + 3(5) = 15 \, m/s$ ✓
- $s = v_0 t + \frac{1}{2}at^2 = 0 + \frac{1}{2}(3)(25) = 37.5 \, m$ ✓

---

### 3.2.3 Optimization in Economics

**Problem:** A company produces $x$ thousand units of a product. The revenue function is $R(x) = 50x - 5x^2$ and the cost function is $C(x) = 20x + 100$. Find the production level that maximizes profit.

**Solution:**

*Step 1: Define the profit function*
$$P(x) = R(x) - C(x) = (50x - 5x^2) - (20x + 100)$$
$$P(x) = 30x - 5x^2 - 100$$

*Step 2: Use calculus to find the maximum*

Find derivative:
$$P'(x) = 30 - 10x$$

Set equal to zero:
$$30 - 10x = 0$$
$$x = 3$$

Second derivative: $P''(x) = -10 < 0$ (maximum)

*Step 3: Interpret the result*
- Production level: $x = 3$ thousand units = 3,000 units
- Maximum profit: $P(3) = 30(3) - 5(9) - 100 = 90 - 45 - 100 = -55$ (This indicates a loss!)

This suggests the model needs adjustment, or the company is operating at a loss at this production level.

```
    Profit
      ↑
      │     ╱
      │   ╱   Maximum at x = 3
      │ ╱
   -55●─────────────────────→ x
      │      3
```

---

### 3.2.4 Related Rates in Physics

**Problem:** A spherical balloon is being inflated at a rate of $100 \, cm^3/s$. How fast is the radius changing when the radius is 5 cm?

**Solution:**

*Step 1: Set up the equation*
For a sphere: $V = \frac{4}{3}\pi r^3$

*Step 2: Differentiate with respect to time*
$$\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}$$

*Step 3: Substitute known values*
Given: $\frac{dV}{dt} = 100 \, cm^3/s$, $r = 5 \, cm$
$$100 = 4\pi(25) \frac{dr}{dt}$$
$$100 = 100\pi \frac{dr}{dt}$$
$$\frac{dr}{dt} = \frac{1}{\pi} \, cm/s \approx 0.318 \, cm/s$$

*Algebraic verification:*
The balloon's volume increases at $100 \, cm^3/s$. The surface area of the sphere is $4\pi r^2 = 100\pi \, cm^2$ at $r = 5$. Since $\frac{dV}{dt} = \text{surface area} \times \frac{dr}{dt}$, we get the same result.

---

### 3.2.5 Exponential Growth and Decay

**Problem:** A population of bacteria doubles every 3 hours. Initially there are 100 bacteria. Find:
1. The population after 9 hours
2. The rate of growth at 9 hours

**Solution (Using Calculus):**

*Step 1: Set up the differential equation*
$$\frac{dP}{dt} = kP$$

*Step 2: Solve using separation of variables*
$$\frac{dP}{P} = k \, dt$$
$$\ln|P| = kt + C$$

Since $P > 0$: $\ln P = kt + C$
$$P = e^{kt + C} = e^{Ct} e^{kt}$$

Let $P_0 = e^C$ (initial population):
$$P(t) = P_0 e^{kt}$$

*Step 3: Find k using the doubling time*
When $t = 3$, $P(3) = 2P_0$:
$$2P_0 = P_0 e^{3k}$$
$$2 = e^{3k}$$
$$\ln 2 = 3k$$
$$k = \frac{\ln 2}{3} \approx 0.231$$

*Step 4: Find the population after 9 hours*
$$P(9) = 100 \cdot e^{9 \cdot \frac{\ln 2}{3}} = 100 \cdot e^{3\ln 2} = 100 \cdot 2^3 = 800$$

*Step 5: Find the rate of growth at t = 9*
$$P'(t) = kP_0 e^{kt} = kP(t)$$
$$P'(9) = \frac{\ln 2}{3} \cdot 800 \approx 0.231 \cdot 800 \approx 185 \text{ bacteria/hour}$$

```
    Population
      ↑
  800│                    ●
    │                  ╱
  600│                ╱
    │              ╱
  400│          ╱●
    │       ╱
  200│   ╱●
    │╱
    └───────────────────→ t (hours)
      0   3   6   9   12
```

---

### 3.2.6 Area Between Curves with Technology

**Problem:** Find the area enclosed by the curves $y = x^2$ and $y = \sqrt{x}$.

**Solution:**

*Step 1: Find intersection points*
$$x^2 = \sqrt{x}$$
Square both sides: $x^4 = x$
$$x^4 - x = 0$$
$$x(x^3 - 1) = 0$$
$$x(x - 1)(x^2 + x + 1) = 0$$
Real solutions: $x = 0$, $x = 1$

*Step 2: Determine which function is on top*
For $0 < x < 1$:
- At $x = 0.25$: $x^2 = 0.0625$, $\sqrt{x} = 0.5$
- $\sqrt{x} > x^2$

So $\sqrt{x}$ is on top.

*Step 3: Set up and evaluate the integral*
$$A = \int_0^1 (\sqrt{x} - x^2) \, dx$$
$$= \int_0^1 (x^{1/2} - x^2) \, dx$$
$$= [\frac{x^{3/2}}{3/2} - \frac{x^3}{3}]_0^1$$
$$= [\frac{2}{3}x^{3/2} - \frac{x^3}{3}]_0^1$$
$$= \frac{2}{3}(1) - \frac{1}{3}(1) - 0$$
$$= \frac{1}{3}$$

```
    y
    │
  1 │  ●───────────── y = √x
    │ ╱██████████████
  0.5│╱████████████
    │╱██████████
  0.25│   ████████
    │     ████
  0 │●───────────●─── y = x²
    └───────────────── x
      0   0.5  1   1.5
```

---

### 3.2.7 Volume of Complex Solids

**Problem:** Find the volume of the solid obtained by rotating the region bounded by $y = x$ and $y = x^2$ about the line $y = 1$.

**Solution:**

*Step 1: Find intersection points*
$$x = x^2$$
$$x^2 - x = 0$$
$$x(x - 1) = 0$$
$x = 0$ or $x = 1$

*Step 2: Determine the radii*
- Outer radius: distance from $y = 1$ to $y = x^2$: $R = 1 - x^2$
- Inner radius: distance from $y = 1$ to $y = x$: $r = 1 - x$

*Step 3: Set up and evaluate using washer method*
$$V = \pi \int_0^1 [(1 - x^2)^2 - (1 - x)^2] \, dx$$
$$= \pi \int_0^1 [(1 - 2x^2 + x^4) - (1 - 2x + x^2)] \, dx$$
$$= \pi \int_0^1 (1 - 2x^2 + x^4 - 1 + 2x - x^2) \, dx$$
$$= \pi \int_0^1 (2x - 3x^2 + x^4) \, dx$$
$$= \pi [x^2 - x^3 + \frac{x^5}{5}]_0^1$$
$$= \pi [(1 - 1 + \frac{1}{5}) - 0]$$
$$= \frac{\pi}{5}$$

```
    y=1 ═════════════════
       │  Outer radius
       │     ←─────→
       │  ┌──────────┐
       │  │  ■■■■■■  │
       │  │ ■■■■■■■■■ │
       │  │■■■■■■■■■■ │
       │  └──────────┘
       │     ←─────→
       │  Inner radius
    y=x│●─────────────
       │  ╲
    y=x²│   ╲●
```

---

### 3.2.8 Kinematics with Variable Acceleration

**Problem:** A car's acceleration is given by $a(t) = 2t + 1$ (in m/s²). If the car starts from rest at $t = 0$, find:
1. The velocity at time $t$
2. The position at time $t$
3. The distance traveled in the first 4 seconds

**Solution:**

*Step 1: Find velocity (integrate acceleration)*
$$v(t) = \int (2t + 1) \, dt = t^2 + t + C$$
Since $v(0) = 0$, $C = 0$
$$v(t) = t^2 + t$$

*Step 2: Find position (integrate velocity)*
$$s(t) = \int (t^2 + t) \, dt = \frac{t^3}{3} + \frac{t^2}{2} + C$$
Since $s(0) = 0$, $C = 0$
$$s(t) = \frac{t^3}{3} + \frac{t^2}{2}$$

*Step 3: Find distance in first 4 seconds*
$$s(4) = \frac{4^3}{3} + \frac{4^2}{2} = \frac{64}{3} + \frac{16}{2} = \frac{64}{3} + 8 = \frac{64 + 24}{3} = \frac{88}{3} \approx 29.3 \, m$$

*Verification using algebraic kinematics:*
For variable acceleration, we must use calculus. The kinematic equations $v = v_0 + at$ and $s = v_0 t + \frac{1}{2}at^2$ only work for constant acceleration.

```
    Velocity (m/s)
      ↑
  20 │                  ● v(4) = 20
    │               ╱
  15 │            ╱
    │         ╱
  10 │      ╱
    │   ╱
  5 │╱
    │●──────────────────→ t (s)
    └   1   2   3   4
```

---

## 3.3 Summary: When to Use Each Approach

| Problem Type | Algebra Approach | Calculus Approach |
|-------------|------------------|-------------------|
| Finding max/min of quadratic | Complete the square | Derivative = 0 |
| Area under curve | Not applicable | Definite integral |
| Rate problems | Proportional reasoning | Related rates |
| Growth/decay | Discrete doubling | Continuous exponential |
| Volume | Basic geometry formulas | Integration methods |
| Motion with constant acceleration | Kinematic equations | Integration of acceleration |

---

## 3.4 Practice Problems

### Problem 1: Optimization
Find the rectangle of maximum area that can be inscribed in a semicircle of radius 10.

### Problem 2: Related Rates
A conical tank (with vertex down) is being filled with water at 2 cubic feet per minute. If the height is 10 feet and the radius at the top is 5 feet, how fast is the water level rising when the water is 6 feet deep?

### Problem 3: Area Between Curves
Find the area of the region enclosed by $y = x^3$ and $y = x$.

### Problem 4: Volume of Revolution
Find the volume of the solid obtained by rotating the region bounded by $y = e^x$, $x = 0$, $x = 1$, and the x-axis about the x-axis.

### Problem 5: Exponential Decay
A radioactive substance has a half-life of 5730 years (carbon-14). If you have 100 grams today, how much will remain after 10,000 years?

---

## 3.5 Answers to Practice Problems

### Problem 1: Optimization
**Solution:** Let the rectangle have width $2x$ and height $y$.
Using the equation of the semicircle: $x^2 + y^2 = 10^2$
Area: $A = 2xy = 2x\sqrt{100 - x^2}$
$dA/dx = 2\sqrt{100 - x^2} + 2x \cdot \frac{-x}{\sqrt{100 - x^2}} = 0$
Solving: $x = \frac{10}{\sqrt{2}} = 5\sqrt{2}$
Maximum area: $A = 2(5\sqrt{2})(5\sqrt{2}) = 100$ square units

### Problem 2: Related Rates
**Solution:**
Volume of cone: $V = \frac{1}{3}\pi r^2 h$
Similar triangles: $\frac{r}{h} = \frac{5}{10} = \frac{1}{2}$, so $r = \frac{h}{2}$
$V = \frac{1}{3}\pi (\frac{h}{2})^2 h = \frac{\pi h^3}{12}$
Differentiate: $\frac{dV}{dt} = \frac{\pi h^2}{4} \frac{dh}{dt}$
Given $\frac{dV}{dt} = 2$, $h = 6$:
$2 = \frac{\pi(36)}{4} \frac{dh}{dt}$
$\frac{dh}{dt} = \frac{8}{9\pi} \approx 0.28$ ft/min

### Problem 3: Area Between Curves
**Solution:**
Find intersections: $x^3 = x \Rightarrow x(x^2 - 1) = 0$
$x = -1, 0, 1$
$A = \int_{-1}^0 (x - x^3) dx + \int_0^1 (x^3 - x) dx$
$= [\frac{x^2}{2} - \frac{x^4}{4}]_{-1}^0 + [\frac{x^4}{4} - \frac{x^2}{2}]_0^1$
$= (0 - (0.5 - 0.25)) + ((0.25 - 0.5) - 0)$
$= 0.25 + (-0.25) = 0$ Wait, let me recalculate:
$= [0 - (-0.5 + 0.25)] + [(0.25 - 0.5) - 0]$
$= 0.25 + (-0.25) = 0$ 

Actually:
$\int_{-1}^0 (x - x^3) dx = [\frac{x^2}{2} - \frac{x^4}{4}]_{-1}^0 = 0 - (\frac{1}{2} - \frac{1}{4}) = -\frac{1}{4}$
$\int_0^1 (x^3 - x) dx = [\frac{x^4}{4} - \frac{x^2}{2}]_0^1 = \frac{1}{4} - \frac{1}{2} = -\frac{1}{4}$

Total area = $|-\frac{1}{4}| + |-\frac{1}{4}| = \frac{1}{2}$

### Problem 4: Volume of Revolution
**Solution:**
$V = \pi \int_0^1 (e^x)^2 dx = \pi \int_0^1 e^{2x} dx$
$= \pi [\frac{e^{2x}}{2}]_0^1 = \pi(\frac{e^2 - 1}{2})$

### Problem 5: Exponential Decay
**Solution:**
$N(t) = N_0 e^{-kt}$
Given half-life = 5730 years: $N(5730) = \frac{1}{2}N_0$
$\frac{1}{2} = e^{-5730k}$
$\ln(0.5) = -5730k$
$k = \frac{\ln 2}{5730} \approx 0.0001209$

At $t = 10000$:
$N(10000) = 100 \cdot e^{-10000 \cdot \frac{\ln 2}{5730}}$
$= 100 \cdot e^{-1.745}$
$= 100 \cdot 0.1746 = 17.46$ grams

---

# Conclusion

Algebra and calculus are complementary branches of mathematics that together provide powerful tools for solving real-world problems. Algebra provides the foundational language of functions, equations, and relationships, while calculus extends these concepts to analyze rates of change, optimization, and accumulation.

**Key Takeaways:**

1. **Algebra** gives us the ability to:
   - Represent relationships between quantities
   - Solve equations and find roots
   - Factor and simplify expressions
   - Model discrete phenomena

2. **Calculus** extends our capabilities to:
   - Analyze continuous change
   - Find instantaneous rates of change
   - Calculate areas and volumes of complex shapes
   - Solve optimization problems
   - Model continuous growth and decay

3. **Together**, they enable us to:
   - Solve complex physics problems
   - Optimize business and engineering processes
   - Model population dynamics
   - Analyze financial markets
   - Understand machine learning algorithms

The integration of algebraic and calculus techniques is essential for advanced studies in science, technology, engineering, mathematics (STEM) fields, and is fundamental to modern artificial intelligence and data science applications.

*Related Notes:*
- [[05-AI-Research/AI Fundamentals]]
- [[03-Resources/Knowledge Management System]]
- [[07-Cybersecurity/Cryptography Math]]
- [[09-Knowledge/Mathematical Foundations of CS]]
