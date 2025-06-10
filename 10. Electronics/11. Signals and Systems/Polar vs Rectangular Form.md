When we work with complex numbers we can describe each number in **two equivalent ways**, depending on which pieces of information we want to emphasize:

||What you write|What the symbols mean|How to recover one form from the other|
|---|---|---|---|
|**Rectangular (Cartesian) form**|z=x+j yz = x + j\,y|• xx: real (horizontal) component• yy: imaginary (vertical) component|∣z∣=x2+y2\lvert z\rvert = \sqrt{x^{2}+y^{2}}θ=tan⁡−1 ⁣(yx)\theta = \tan^{-1}\!\bigl(\tfrac{y}{x}\bigr) (use `atan2` to get the correct quadrant)|
|**Polar (exponential) form**|z=∣z∣ejθ=∣z∣(cos⁡θ+jsin⁡θ)z = \lvert z\rvert e^{j\theta} = \lvert z\rvert(\cos\theta + j\sin\theta)|• ∣z∣\lvert z\rvert (often written rr): the **magnitude** or distance of zz from the origin• θ\theta: the **angle** (or _argument/phase_) measured counter-clockwise from the positive real axis|x=∣z∣cos⁡θx = \lvert z\rvert\cos\thetay=∣z∣sin⁡θy = \lvert z\rvert\sin\theta|

### Why the two forms are useful

- **Rectangular form** is convenient when you need to **add or subtract** complex numbers because you simply add/subtract corresponding real and imaginary parts:
    
    (x1+jy1)  +  (x2+jy2)  =  (x1+x2)  +  j(y1+y2).(x_1 + j y_1) \;+\; (x_2 + j y_2) \;=\; (x_1 + x_2) \;+\; j(y_1 + y_2).
- **Polar form** is ideal for **multiplication, division, and exponentiation** because magnitudes and phases separate cleanly:
    
    (∣z1∣ejθ1)(∣z2∣ejθ2)=(∣z1∣∣z2∣)ej(θ1+θ2).(\lvert z_1\rvert e^{j\theta_1})(\lvert z_2\rvert e^{j\theta_2}) = (\lvert z_1\rvert\lvert z_2\rvert)e^{j(\theta_1+\theta_2)}.

### Relating this to the excerpt you posted

In the book, the authors write

Ceat,withC=∣C∣ejθ  (polar)anda=r+jω0  (rectangular).C e^{a t}, \qquad\text{with}\quad C = \lvert C\rvert e^{j\theta}\;(\text{polar})\quad \text{and}\quad a = r + j\omega_0\;(\text{rectangular}).

- CC is put in **polar form** so its magnitude ∣C∣\lvert C\rvert (an overall scaling) and phase θ\theta (a time-independent phase shift) are explicit.
    
- aa is placed in **rectangular form** because the **real part** rr tells you the exponential **growth/decay rate** erte^{rt}, while the **imaginary part** ω0\omega_0 gives the **angular frequency** of oscillation.
    

Expanding with Euler’s relation ejϕ=cos⁡ϕ+jsin⁡ϕe^{j\phi} = \cos\phi + j\sin\phi they obtain

Ceat=∣C∣ert[cos⁡(ω0t+θ)+jsin⁡(ω0t+θ)],C e^{a t} = \lvert C\rvert e^{rt}\bigl[\cos(\omega_0 t + \theta) + j\sin(\omega_0 t + \theta)\bigr],

which cleanly separates:

- **Envelope**: ∣C∣ert\lvert C\rvert e^{rt} (decay or growth).
    
- **Oscillation**: ω0\omega_0 radians per second.
    
- **Phase offset**: θ\theta.
    

That is the practical power of switching between rectangular and polar descriptions of complex numbers.