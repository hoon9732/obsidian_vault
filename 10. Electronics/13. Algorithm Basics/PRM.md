### 🔹 PRM (Probabilistic Roadmap)

**PRM** is a **sampling-based motion planning** algorithm used in static environments. It builds a **roadmap** of valid paths through random sampling and connects them into a graph.

---

### 🔸 Algorithm Steps

1. **Sample** N random collision-free points in the configuration space.
2. For each point, find its **k-nearest neighbors**.
3. Try to **connect** each pair with a direct path (usually a straight line), keeping only collision-free connections.
4. Store connections in a **graph**.
5. Use **graph search (e.g., Dijkstra)** to find a path from start to goal.

---

### 🔹 Example Code (2D PRM, no obstacles for simplicity)

```python
import random
import math
import matplotlib.pyplot as plt
from scipy.spatial import KDTree
from collections import defaultdict
import heapq

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def generate_samples(bounds, n):
    return [(random.uniform(bounds[0], bounds[2]), random.uniform(bounds[1], bounds[3])) for _ in range(n)]

def connect_nodes(samples, k):
    tree = KDTree(samples)
    graph = defaultdict(list)
    for i, point in enumerate(samples):
        distances, indices = tree.query(point, k+1)
        for j in indices[1:]:  # skip self
            p2 = samples[j]
            # Assume collision-free (no obstacles in this simplified example)
            graph[point].append(p2)
            graph[p2].append(point)
    return graph

def dijkstra(graph, start, goal):
    queue = [(0, start)]
    dist = {start: 0}
    prev = {start: None}
    visited = set()

    while queue:
        cost, current = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            alt = cost + distance(current, neighbor)
            if neighbor not in dist or alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current
                heapq.heappush(queue, (alt, neighbor))

    path = []
    node = goal
    while node:
        path.append(node)
        node = prev.get(node)
    path.reverse()
    return path

# Parameters
bounds = (0, 0, 10, 10)
n_samples = 100
k = 5
start = (0, 0)
goal = (9, 9)

# Generate roadmap
samples = generate_samples(bounds, n_samples)
samples += [start, goal]
graph = connect_nodes(samples, k)

# Find path
path = dijkstra(graph, start, goal)

# Plot
for node, neighbors in graph.items():
    for neighbor in neighbors:
        plt.plot([node[0], neighbor[0]], [node[1], neighbor[1]], 'g-', linewidth=0.5)
if path:
    xs, ys = zip(*path)
    plt.plot(xs, ys, 'r-', linewidth=2)
plt.plot(start[0], start[1], 'bo')  # Start
plt.plot(goal[0], goal[1], 'ro')    # Goal
plt.axis("equal")
plt.show()
```

---

### 💡 Key Concepts

* **Sampling**: random generation of collision-free nodes.
* **Roadmap**: graph of points and safe edges.
* **KNN**: k-nearest-neighbor connection strategy.
* **Graph search**: Dijkstra/A\* used after graph construction.
#Algorithm #