### 🔹 K-Means

**K-Means** is an **unsupervised clustering algorithm** that partitions data into **K clusters** by minimizing the **intra-cluster variance** (distance to cluster center).

---

### 🔸 Algorithm Steps

1. Initialize **K random centroids**.
2. **Assign** each point to the nearest centroid.
3. **Update** centroids by calculating the mean of all assigned points.
4. Repeat steps 2–3 until convergence (no change in assignments or centroids).

---

### 🔹 Example Code (Python)

```python
import numpy as np
import matplotlib.pyplot as plt

def k_means(X, k, max_iter=100):
    # Randomly initialize k centroids
    np.random.seed(42)
    centroids = X[np.random.choice(len(X), k, replace=False)]
    
    for _ in range(max_iter):
        # Assign points to nearest centroid
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)

        # Update centroids
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

        # Check for convergence
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    
    return labels, centroids
```

---

### 🔸 Example Usage

```python
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=300, centers=3, random_state=0)
labels, centers = k_means(X, k=3)

# Plotting
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=30)
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200)
plt.title("K-Means Clustering")
plt.show()
```

---

### 💡 Key Concepts

* **Centroid**: average of all points in a cluster.
* **Euclidean distance**: common metric to assign points.
* **Unsupervised**: no labeled data used.
---
#Algorithm