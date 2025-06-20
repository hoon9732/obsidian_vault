### 🔹 Nonlinear Data Structure

A **nonlinear data structure** stores elements in a **hierarchical** or **interconnected** manner, where a single element may be connected to multiple others. Traversal isn't strictly sequential.

---

### 🔸 Characteristics

* Not stored in a single line
* Can represent complex relationships (e.g., hierarchy, networks)
* More flexible than linear structures

---

### 🔹 Common Types of Nonlinear Data Structures

| Structure       | Description                                              | Python Representation                |
| --------------- | -------------------------------------------------------- | ------------------------------------ |
| **Tree**        | Hierarchical structure with parent-child relationships   | Class-based `Node` or `dict`         |
| **Binary Tree** | Tree where each node has ≤ 2 children                    | Class-based                          |
| **Heap**        | Complete binary tree used for priority management        | `heapq` module                       |
| **Graph**       | Nodes connected by edges (can be directed or undirected) | `dict`, `adjacency list`, `networkx` |
| **Trie**        | Tree-like structure for string prefix matching           | Class-based with children as dict    |

---

### 🔸 Example: Tree

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

root = TreeNode("A")
root.children = [TreeNode("B"), TreeNode("C")]
```

---

### 🔸 Example: Binary Tree

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
```

---

### 🔸 Example: Graph (Adjacency List)

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
```

---

### 🔸 Example: Heap (Min-Heap)

```python
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappop(heap)  # returns 1
```

---

#Algorithm
