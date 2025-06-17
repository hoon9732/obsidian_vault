Here’s your **Lecture 10 Pop Quiz** on **Continuous-Time Fourier Transform (C.T.F.T.)**, **2D Fourier Transforms**, and **impulse train representations**. Each question is immediately followed by its **answer and explanation** — perfect for study and review.

---

## 📘 Pop Quiz: Signals & Systems – Lecture 10

**Topics:** Derivation of C.T.F.T., FT of periodic signals, Duality, 2D C.T.F.T.

---

### 🔹 Part A: Conceptual Questions (with Answers)

---

**1. \[Deriving C.T.F.T.]**
**Q:** What is the connection between Fourier Series coefficients $a_k$ and the Fourier Transform $X(f)$?

**A:**

$$
T a_k = X(kf_0)
$$

**Explanation:**
As the period $T \to \infty$, the discrete samples $a_k$ become samples of a continuous function $X(f)$, forming the **envelope** of the Fourier Transform.

---

**2. \[FT of Periodic Signal]**
**Q:** What is the Fourier Transform of a periodic signal $x(t) = \sum a_k e^{j2\pi k f_0 t}$?

**A:**

$$
X(f) = \sum_{k=-\infty}^{\infty} a_k \delta(f - kf_0)
$$

**Explanation:**
The FT of a periodic signal becomes a **train of impulses** located at harmonics of the base frequency.

---

**3. \[Synthesis Equation]**
**Q:** What happens to the synthesis equation of a Fourier series as $T \to \infty$?

**A:**

$$
x(t) = \int_{-\infty}^{\infty} X(f) e^{j2\pi f t} df
$$

**Explanation:**
The synthesis equation of Fourier Series transitions to that of the **Fourier Transform**, reconstructing aperiodic signals.

---

**4. \[Duality Property]**
**Q:** State the duality property of the C.T.F.T.

**A:**
If $x(t) \leftrightarrow X(f)$, then

$$
X(t) \leftrightarrow x(-f)
$$

**Explanation:**
Duality swaps the roles of time and frequency domains.

---

**5. \[Parseval’s Theorem]**
**Q:** What does Parseval's theorem say about the total energy of a signal?

**A:**

$$
\int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df
$$

**Explanation:**
**Energy is conserved** between time and frequency domains.

---

**6. \[Convolution Property]**
**Q:** How does convolution in time relate to the frequency domain?

**A:**

$$
x(t) * h(t) \leftrightarrow X(f) H(f)
$$

**Explanation:**
Time-domain convolution equals **multiplication in frequency**.

---

**7. \[Multiplication Property]**
**Q:** What does multiplication in time domain correspond to in frequency domain?

**A:**

$$
x_1(t) x_2(t) \leftrightarrow X_1(f) * X_2(f)
$$

**Explanation:**
**Multiplication in time = convolution in frequency**, by duality.

---

### 🔹 Part B: 2D Fourier Transform (with Answers)

---

**8. \[2D C.T.F.T.]**
**Q:** What is the 2D Continuous-Time Fourier Transform of $f(x, y)$?

**A:**

$$
F(u, v) = \iint f(x, y) e^{-j2\pi(ux + vy)} dx dy
$$

**Explanation:**
This extends 1D C.T.F.T. to spatial signals, analyzing **spatial frequency content**.

---

**9. \[2D Conjugacy]**
**Q:** If $f(x, y)$ is real, what is the conjugacy property of its transform $F(u, v)$?

**A:**

$$
F^*(u, v) = F(-u, -v)
$$

**Explanation:**
For real signals, the Fourier Transform has **conjugate symmetry**.

---

**10. \[2D Rectangular Pulse]**
**Q:** What is the Fourier Transform of a 2D rectangular pulse of size $X_0 \times Y_0$?

**A:**

$$
F(u, v) = \frac{\sin(2\pi X_0 u)}{\pi u} \cdot \frac{\sin(2\pi Y_0 v)}{\pi v}
$$

**Explanation:**
This is a **2D sinc function** — the product of 1D transforms along each axis.

---

**11. \[2D Gaussian]**
**Q:** What is the Fourier Transform of a 2D Gaussian centered at the origin?

**A:**

$$
F(u, v) = e^{-\sigma^2 4\pi^2 (u^2 + v^2)}
$$

**Explanation:**
A Gaussian in space transforms to a **Gaussian in frequency** — uniquely self-Fourier.

---

**12. \[Circular Disk]**
**Q:** What is the FT of a 2D circular disk of radius $a$?

**A:**

$$
F(\rho) = a \cdot \frac{J_1(\pi a \rho)}{\rho}, \quad \rho = \sqrt{u^2 + v^2}
$$

**Explanation:**
This is a **Bessel function**, showing circular symmetry in the frequency domain.

---

Would you like this formatted into a printable **PDF** or interactive online format for quiz practice?
