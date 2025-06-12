This slide explains how to **compose multiple rotation matrices** with respect to a **fixed reference frame** (often called the **world frame**, denoted $o_0$). This is common in robot kinematics, when multiple rotations or transformations are applied **relative to a common origin**.

---

## 🔄 Summary: Composition of Rotations (Fixed Frame)

---

### 🧭 Fixed vs. Moving Frame

* **Fixed frame composition**: Rotations are applied about the **same reference frame** (e.g., the global/world frame $o_0$).
* **Moving frame composition**: Rotations are applied **sequentially in rotating frames** (we’ll talk about that later).

---

### 📌 What’s Happening in This Slide?

Let’s break it down.

---

### Step 1: Define Frames

* Let $R^0_1$ be the rotation matrix **from frame 1 to frame 0**.
* Let $R$ be a rotation **we want to apply**, but it’s defined **in frame 0**.
* We need to **express that rotation from frame 1’s point of view** to apply it correctly.

---

### Step 2: Change of Basis (Similarity Transform)

To convert $R$ (in frame 0) into frame 1’s perspective:

$$
R' = (R^0_1)^{-1} \cdot R \cdot R^0_1
$$

This is just a **similarity transformation**, changing the basis from frame 0 to frame 1.

---

### Step 3: Compose Rotations (in the fixed frame)

Now that we’ve expressed $R$ in frame 1 (i.e., $R'$), we **post-multiply** it to update $R^0_1$:

$$
R^0_2 = R^0_1 \cdot R'
$$

Substituting in the expression for $R'$:

$$
R^0_2 = R^0_1 \cdot \left[ (R^0_1)^{-1} R R^0_1 \right] = R R^0_1
$$

---

## 🟨 Final Result:

$$
\boxed{R^0_2 = R R^0_1}
$$

This is called **pre-multiplication**, because we apply the new rotation **before** the previous one, since everything is being expressed **relative to the fixed frame** $o_0$.

---

## 🆚 Pre-multiplication vs. Post-multiplication

| Term                    | Context                         | Interpretation                                                                                                                  |
| ----------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Pre-multiplication**  | **Fixed frame (world)**         | New rotation is expressed in the global frame and comes **before** the previous transformation: $R_{\text{new}} R_{\text{old}}$ |
| **Post-multiplication** | **Rotating frame (body frame)** | New rotation is expressed **relative to the current frame** and comes **after**: $R_{\text{old}} R_{\text{new}}$                |

---

## ✅ Takeaway

* This slide explains how to properly **compose rotations in a fixed reference frame**.
* You must **pre-multiply** new rotations (defined in the fixed frame) when updating the system's orientation.

---

Would you like me to compare this with the **moving frame composition** next (i.e., post-multiplication)?
