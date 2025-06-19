### 🔹 RRT (Rapidly-exploring Random Tree)

**RRT** is a sampling-based algorithm used for **path planning** in high-dimensional or continuous spaces. It incrementally builds a tree by randomly sampling points and connecting them toward the tree.

---

### 🔸 Algorithm Steps

1. Initialize tree with the **start node**.
2. **Randomly sample** a point in the space.
3. Find the **nearest node** in the tree to this random point.
4. **Steer** from the nearest node towards the random point by a fixed step size.
5. If the path is **collision-free**, add the new point to the tree.
6. Repeat until the **goal is reached** or max iterations are met.

---

### 🔹 Example Code (2D RRT Simplified, no obstacles)

```python
import random
import math
import matplotlib.pyplot as plt

class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

def distance(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)

def steer(from_node, to_point, step_size):
    theta = math.atan2(to_point[1] - from_node.y, to_point[0] - from_node.x)
    return Node(from_node.x + step_size * math.cos(theta),
                from_node.y + step_size * math.sin(theta),
                from_node)

def rrt(start, goal, bounds, step_size=1.0, max_iter=1000):
    tree = [Node(*start)]

    for _ in range(max_iter):
        rand_point = (random.uniform(bounds[0], bounds[2]),
                      random.uniform(bounds[1], bounds[3]))
        nearest = min(tree, key=lambda n: math.hypot(n.x - rand_point[0], n.y - rand_point[1]))
        new_node = steer(nearest, rand_point, step_size)
        tree.append(new_node)

        if distance(new_node, Node(*goal)) < step_size:
            goal_node = Node(*goal, parent=new_node)
            tree.append(goal_node)
            return tree, goal_node  # Success

    return tree, None  # Failed to reach goal

def draw_path(goal_node):
    path = []
    node = goal_node
    while node:
        path.append((node.x, node.y))
        node = node.parent
    path.reverse()
    xs, ys = zip(*path)
    plt.plot(xs, ys, '-r')

def draw_tree(tree):
    for node in tree:
        if node.parent:
            plt.plot([node.x, node.parent.x], [node.y, node.parent.y], '-g')

start = (0, 0)
goal = (9, 9)
bounds = (0, 0, 10, 10)

tree, goal_node = rrt(start, goal, bounds)
draw_tree(tree)
if goal_node:
    draw_path(goal_node)
plt.plot(start[0], start[1], 'bo')  # Start
plt.plot(goal[0], goal[1], 'ro')    # Goal
plt.axis("equal")
plt.show()
```

---

### 💡 Key Concepts

* **Sampling-based**: random point generation in space.
* **Tree growth**: biased toward unexplored regions.
* **Steer**: controlled step toward random point.
* **No global map** required—suitable for complex spaces.
---
#Algorithm #Tree