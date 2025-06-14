To recover $w(t)=x_1(t)\,x_2(t)$ from its samples $w_p(t)=w(t)\sum_n\delta(t-nT)$ by ideal low‐pass filtering, we need to make sure no aliasing occurs when sampling.  The key steps are:

1. **Find the bandwidth of $w(t)$.**
   In the frequency domain

   $$
   W(j\omega)
   \;=\;\bigl[X_1\ast X_2\bigr](j\omega)
   \;=\;\frac1{2\pi}\int_{-\infty}^{\infty}X_1(j\Omega)\,X_2\bigl(j(\omega-\Omega)\bigr)\,d\Omega.
   $$

   Since $X_1(j\omega)$ is supported on $|\omega|\le\omega_1$ and $X_2(j\omega)$ on $|\omega|\le\omega_2$, their convolution is supported on

   $$
     -(\omega_1+\omega_2)\;\le\;\omega\;\le\;\omega_1+\omega_2.
   $$

   Thus $w(t)$ is bandlimited to

   $$
     \Omega_m \;=\;\omega_1+\omega_2.
   $$

2. **Apply the sampling theorem.**
   To avoid aliasing when sampling a bandlimited signal of maximum frequency $\Omega_m$, the sampling angular frequency must satisfy

   $$
     \omega_s \;=\;\frac{2\pi}{T} \;>\;2\,\Omega_m
     \quad\Longrightarrow\quad
     \frac{2\pi}{T}\;>\;2\,(\omega_1+\omega_2)
     \;\Longrightarrow\;
     T\;<\;\frac{\pi}{\omega_1+\omega_2}.
   $$

   Hence the **maximum** permissible sampling interval is

   $$
     \boxed{T_{\max} \;=\;\frac{\pi}{\omega_1+\omega_2}\,.}
   $$

3. **Reconstruction filter.**
   You then pass the sampled train $w_p(t)$ through an ideal low‐pass filter with cutoff

   $$
     \omega_c \;=\;\omega_1+\omega_2
     \quad\text{(or anything up to }\tfrac{\omega_s}{2}\text{)}
   $$

   to exactly recover $w(t)$.

---

**Answer:**

$$
\displaystyle T_{\max} \;=\;\frac{\pi}{\omega_1+\omega_2}\,,
$$

so that $\omega_s=2\pi/T>2(\omega_1+\omega_2)$ and no aliasing occurs.
