### 🔹 Postorder Traversal (DFS - Depth-First Search)

**Postorder traversal** visits nodes in the following order:

1. **Traverse the left subtree** (or all children)
2. **Traverse the right subtree** (or remaining children)
3. **Visit the root**

---

### 🔸 General Order

```
Postorder(node):
    - Postorder(left / first child)
    - Postorder(right / remaining children)
    - Process(node)
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

**Postorder traversal**: `D → E → B → C → A`

---

### 🔸 Python Code (Binary Tree)

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# Example tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

postorder(root)
```

---

### 🔹 N-ary Tree Postorder Traversal

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def postorder(node):
    if node:
        for child in node.children:
            postorder(child)
        print(node.val)
```

---

#Algorithm #Tree