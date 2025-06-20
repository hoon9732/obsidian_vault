### 🔹 Level Order Traversal (BFS - Breadth-First Search)

**Level Order Traversal** visits nodes **level by level**, from top to bottom and left to right within each level.

It uses a **queue** to process nodes in order of their depth.

---

### 🔸 General Order

```
LevelOrder(root):
    - Initialize queue with root
    - While queue not empty:
        - Dequeue node
        - Process node
        - Enqueue all children (or left/right for binary tree)
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

**Level order traversal**: `A → B → C → D → E`

---

### 🔸 Python Code (Binary Tree)

```python
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

level_order(root)
```

---

### 🔹 Level Order for N-ary Tree

```python
def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        for child in node.children:
            queue.append(child)
```

---

#Algorithm #Tree