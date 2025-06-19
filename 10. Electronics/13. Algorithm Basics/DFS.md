
---

### 🔹 What is **DFS** (Depth-First Search)?

**DFS** is a **graph traversal algorithm** that explores as far down a path as possible before backtracking. It dives deep into one branch before trying another. DFS can be implemented **recursively** or using a **stack**.

---

### 🔸 DFS Algorithm Steps:

1. Start from a source node.
2. Visit the node and mark it as visited.
3. For each unvisited neighbor, **recursively** perform DFS (or push onto a stack if using iterative DFS).

---

### 🔹 Example Code (Recursive DFS in Python)

```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in visited:
        print("Visited:", node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
```

---

### 🔹 Example Graph (Same as BFS):

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')
```

**Output:**

```
Visited: A
Visited: B
Visited: D
Visited: E
Visited: F
Visited: C
```

---

### 🔸 Iterative DFS (using stack)

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print("Visited:", node)
            visited.add(node)
            stack.extend(reversed(graph[node]))  # reverse to match recursive order
```

---

### 💡 Key Concepts Used:

* **Stack** (LIFO): Used in iterative DFS
* **Recursion**: Natural for tree/graph traversal
* **Visited set**: Prevents re-visiting
* **Adjacency list**: Graph representation

---

#Algorithm #Graph 