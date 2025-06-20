### 🔹 Binary Search Tree (BST)

A **Binary Search Tree** is a **binary tree** where each node follows the **BST property**:

* **Left subtree** contains values **less than** the node.
* **Right subtree** contains values **greater than** the node.
* No duplicate values (in standard BSTs).

---

### 🔸 BST Operations

| Operation   | Description                                       |
| ----------- | ------------------------------------------------- |
| `insert(x)` | Add a new node maintaining BST property           |
| `search(x)` | Check if value `x` exists in the tree             |
| `delete(x)` | Remove a node and rebalance the tree if necessary |
| `inorder()` | Returns values in **sorted order**                |

---

### 🔹 BST Example Structure

```
        8
       / \
      3   10
     / \    \
    1   6    14
```

---

### 🔸 Python Code (Insert, Search, Inorder)

```python
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return BSTNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if not node or node.val == val:
            return node
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.val, end=' ')
            self._inorder(node.right)
```

---

### 🔸 Example Usage

```python
bst = BST()
for x in [8, 3, 10, 1, 6, 14]:
    bst.insert(x)

bst.inorder()  # Output: 1 3 6 8 10 14
print(bst.search(6) is not None)  # True
print(bst.search(7) is not None)  # False
```

---

#Algorithm #Tree