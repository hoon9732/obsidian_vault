Great! Let's solve **Problem 2.8**, which involves continuous-time convolution:

---

### **Given:**

$$
x(t) = 
\begin{cases}
t + 1, & 0 \le t \le 1 \\
2 - t, & 1 < t \le 2 \\
0, & \text{elsewhere}
\end{cases}
$$

This is a **triangular pulse** from $t = 0$ to $t = 2$, with a peak at $t = 1$.

$$
h(t) = \delta(t + 2) + 2\delta(t + 1)
$$

This is a **sum of shifted Dirac delta functions**, located at $t = -2$ and $t = -1$.

---

### **Step 1: Use the convolution property**

Convolution with delta functions simplifies using the **sifting property**:

$$
x(t) * h(t) = x(t) * [\delta(t + 2) + 2\delta(t + 1)] \\
= x(t + 2) + 2x(t + 1)
$$

That’s it! No integration needed, just a shift and scaling.

---

### **Step 2: Analyze support of $x(t + 2)$ and $x(t + 1)$**

We know that $x(t)$ is nonzero only for $0 \le t \le 2$

So:

* $x(t + 2)$ is nonzero for $t + 2 \in [0, 2] \Rightarrow t \in [-2, 0]$
* $x(t + 1)$ is nonzero for $t + 1 \in [0, 2] \Rightarrow t \in [-1, 1]$

Thus:

* $x(t + 2)$ is a triangular pulse from $t = -2$ to $t = 0$
* $2x(t + 1)$ is a scaled triangular pulse from $t = -1$ to $t = 1$

---

### **Step 3: Compute the final expression piecewise**

Let’s write the expressions for each range:

#### 1. For $-2 \le t \le -1$:

* $x(t + 2) = (t + 2) + 1 = t + 3$
* $x(t + 1) = 0$

$$
y(t) = x(t + 2) + 2x(t + 1) = t + 3 + 0 = t + 3
$$

---

#### 2. For $-1 < t \le 0$:

* $x(t + 2) = 2 - (t + 2) = 0$ to 1 → decreasing: $x(t + 2) = 2 - t - 2 = -t$
* $x(t + 1) = (t + 1) + 1 = t + 2$

$$
y(t) = (-t) + 2(t + 2) = -t + 2t + 4 = t + 4
$$

---

#### 3. For $0 < t \le 1$:

* $x(t + 2) = 0$
* $x(t + 1) = 2 - (t + 1) = 1 - t$

$$
y(t) = 0 + 2(1 - t) = 2 - 2t
$$

---

### **Final answer:**

$$
y(t) = 
\begin{cases}
t + 3, & -2 \le t \le -1 \\
t + 4, & -1 < t \le 0 \\
2 - 2t, & 0 < t \le 1 \\
0, & \text{elsewhere}
\end{cases}
$$

---

### Optional Sketch (Verbal Description):

* From $t = -2$ to $-1$: linearly increasing from 1 to 2
* From $t = -1$ to $0$: linearly increasing from 3 to 4
* From $t = 0$ to $1$: linearly decreasing from 2 to 0

Let me know if you’d like a plotted sketch!
