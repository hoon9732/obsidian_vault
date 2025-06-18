**Title: Convolution of Discrete-Time Signals (Problem 2.1)**

We are given:

$$
x[n] = \delta[n] + 2\delta[n-1] - \delta[n-3]
$$

$$
h[n] = 2\delta[n+1] + 2\delta[n-1]
$$

We are to compute the following convolutions:

---

### **(a) $y_1[n] = x[n] * h[n]$**

Use the definition of convolution:

$$
y[n] = \sum_{k=-\infty}^{\infty} x[k] h[n-k]
$$

List non-zero values:

* $x[n]$: nonzero at $n = 0, 1, 3$

  * $x[0] = 1$
  * $x[1] = 2$
  * $x[3] = -1$

* $h[n]$: nonzero at $n = -1, 1$

  * $h[-1] = 2$
  * $h[1] = 2$

Now compute $y_1[n]$:

$$
\begin{align*}
y_1[n] &= x[n] * h[n] \\
&= \sum_{k} x[k] \cdot h[n-k]
\end{align*}
$$

Compute individual terms:

* For $n = -1$:

  $$
  y_1[-1] = x[0] \cdot h[-1] = 1 \cdot 2 = 2
  $$
* $n = 0$:

  $$
  y_1[0] = x[1] \cdot h[-1] = 2 \cdot 2 = 4
  $$
* $n = 1$:

  $$
  y_1[1] = x[0] \cdot h[1] + x[1] \cdot h[0] = 1 \cdot 2 + 2 \cdot 0 = 2
  $$
* $n = 2$:

  $$
  y_1[2] = x[1] \cdot h[1] + x[3] \cdot h[-1] = 2 \cdot 2 + (-1) \cdot 2 = 4 - 2 = 2
  $$
* $n = 4$:

  $$
  y_1[4] = x[3] \cdot h[1] = -1 \cdot 2 = -2
  $$

So:

$$
\boxed{y_1[n] = 2\delta[n+1] + 4\delta[n] + 2\delta[n+1] + 2\delta[n+2] - 2\delta[n-4]}
$$

---

### **(b) $y_2[n] = x[n+2] * h[n]$**

This is convolution of a **time-advanced** signal. We know:

$$
x[n+2] = \delta[n+2] + 2\delta[n+1] - \delta[n-1]
$$

Use the same method as in (a), or use **time-shift property** of convolution:

$$
x[n+2] * h[n] = y_1[n+2]
$$

So:

$$
\boxed{y_2[n] = y_1[n+2]}
$$

i.e., shift all values of $y_1[n]$ left by 2.

So:

* $y_2[-3] = y_1[-1] = 2$
* $y_2[-2] = y_1[0] = 4$
* $y_2[-1] = y_1[1] = 2$
* $y_2[0] = y_1[2] = 2$
* $y_2[2] = y_1[4] = -2$

---

### **(c) $y_3[n] = x[n] * h[n+2]$**

Again, use time-shift property of convolution:

$$
x[n] * h[n+2] = y_1[n - 2]
$$

So:

$$
\boxed{y_3[n] = y_1[n - 2]}
$$

Shift $y_1[n]$ **right by 2**:

* $y_3[1] = y_1[-1] = 2$
* $y_3[2] = y_1[0] = 4$
* $y_3[3] = y_1[1] = 2$
* $y_3[4] = y_1[2] = 2$
* $y_3[6] = y_1[4] = -2$

---

Let me know if you'd like plots for each of the three $y[n]$ signals!
