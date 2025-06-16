Great question! Let's solve **Problem 2.11** step by step.

---

### **Given:**

* $x(t) = u(t - 3) - u(t - 5)$: a rectangular pulse from $t = 3$ to $t = 5$
* $h(t) = e^{-3t} u(t)$: a one-sided exponential starting at $t = 0$

---

## **(a) Compute $y(t) = x(t) * h(t)$**

We know:

$$
x(t) = 
\begin{cases}
1, & 3 \le t < 5 \\
0, & \text{otherwise}
\end{cases}
$$

So the convolution becomes:

$$
y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \, d\tau = \int_3^5 h(t - \tau) \, d\tau
$$

Let $u = t - \tau \Rightarrow d\tau = -du$

When $\tau = 3$, $u = t - 3$
When $\tau = 5$, $u = t - 5$

$$
y(t) = \int_3^5 e^{-3(t - \tau)} \, d\tau = e^{-3t} \int_3^5 e^{3\tau} \, d\tau
$$

Compute the integral:

$$
\int_3^5 e^{3\tau} \, d\tau = \frac{1}{3} \left( e^{15} - e^{9} \right)
$$

So:

$$
y(t) = e^{-3t} \cdot \frac{1}{3}(e^{15} - e^9)
$$

BUT WAIT! That's valid **only when $t \ge 5$**. We need to consider the limits based on **shifting rectangle**:

Let’s break it into **cases**:

---

### **Case 1: $t < 3$**

* The shifted rectangle $x(\tau)$ and exponential $h(t - \tau)$ do not overlap.
* So:

  $$
  y(t) = 0
  $$

---

### **Case 2: $3 \le t < 5$**

* Overlap begins from $\tau = 3$ to $\tau = t$

$$
y(t) = \int_3^t e^{-3(t - \tau)} d\tau = e^{-3t} \int_3^t e^{3\tau} d\tau
= e^{-3t} \cdot \frac{1}{3}(e^{3t} - e^9) = \frac{1}{3}(1 - e^{9 - 3t})
$$

---

### **Case 3: $5 \le t$**

* Full overlap from $\tau = 3$ to $\tau = 5$

$$
y(t) = \int_3^5 e^{-3(t - \tau)} d\tau = e^{-3t} \cdot \frac{1}{3}(e^{15} - e^9) = \frac{1}{3}(e^{9 - 3t} - e^{15 - 3t})
$$

---

### ✅ Final answer for **(a):**

$$
y(t) =
\begin{cases}
0, & t < 3 \\
\frac{1}{3}(1 - e^{9 - 3t}), & 3 \le t < 5 \\
\frac{1}{3}(e^{9 - 3t} - e^{15 - 3t}), & t \ge 5
\end{cases}
$$

---

## **(b) Compute $g(t) = \frac{d}{dt}x(t) * h(t)$**

We know:

$$
\frac{d}{dt}x(t) = \delta(t - 3) - \delta(t - 5)
$$

So:

$$
g(t) = [\delta(t - 3) - \delta(t - 5)] * h(t)
= h(t - 3) - h(t - 5)
$$

Since $h(t) = e^{-3t} u(t)$, we get:

$$
g(t) = e^{-3(t - 3)} u(t - 3) - e^{-3(t - 5)} u(t - 5)
$$

---

### ✅ Final answer for **(b):**

$$
g(t) = e^{-3(t - 3)} u(t - 3) - e^{-3(t - 5)} u(t - 5)
$$

---

## **(c) How is $g(t)$ related to $y(t)$?**

We used the **derivative property of convolution**:

$$
\frac{d}{dt}x(t) * h(t) = \frac{d}{dt} y(t)
\Rightarrow g(t) = \frac{dy(t)}{dt}
$$

---

### ✅ Final answer for **(c):**

$$
g(t) = \frac{dy(t)}{dt}
$$

---

Let me know if you'd like a graph for visual intuition!
