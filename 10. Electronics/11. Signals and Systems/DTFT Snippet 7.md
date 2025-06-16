Let’s go step by step through **Problem 2.17**, which involves solving a **first-order linear differential equation** for an LTI system.

---

### 💡 Given system:

$$
\frac{d}{dt} y(t) + 4y(t) = x(t), \quad \text{with initial rest}
$$

This is a **linear time-invariant (LTI) system** with zero initial conditions.

---

## **(a) Input: $x(t) = e^{(-1 + 3j)t} u(t)$**

We’re solving:

$$
\frac{d}{dt} y(t) + 4y(t) = e^{(-1 + 3j)t} u(t)
$$

### Step 1: Use Laplace Transform

Let’s denote:

* $X(s) = \mathcal{L}\{x(t)\} = \frac{1}{s + 1 - 3j}$
* Let $Y(s)$ be the Laplace Transform of $y(t)$

From the Laplace transform of the equation:

$$
sY(s) + 4Y(s) = X(s) = \frac{1}{s + 1 - 3j}
\Rightarrow Y(s) = \frac{1}{(s + 1 - 3j)(s + 4)}
$$

### Step 2: Use Partial Fractions

$$
Y(s) = \frac{A}{s + 1 - 3j} + \frac{B}{s + 4}
$$

Multiply both sides:

$$
1 = A(s + 4) + B(s + 1 - 3j)
$$

Plug $s = -1 + 3j$:

$$
1 = A((-1 + 3j) + 4) = A(3 + 3j) \Rightarrow A = \frac{1}{3 + 3j}
= \frac{1}{3(1 + j)} = \frac{1 - j}{6}
$$

Plug $s = -4$:

$$
1 = B(-4 + 1 - 3j) = B(-3 - 3j) \Rightarrow B = \frac{1}{-3(1 + j)} = \frac{-1 + j}{6}
$$

### Step 3: Inverse Laplace

Now:

$$
Y(s) = \frac{1 - j}{6} \cdot \frac{1}{s + 1 - 3j} + \frac{-1 + j}{6} \cdot \frac{1}{s + 4}
$$

Using Laplace inverse:

* $\mathcal{L}^{-1}\left\{\frac{1}{s + a}\right\} = e^{-at} u(t)$

So:

$$
y(t) = \frac{1 - j}{6} \cdot e^{(-1 + 3j)t} u(t) + \frac{-1 + j}{6} \cdot e^{-4t} u(t)
$$

---

## ✅ Final Answer for (a):

$$
\boxed{
y(t) = \frac{1 - j}{6} e^{(-1 + 3j)t} u(t) + \frac{-1 + j}{6} e^{-4t} u(t)
}
$$

---

## **(b) Input: $x(t) = e^{-t} \cos(3t) u(t)$**

We are told this is the **real part** of the previous input:

$$
x(t) = \Re\left\{e^{(-1 + 3j)t} u(t)\right\}
\Rightarrow y(t) = \Re\left\{ \text{solution from part (a)} \right\}
$$

### So:

$$
y(t) = \Re\left\{
\frac{1 - j}{6} e^{(-1 + 3j)t}
+ \frac{-1 + j}{6} e^{-4t}
\right\}
$$

Break each term:

* First term:

$$
\frac{1 - j}{6} e^{-t} e^{j3t} = \frac{1 - j}{6} e^{-t} (\cos(3t) + j\sin(3t))
$$

Multiply:

$$
= \frac{1}{6} e^{-t} \left[(1 - j)(\cos(3t) + j\sin(3t))\right]
= \frac{1}{6} e^{-t} \left[\cos(3t) + \sin(3t) + j(\sin(3t) - \cos(3t))\right]
\Rightarrow \Re = \frac{1}{6} e^{-t} (\cos(3t) + \sin(3t))
$$

* Second term:

$$
\Re\left\{ \frac{-1 + j}{6} e^{-4t} \right\} = \frac{-1}{6} e^{-4t}
$$

---

## ✅ Final Answer for (b):

$$
\boxed{
y(t) = \frac{1}{6} e^{-t} (\cos(3t) + \sin(3t)) - \frac{1}{6} e^{-4t}, \quad t \ge 0
}
$$

Let me know if you’d like a plot of the solution!
