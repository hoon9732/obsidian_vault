When we work with complex numbers we can describe each number in **two equivalent ways**, depending on which pieces of information we want to emphasize:

|                                  | What you write                                                              | What the symbols mean                                                                                                                                                                                  | How to recover one form from the other                                                                                            |
| -------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| **Rectangular (Cartesian) form** | $z = x + j\,y$                                                              | • $x$: real (horizontal) component<br>• $y$: imaginary (vertical) component                                                                                                                            | $\lvert z\rvert = \sqrt{x^{2}+y^{2}}$<br>$\theta = \tan^{-1}\!\bigl(\tfrac{y}{x}\bigr)$ (use `atan2` to get the correct quadrant) |
| **Polar (exponential) form**     | $z = \lvert z\rvert e^{j\theta} = \lvert z\rvert(\cos\theta + j\sin\theta)$ | • $\lvert z\rvert$ (often written $r$): the **magnitude** or distance of $z$ from the origin<br>• $\theta$: the **angle** (or *argument/phase*) measured counter-clockwise from the positive real axis | $x = \lvert z\rvert\cos\theta$<br>$y = \lvert z\rvert\sin\theta$                                                                  |

### Why the two forms are useful

* **Rectangular form** is convenient when you need to **add or subtract** complex numbers because you simply add/subtract corresponding real and imaginary parts:

  $$
  (x_1 + j y_1) \;+\; (x_2 + j y_2) \;=\; (x_1 + x_2) \;+\; j(y_1 + y_2).
  $$

* **Polar form** is ideal for **multiplication, division, and exponentiation** because magnitudes and phases separate cleanly:

  $$
  (\lvert z_1\rvert e^{j\theta_1})(\lvert z_2\rvert e^{j\theta_2})
  = (\lvert z_1\rvert\lvert z_2\rvert)e^{j(\theta_1+\theta_2)}.
  $$

### Relating this to the excerpt you posted

In the book, the authors write

$$
C e^{a t},
\qquad\text{with}\quad
C = \lvert C\rvert e^{j\theta}\;(\text{polar})\quad
\text{and}\quad
a = r + j\omega_0\;(\text{rectangular}).
$$

* $C$ is put in **polar form** so its magnitude $\lvert C\rvert$ (an overall scaling) and phase $\theta$ (a time-independent phase shift) are explicit.
* $a$ is placed in **rectangular form** because the **real part** $r$ tells you the exponential **growth/decay rate** $e^{rt}$, while the **imaginary part** $\omega_0$ gives the **angular frequency** of oscillation.

Expanding with Euler’s relation $e^{j\phi} = \cos\phi + j\sin\phi$ they obtain

$$
C e^{a t}
   = \lvert C\rvert e^{rt}\bigl[\cos(\omega_0 t + \theta)
     + j\sin(\omega_0 t + \theta)\bigr],
$$

which cleanly separates:

* **Envelope**: $\lvert C\rvert e^{rt}$ (decay or growth).
* **Oscillation**: $\omega_0$ radians per second.
* **Phase offset**: $\theta$.

That is the practical power of switching between rectangular and polar descriptions of complex numbers.
