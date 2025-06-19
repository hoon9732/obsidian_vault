### 🔹 Priority Queue

A **priority queue** is a **queue where elements are dequeued based on priority**, not insertion order. Higher priority items come out before lower priority ones.

---

### 🔸 Key Properties

* Each element has a **value** and a **priority**
* Implemented efficiently using a **heap**

  * In Python, the `heapq` module implements a **min-heap**
  * For max-priority behavior, invert the priority

---

### 🔹 Implementation Using `heapq`

```python
import heapq

pq = []  # priority queue list (heap)

# Push: (priority, value)
heapq.heappush(pq, (1, "low"))
heapq.heappush(pq, (0, "high"))
heapq.heappush(pq, (5, "very low"))

# Pop: returns the item with the lowest priority number
item = heapq.heappop(pq)  # (0, 'high')
```

---

### 🔸 Custom Object with Priority

```python
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    
    def __lt__(self, other):  # define less-than for heapq
        return self.priority < other.priority

pq = []
heapq.heappush(pq, Task("clean", 2))
heapq.heappush(pq, Task("write report", 1))
heapq.heappush(pq, Task("sleep", 5))

task = heapq.heappop(pq)
print(task.name)  # "write report"
```

---

### 🔸 Max-Priority Queue (Invert Priority)

```python
heapq.heappush(pq, (-priority, value))
```

---

### 🔹 Key Functions (from `heapq`)

| Function               | Description                           |
| ---------------------- | ------------------------------------- |
| `heappush(heap, x)`    | Push element `x` onto the heap        |
| `heappop(heap)`        | Pop and return smallest element       |
| `heapify(list)`        | Convert list into a heap in-place     |
| `heappushpop(heap, x)` | Push then pop in one step (efficient) |

---

#Algorithm #Queue