### 🔹 Linear Data Structure

A **linear data structure** stores elements **sequentially**, with each element connected to its next (and optionally previous) element. Traversal is done **one after another** in a straight line.

---

### 🔸 Characteristics

* Ordered elements
* Single-level memory (no branching like in trees/graphs)
* Simple traversal: left to right or front to back

---

### 🔹 Common Types of Linear Data Structures in Python

| Structure        | Description                                   | Example Functions                         |
| ---------------- | --------------------------------------------- | ----------------------------------------- |
| **Array / List** | Fixed/variable size; indexed access           | `append()`, `pop()`, `insert()`, `sort()` |
| **Stack**        | LIFO (Last-In-First-Out)                      | `append()`, `pop()`, `[-1]` (peek)        |
| **Queue**        | FIFO (First-In-First-Out)                     | `append()`, `pop(0)` or use `deque()`     |
| **Deque**        | Double-ended queue                            | `appendleft()`, `popleft()`, `extend()`   |
| **Linked List**  | Nodes linked with pointers (manual in Python) | Custom implementation using classes       |

---

### 🔸 Example: Array/List

```python
arr = [10, 20, 30]
arr.append(40)      # [10, 20, 30, 40]
arr.pop()           # [10, 20, 30]
```

---

### 🔸 Example: Stack

```python
stack = []
stack.append(1)
stack.append(2)
stack.pop()         # removes 2
```

---

### 🔸 Example: Queue (with deque)

```python
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()     # removes 1
```

---

### 🔸 Example: Custom Linked List

```python
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
```

---

#Algorithm 