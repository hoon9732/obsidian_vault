Let’s break down the given signal and solve the problem step by step.

---

### Given:

$$
h[n] = \left(\frac{1}{2}\right)^{n-1} \left\{u[n+3] - u[n-10]\right\}
$$

This represents a **finite-duration signal** modulated by the step function difference:

* $u[n+3] = 1$ for $n \ge -3$
* $u[n-10] = 1$ for $n \ge 10$

So:

$$
h[n] = \left(\frac{1}{2}\right)^{n-1}, \quad \text{for } -3 \le n < 10
$$

$$
h[n] = 0 \quad \text{otherwise}
$$

---

### Now consider:

$$
h[n - k] = \begin{cases}
\left(\frac{1}{2}\right)^{n - k - 1}, & A \le k \le B \\
0, & \text{elsewhere}
\end{cases}
$$

We need to determine the values of $A$ and $B$ in terms of $n$, such that this expression matches the support (non-zero range) of $h[n]$, which is $-3 \le n < 10$.

---

### Step-by-step analysis:

Since $h[n - k]$ is non-zero when:

$$
-3 \le n - k < 10
$$

Solve for $k$:

1. From $-3 \le n - k$:

   $$
   k \le n + 3
   $$

2. From $n - k < 10$:

   $$
   k > n - 10
   \Rightarrow k \ge n - 9 \quad \text{(for integer values)}
   $$

Thus, $k \in [n - 9, n + 3]$

---

### Final Answer:

$$
A = n - 9, \quad B = n + 3
$$

These are the values of $A$ and $B$ in terms of $n$ such that:

$$
h[n - k] = \begin{cases}
\left(\frac{1}{2}\right)^{n - k - 1}, & n - 9 \le k \le n + 3 \\
0, & \text{otherwise}
\end{cases}
$$

Let me know if you want to keep solving more problems from this set!
