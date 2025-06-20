### 🔹 Inorder Traversal (for Binary Trees)

**Inorder traversal** visits nodes in the following order:

1. **Traverse the left subtree**
2. **Visit the root**
3. **Traverse the right subtree**

---

### 🔸 General Order

```
Inorder(node):
    - Inorder(left)
    - Process(node)
    - Inorder(right)
```

---

### 🔹 Example: Binary Tree

```
      A
     / \
    B   C
   / \
  D   E
```

**Inorder traversal**: `D → B → E → A → C`

---

### 🔸 Python Code (Binary Tree)

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# Example tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

inorder(root)
```

---

### 🔹 Notes

* **Inorder traversal** is only defined for **binary trees**.
* In a **binary search tree (BST)**, **inorder traversal** returns nodes in **sorted order**.

---

#Algorithm #Tree