We want to “stretch” the occupied band

$$
|Ω|<\tfrac{3π}{14}
$$

into the full baseband

$$
|ω|<π
$$

by a rational rate change $L/M$.  After up-sampling by $L$ and then down-sampling by $M$, the $k=0$ branch of the DTFT is

$$
Y(e^{jω})\Big|_{k=0}
= X\!\Bigl(e^{j\frac{L}{M}ω}\Bigr)
$$

so its support is

$$
\Bigl|\tfrac{L}{M}\,ω\Bigr|<\tfrac{3π}{14}
\quad\Longleftrightarrow\quad
|ω|<\frac{3π}{14}\,\frac{M}{L}.
$$

To make that equal $|ω|<π$ we require

$$
\frac{3π}{14}\;\frac{M}{L}\;=\;π
\quad\Longrightarrow\quad
\frac{M}{L}=\frac{14}{3}.
$$

The smallest integer solution is

$$
\boxed{L=3,\quad M=14.}
$$

Hence **upsample by 3**, then **downsample by 14** (with the usual anti‐aliasing filter in between), will expand the nonzero band $|Ω|<3π/14$ out to fill $|ω|<π$ without overlap.
