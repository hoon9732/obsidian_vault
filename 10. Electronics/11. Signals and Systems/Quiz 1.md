To design a **bandpass filter** using a given **ideal lowpass filter** with frequency response $H_{LP}(e^{j\omega})$, where the cutoff frequency is $\omega_c = \frac{\pi}{4}$, you can **modulate** (i.e., frequency shift) the lowpass filter to center it at your desired passband.

---

### 🔹 Step-by-Step: From Lowpass to Bandpass

#### **1. Define Desired Bandpass Frequency Range**

Suppose you want the bandpass filter to pass frequencies between:

$$
\omega_1 = \frac{\pi}{3}, \quad \omega_2 = \frac{2\pi}{3}
$$

The center frequency of the bandpass is:

$$
\omega_c = \frac{\omega_1 + \omega_2}{2} = \frac{\pi}{2}
$$

The bandwidth is:

$$
B = \omega_2 - \omega_1 = \frac{\pi}{3}
$$

#### **2. Use Lowpass Filter as Prototype**

Your prototype lowpass filter has a cutoff at $\frac{\pi}{4}$, which is less than $B/2 = \frac{\pi}{6}$, so you should **adjust it** to have a cutoff of $\frac{B}{2} = \frac{\pi}{6}$.

Redesign your lowpass filter $h_{LP}[n]$ such that:

$$
H_{LP}(e^{j\omega}) = 
\begin{cases}
1, & |\omega| < \frac{\pi}{6} \\
0, & \text{otherwise}
\end{cases}
$$

You can implement this using the **ideal sinc function**:

$$
h_{LP}[n] = \frac{\sin\left(\frac{\pi}{6} n\right)}{\pi n}, \quad n \ne 0; \quad h_{LP}[0] = \frac{1}{6}
$$

#### **3. Modulate to Desired Center Frequency**

To convert the lowpass filter to a bandpass filter centered at $\omega_0 = \frac{\pi}{2}$, **modulate** it:

$$
h_{BP}[n] = h_{LP}[n] \cdot \cos(\omega_0 n) = h_{LP}[n] \cdot \cos\left(\frac{\pi}{2} n\right)
$$

This shifts the frequency content of $h_{LP}[n]$ to be centered at $\omega = \pm \omega_0$.

---

### 🔹 Final Design Equation

$$
h_{BP}[n] = \frac{\sin\left(\frac{\pi}{6} n\right)}{\pi n} \cdot \cos\left(\frac{\pi}{2} n\right)
\quad\text{for } n \ne 0; \quad h_{BP}[0] = \frac{1}{6}
$$

This yields an **ideal bandpass filter** with center frequency $\frac{\pi}{2}$ and bandwidth $\frac{\pi}{3}$.

---

### 🔹 Optional: Windowing for FIR Implementation

To make this implementable (finite impulse response), apply a **window function** (e.g., Hamming, Hann) to truncate $h_{BP}[n]$ for a desired length:

$$
h_{BP\_win}[n] = h_{BP}[n] \cdot w[n], \quad -N \leq n \leq N
$$

---

Would you like me to generate Python code or a graph for this filter design?
