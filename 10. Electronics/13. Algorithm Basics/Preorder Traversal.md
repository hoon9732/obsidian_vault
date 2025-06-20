### 🔹 Preorder Traversal (DFS - Depth-First Search)

**Preorder traversal** visits nodes in the following order:

1. **Visit the root**
2. **Traverse the left subtree** (or first child)
3. **Traverse the right subtree** (or remaining children)

---

### 🔸 General Order

```
Preorder(node):
    - Process(node)
    - Preorder(left/first child)
    - Preorder(right/remaining children)
```

---

### 🔹 Example: Binary Tree Preorder

Given binary tree:

```
      A
     / \
    B   C
   / \
  D   E
```

**Preorder traversal**: `A → B → D → E → C`

---

### 🔸 Python Code (Binary Tree)

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# Example tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

preorder(root)
```

---

### 🔹 For N-ary Tree (Multiple Children)

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def preorder(node):
    if node:
        print(node.val)
        for child in node.children:
            preorder(child)
```

---

#Algorithm #Tree