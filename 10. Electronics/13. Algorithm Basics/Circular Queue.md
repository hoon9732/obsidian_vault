### 🔹 Circular Queue

A **circular queue** is a **fixed-size FIFO** (First In, First Out) data structure where the last position connects back to the first, forming a **circle**. It efficiently uses memory by reusing empty spaces left by dequeued elements.

---

### 🔸 Key Concepts

* Uses a fixed-size list.
* Two pointers:

  * `front`: points to the first element
  * `rear`: points to the next insertion position
* Wraps around using modulo: `(index + 1) % size`

---

### 🔹 Implementation (Python)

```python
class CircularQueue:
    def __init__(self, k):
        self.q = [None] * k
        self.size = k
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, value):
        if self.is_full():
            return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return False
        self.q[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def peek_front(self):
        if self.is_empty():
            return None
        return self.q[self.front]

    def peek_rear(self):
        if self.is_empty():
            return None
        return self.q[(self.rear - 1 + self.size) % self.size]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size
```

---

### 🔸 Example Usage

```python
cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)  # full now
cq.dequeue()   # remove 1
cq.enqueue(4)  # adds to the place where 1 was
print(cq.q)    # [4, 2, 3]
```

---

#Algorithm #Queue