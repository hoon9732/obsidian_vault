Here’s a concise “cheat-sheet” of the core ideas and formulas from Lectures 19–22 (Dynamics), organized for quick exam review.&#x20;

---

## Key Concepts

* **Kinematics recap**

  * Forward kinematics: $q\mapsto (R^0_n,o^0_n)$ via successive DH transforms.
  * Jacobian $J(q)$: maps $\dot q\to[v;\,\omega]$ for the end‐effector (or any link CoM).&#x20;

* **Kinetic energy $K$**

  * Each link’s contribution:

    $$
      K_i
      = \tfrac12\,m_i\,v_{c_i}^T v_{c_i}
      \;+\;
      \tfrac12\,\omega_i^T\,R_i(q)\,I_i\,R_i(q)^T\,\omega_i
    $$
  * In joint‐space:

    $$
      K = \tfrac12\,\dot q^T\,D(q)\,\dot q,
      \quad
      D(q)\succeq0\text{ symmetric (inertia matrix).}
    \] :contentReference[oaicite:2]{index=2}

    $$

* **Potential energy $P$**

  * Gravity only (rigid links):

    $$
      P(q) = \sum_{i=1}^n m_i\,g^T\,r_{c_i}(q).
    \] :contentReference[oaicite:3]{index=3}

    $$

* **Lagrangian & E-L equations**

  * $L(q,\dot q)=K-P$.
  * For each generalized coordinate $q_k$:

    $$
      \frac{d}{dt}\Bigl(\frac{\partial L}{\partial\dot q_k}\Bigr)
      \;-\;
      \frac{\partial L}{\partial q_k}
      \;=\;
      \tau_k
      \quad\Bigl(\text{or }f_k\Bigr).
    \] :contentReference[oaicite:4]{index=4}

    $$

* **Equations of motion**

  * In matrix form:

    $$
      D(q)\,\ddot q
      + C(q,\dot q)\,\dot q
      + g(q)
      = \tau,
    $$

    where

    * $D(q)$ – inertia matrix,
    * $C(q,\dot q)\dot q$ – Coriolis/centrifugal terms,
    * $g(q)=\nabla_q P$ – gravity vector.&#x20;

* **Inertia tensor & parallel‐axis theorem**

  * Body‐frame inertia $I_i$ is constant; inertial‐frame inertia is
    $R_i\,I_i\,R_i^T$.
  * If you know centroidal inertia $I_c$, then about a parallel axis at distance $d$:

    $$
      I_o = I_c + m\,d^2.
    \] :contentReference[oaicite:6]{index=6}
    $$

---

## Key Formulas

1. **Jacobian for link i’s CoM**

   $$
   \begin{aligned}
     v_{c_i} &= J_{v_i}(q)\,\dot q,\\
     \omega_i &= J_{\omega_i}(q)\,\dot q.
   \end{aligned}
   $$
2. **Inertia matrix**

   $$
     D(q)
     = \sum_{i=1}^n \Bigl[
       m_i\,J_{v_i}^T\,J_{v_i}
       \;+\;
       J_{\omega_i}^T\,R_i\,I_i\,R_i^T\,J_{\omega_i}
     \Bigr].
   $$
3. **Coriolis matrix (via Christoffel symbols)**

   $$
   \begin{aligned}
     c_{ijk}
     &= \tfrac12\Bigl(\tfrac{\partial d_{kj}}{\partial q_i}
                   +\tfrac{\partial d_{ki}}{\partial q_j}
                   -\tfrac{\partial d_{ij}}{\partial q_k}\Bigr),\\
     [C(q,\dot q)]_{\,kj}
     &= \sum_{i=1}^n c_{ijk}\,\dot q_i.
   \end{aligned}
   $$
4. **Gravity vector**

   $$
     g(q) =
     \begin{bmatrix}
       \tfrac{\partial P}{\partial q_1}\\[3pt]
       \vdots\\[-3pt]
       \tfrac{\partial P}{\partial q_n}
     \end{bmatrix}.
   $$
5. **Euler–Lagrange compact**

   $$
     \frac{d}{dt}(D\,\dot q) - \tfrac12\Bigl(\nabla_q D\Bigr)\,\dot q\,\dot q
     + \nabla_q P
     = \tau.
   $$

---

Keep this sheet at hand—understand how each term arises (especially from kinetic/potential energies and the Jacobian), and you’ll have the core dynamics toolbox ready for your final.
