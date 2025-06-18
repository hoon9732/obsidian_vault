Below is a concise rundown of every major concept covered in **Lecture 06** of the ECE430 Signals & Systems course. I’ve grouped them by topic and given the crux of each idea.

---

## 1. Singularity (Impulse-Family) Functions

1. **Unit Impulse, $\delta(t)$**

   * Defined **operationally**: for any $x(t)$,

     $$
       x(t) * \delta(t) = x(t).
     $$

     (i.e.\ $\delta$ is the “identity” under convolution) .
   * **Sifting property**:
     $\displaystyle \int x(t)\,\delta(t - t_0)\,dt = x(t_0)$ .

2. **Unit Doublet, $\delta'(t)$**

   * The **first derivative** of $\delta(t)$.
   * Operationally, it’s the impulse response of any LTI system whose input–output relation is $y(t)=\tfrac{d}{dt}\,x(t)$.
   * Convolution with $\delta'$ differentiates:

     $$
       x(t)*\delta'(t) = \frac{d}{dt}x(t).
     \] :contentReference[oaicite:2]{index=2}.

     $$

3. **Higher-Order Derivatives, $\delta^{(k)}(t)$**

   * The $k$th derivative of $\delta(t)$.
   * Convolution with $\delta^{(k)}(t)$ applies $k$ derivatives:
     $x * \delta^{(k)} = x^{(k)}$. .

4. **Integrals of the Impulse (Ramp, etc.)**

   * Repeated integration of $\delta(t)$ yields functions like the **unit-ramp**
     $r(t)=\int_{-\infty}^t \! \delta(\tau)\,d\tau$. .
   * Convolution with these corresponds to successive integrals of the input.

---

## 2. Review of LTI System Responses

1. **Impulse Response $h(t)$**

   * Entire characterization of a continuous-time LTI system:

     $$
       y(t)=x(t)*h(t).
     \] :contentReference[oaicite:5]{index=5}.

     $$
2. **Convolution Integral**

   * $y(t)=\int_{-\infty}^{\infty}x(\tau)\,h(t-\tau)\,d\tau.$
   * In discrete time: $y[n]=\sum_k x[k]\,h[n-k].$ .

---

## 3. Choosing a “Basis” of Input Signals

We seek a set of “building-block” signals whose LTI responses are simple:

* **Singularity functions** (impulse, doublet, ramp)
* **Complex exponentials** $e^{st}$
* **Step, ramp, sinusoids**, etc.

If we can expand an arbitrary $x(t)$ in these, superposition yields its response.

---

## 4. Complex Exponentials as Eigenfunctions

1. **Eigenfunction Property**

   * Input $x(t)=e^{st}$ into an LTI system with impulse response $h(t)$:

     $$
       y(t)=h(t)*e^{st}
       =H(s)\,e^{st},
     $$

     where $H(s)=\int h(\tau)e^{-s\tau}d\tau$.
   * Thus $e^{st}$ is an eigenfunction and $H(s)$ its eigenvalue. .

2. **Fourier Series / Transform**

   * A **Fourier series** represents a periodic signal as a sum of harmonically related exponentials.
   * The **Fourier transform** does the same for aperiodic signals over a continuous spectrum. .

---

## 5. Continuous-Time Fourier Series (CTFS)

1. **Analysis/Synthesis**

   * **Synthesis**:
     $\displaystyle x(t)=\sum_{k=-\infty}^\infty C_k\,e^{j k\omega_0 t}.$
   * **Analysis** (coefficients):
     $\displaystyle C_k=\frac{1}{T}\int_0^T x(t)e^{-jk\omega_0 t}\,dt.$ .

2. **Convergence and Gibbs Phenomenon**

   * Partial sums approximate continuous signals but overshoot at discontinuities (Gibbs).
   * Under Dirichlet conditions, series converges to the midpoint of any jump. .

---

### References

All definitions and properties above are drawn directly from Lecture 06 of ECE430-306 (Se Young Chun, March 24 2024) .
