### 🔹 Dijkstra’s Algorithm

Finds **shortest paths** from a source node to all other nodes in a **weighted graph with non-negative edge weights**.

---

### 🔸 Algorithm Steps

1. Set distance to source as `0`, all others as `infinity`.
2. Use a **priority queue** (min-heap) to pick the node with the smallest tentative distance.
3. For each neighbor, calculate `new_distance = current_distance + edge_weight`.
4. If `new_distance` is smaller, update the distance.
5. Repeat until all nodes are visited or queue is empty.

---

### 🔹 Example Code (Python)

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

---

### 🔸 Example Graph

```python
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

print(dijkstra(graph, 'A'))
```

**Output:**

```
{'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

---

### 💡 Key Concepts

* **Priority queue (min-heap)** for efficient node selection.
* **Greedy algorithm** choosing the shortest known path at each step.
* **Relaxation**: update shortest paths dynamically.
---

#Algorithm #Queue #Heap