### 🔹 Tree

A **tree** is a **nonlinear hierarchical data structure** made up of **nodes**, where:

* The topmost node is the **root**.
* Each node may have **zero or more children**.
* There are **no cycles** (unlike graphs).
* Trees are often used to represent hierarchical data (e.g., file systems, XML, parsers).

---

### 🔸 Basic Terms

| Term        | Meaning                                     |
| ----------- | ------------------------------------------- |
| **Root**    | Top node of the tree                        |
| **Leaf**    | Node with no children                       |
| **Parent**  | Node directly above another node            |
| **Child**   | Node directly below another node            |
| **Subtree** | A tree formed by a node and its descendants |
| **Height**  | Longest path from root to leaf              |
| **Depth**   | Distance from root to a node                |

---

### 🔹 Example Tree Structure

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

---

### 🔸 Tree Node Class (Python)

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

# Creating tree
root = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")

root.children = [nodeB, nodeC]
nodeB.children = [nodeD, nodeE]
nodeC.children = [nodeF]
```

---

### 🔹 Tree Traversal Methods

| Traversal Type        | Description                           | Example Order on Above Tree |
| --------------------- | ------------------------------------- | --------------------------- |
| **DFS - Preorder**    | Visit root, then children recursively | A, B, D, E, C, F            |
| **DFS - Postorder**   | Visit children, then root             | D, E, B, F, C, A            |
| **BFS - Level Order** | Visit level by level (uses queue)     | A, B, C, D, E, F            |

---

### 🔸 Example: Preorder DFS

```python
def preorder(node):
    if not node:
        return
    print(node.val)
    for child in node.children:
        preorder(child)

preorder(root)
```

---

#Algorithm #Tree