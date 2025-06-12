This slide compares the **workspace shapes** of four common types of industrial robots:

---

### **Title**: Workspace Comparison

Each robot type (a–d) is shown with a 3D shape representing the **region in space** its end-effector can reach, also known as its **workspace**.

---

### **(a) Spherical Robot**

* **Workspace**: A hollowed-out spherical section.
* **Structure**: Typically has a rotary base joint, a radial arm extension, and a pivoting motion (like a polar coordinate system).
* **Use case**: Often used in welding or material handling.
* **Limitation**: Singularities and limited reach near the center.

---

### **(b) SCARA Robot (Selective Compliance Assembly Robot Arm)**

* **Workspace**: A flat, cylindrical doughnut shape (wide horizontal reach with vertical Z motion).
* **Structure**: 2 rotary joints for horizontal motion + 1 prismatic (vertical) joint.
* **Use case**: Ideal for fast, precise assembly operations on a horizontal plane.
* **Advantage**: Very fast and precise in planar motion; compliant in Z-axis for insertion tasks.

---

### **(c) Cylindrical Robot**

* **Workspace**: A cylindrical volume.
* **Structure**: Base rotation + linear radial extension + vertical motion (prismatic + rotary joints).
* **Use case**: Material handling, spot welding.
* **Advantage**: Simple mechanics and good reach in vertical applications.

---

### **(d) Cartesian Robot**

* **Workspace**: A rectangular box or cuboid.
* **Structure**: 3 linear axes (X, Y, Z) — like a 3D printer or CNC machine.
* **Use case**: Pick and place, machining, 3D printing.
* **Advantage**: High precision, easy control and programming.
* **Limitation**: Large footprint and lower flexibility compared to articulated arms.

---

### Summary Table (Workspace Shape Comparison):

| Robot Type  | Workspace Shape         | Motion Axes                  |
| ----------- | ----------------------- | ---------------------------- |
| Spherical   | Spherical shell sector  | Rotary + Pivot + Extension   |
| SCARA       | Cylindrical ring (flat) | 2 Rotational + 1 Vertical    |
| Cylindrical | Cylinder                | Rotary base + Linear (Z & R) |
| Cartesian   | Rectangular cuboid      | 3 Linear (X, Y, Z)           |

---

Would you like a more detailed explanation of any specific robot type or their kinematics?
