Sure! Let's start with **BFS**.

---

### 🔹 What is **BFS** (Breadth-First Search)?

**BFS** is a **graph traversal algorithm** that explores all the neighbors of a node before moving on to their neighbors. It works **level by level**, which makes it suitable for:

* Finding the **shortest path** in unweighted graphs
* Checking **connected components**
* Tree or graph **level-order traversal**

---

### 🔸 BFS Algorithm Steps:

1. Start from a source node.
2. Use a **queue** to track nodes to visit.
3. Use a **visited set** or list to avoid revisiting nodes.
4. While the queue is not empty:

   * Pop the front node.
   * Visit its unvisited neighbors and add them to the queue.

---

### 🔹 Example Code (Python)

Here's an example of BFS on an **unweighted graph** represented with an adjacency list:

```python
from collections import deque

def bfs(graph, start):
    visited = set()                # Keeps track of visited nodes
    queue = deque([start])         # Queue for BFS, initialized with start node

    while queue:
        node = queue.popleft()     # Pop the front node in the queue
        if node not in visited:
            print("Visited:", node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)  # Add unvisited neighbors to the queue
```

---

### 🔸 Example Graph:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')
```

**Output:**

```
Visited: A
Visited: B
Visited: C
Visited: D
Visited: E
Visited: F
```

---

### 💡 Key Concepts Used:

* **Graph**: Collection of nodes and edges
* **Queue (deque)**: Ensures FIFO processing
* **Visited set**: Prevents cycles/infinite loops
* **Adjacency list**: A common way to represent graphs in code

---

Let me know the next keyword you'd like explained with code!
#Algorithm #Graph