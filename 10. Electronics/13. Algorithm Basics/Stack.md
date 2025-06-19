### 🔹 Stack (Python)

A **stack** is a **LIFO (Last In, First Out)** data structure. Python does not have a built-in `Stack` type, but it can be implemented using **lists** or the **`collections.deque`** module.

---

### 🔸 Basic Stack Operations using `list`

```python
stack = []

# Push
stack.append(10)
stack.append(20)

# Pop
item = stack.pop()    # returns 20

# Peek (top element)
top = stack[-1]       # returns 10

# Check if empty
is_empty = len(stack) == 0
```

---

### 🔹 Major Stack-Related Functions (using `list`)

| Operation | Function / Expression | Description                          |
| --------- | --------------------- | ------------------------------------ |
| Push      | `stack.append(x)`     | Add element `x` to the top           |
| Pop       | `stack.pop()`         | Remove and return top element        |
| Peek      | `stack[-1]`           | View the top element without popping |
| Size      | `len(stack)`          | Number of elements in stack          |
| Is Empty  | `len(stack) == 0`     | Check if stack is empty              |

---

### 🔸 Stack Using `collections.deque` (Faster)

```python
from collections import deque

stack = deque()

stack.append("a")   # push
stack.pop()         # pop
```

---

### 🔸 Custom Stack Class Example

```python
class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)
    
    def pop(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]
    
    def is_empty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)
```

---

#Algorithm