**“Real” and “Right-Sided” in Discrete-Time Signals, and Their Impact on ROC**

---

### 1. Real $x[n]$

* **Definition:** $x[n]$ is *real* if every sample $x[n]$ is a real number (no imaginary part).
* **Consequence in the $Z$-domain:** Realness implies that the polynomial (or rational) coefficients in

  $$
    X(z)=\sum_{n=-\infty}^{\infty}x[n]\,z^{-n}
  $$

  are real.  Equivalently, any pole or zero off the real axis must come with its complex conjugate—so that the overall transfer function has real coefficients.

---

### 2. Right-Sided $x[n]$

* **Definition:** $x[n]$ is *right-sided* (or *causal*) if

  $$
    x[n] = 0\quad\forall\,n<0.
  $$
* **Physical interpretation:** A causal system doesn’t “know” future inputs; its output at time $n$ depends only on $x[0],x[1],\dots,x[n]$.

---

### 3. Impact on the ROC

The **Region of Convergence** for the power-series
$\;X(z)=\sum_{n=0}^{\infty}x[n]\,z^{-n}$
must be a ring (or disk) in the complex $z$-plane that makes the infinite sum converge.

* **Right-sided ⇒ ROC is outside the outermost pole**
  Because a causal sequence’s $Z$-series in powers of $z^{-1}$ behaves like a power series in $1/z$, the ROC must be of the form

  $$
    |z| > R_{\max},
  $$

  where $R_{\max}$ is the magnitude of the pole lying farthest from the origin.  Only for $|z|$ strictly larger than that pole do all terms $x[n]\,z^{-n}$ decay geometrically and the sum converge.

* **Left-sided ⇒ ROC is inside the innermost pole**
  (Not our case, but for contrast: if $x[n]$ were nonzero only for $n\le N$, the ROC would be $|z|<R_{\min}$.)

* **Two-sided ⇒ ROC is between poles**
  If $x[n]$ extends both for positive and negative $n$, the ROC is an annulus bounded by the nearest and farthest pole magnitudes.

---

### 4. Summary

* **Real** ⇒ Poles and zeros occur in conjugate-pairs; $X(z)$ has real polynomial coefficients.
* **Right-sided (causal)** ⇒ ROC is of the form $\;|z|>r$, running outward from the largest-magnitude pole.
* **Implication for stability:** If the ROC $|z|>r$ also includes the unit circle $|z|=1$, then the system is BIBO‐stable.
