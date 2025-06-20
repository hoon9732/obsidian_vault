### ✅ Full Python Code

```python
# Define the Tree Node class
class TaskNode:
    def __init__(self, task):
        self.task = task
        self.left = None
        self.right = None

# Preorder traversal: Root → Left → Right
def preorder(node):
    if node:
        print(node.task, end=' ')
        preorder(node.left)
        preorder(node.right)

# Inorder traversal: Left → Root → Right
def inorder(node):
    if node:
        inorder(node.left)
        print(node.task, end=' ')
        inorder(node.right)

# Postorder traversal: Left → Right → Root
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.task, end=' ')

# Example tree structure for the drone task
#       A
#      / \
#     B   C
#    / \   \
#   D   E   F

root = TaskNode('A')
root.left = TaskNode('B')
root.right = TaskNode('C')
root.left.left = TaskNode('D')
root.left.right = TaskNode('E')
root.right.right = TaskNode('F')

# Output each traversal
print("Preorder Traversal:")
preorder(root)
print("\nInorder Traversal:")
inorder(root)
print("\nPostorder Traversal:")
postorder(root)
```

---

### 🔄 Output Example

```
Preorder Traversal:
A B D E C F
Inorder Traversal:
D B E A C F
Postorder Traversal:
D E B F C A
```

---
#Algorithm #Tree