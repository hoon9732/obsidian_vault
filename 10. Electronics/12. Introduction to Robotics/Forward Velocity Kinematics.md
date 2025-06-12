This slide introduces **velocity kinematics** using the **Jacobian** matrix for a **2-link planar manipulator**, a fundamental concept in robotics.

---

### 🔧 **Robot Setup**

* A **2-DOF planar robot arm** with:

  * Joint angles: $\theta_1$, $\theta_2$
  * Link lengths: $a_1$, $a_2$
  * End-effector position: $[x_2, y_2]$

---

### 🔹 **Forward Velocity Kinematics (Jacobian Equation)**

The velocity of the end-effector is expressed as:

$$
\begin{bmatrix}
\dot{x}_2 \\
\dot{y}_2
\end{bmatrix}
= J(\theta) \cdot
\begin{bmatrix}
\dot{\theta}_1 \\
\dot{\theta}_2
\end{bmatrix}
$$

Where the **Jacobian matrix** $J$ is:

$$
J =
\begin{bmatrix}
-a_1 \sin\theta_1 - a_2 \sin(\theta_1 + \theta_2) & -a_2 \sin(\theta_1 + \theta_2) \\
a_1 \cos\theta_1 + a_2 \cos(\theta_1 + \theta_2) & a_2 \cos(\theta_1 + \theta_2)
\end{bmatrix}
$$

This matrix maps **joint velocities** $\dot{q} = [\dot{\theta}_1, \dot{\theta}_2]^T$ to **Cartesian velocities** $\dot{x}$.

---

### 🔁 **Inverse Velocity Kinematics**

To find the joint velocities from the end-effector velocity:

$$
\dot{q} = J^{-1} \dot{x}
$$

The explicit inverse is given in the slide as:

$$
\dot{q} = \frac{1}{a_1 a_2 \sin(\theta_2)}
\begin{bmatrix}
a_2 \cos(\theta_1 + \theta_2) & a_2 \sin(\theta_1 + \theta_2) \\
- a_1 \cos(\theta_1) - a_2 \cos(\theta_1 + \theta_2) & - a_1 \sin(\theta_1) - a_2 \sin(\theta_1 + \theta_2)
\end{bmatrix}
\begin{bmatrix}
\dot{x} \\
\dot{y}
\end{bmatrix}
$$

---

### ❗ **Singularities**

* **Jacobian is non-invertible (singular)** when $\sin(\theta_2) = 0$, i.e.:

  $$
  \theta_2 = 0 \text{ or } \pi
  $$

* **What does this imply?**

  * At these configurations, the **end-effector loses a degree of freedom**.
  * Motions in certain Cartesian directions become impossible.
  * Numerically, the robot control may become **unstable or inaccurate**.
  * Geometrically, the links are **fully extended or folded**, collapsing the area the end-effector can influence.

---

### ✅ Key Takeaways

* **Jacobian maps joint velocities to end-effector velocities**.
* Its **inverse** (if exists) allows computing required joint velocities.
* **Singularities** must be avoided in trajectory planning, as they cause **loss of control or infinite joint velocities**.

---

Would you like me to help derive this Jacobian step-by-step or explain how to visualize these singularities geometrically?
