### 🔹 List (Python)

A **list** in Python is an **ordered, mutable** collection of elements. Lists can contain any data type and allow duplicates.

---

### 🔸 Creating a List

```python
my_list = [1, 2, 3, "apple", True]
```

---

### 🔹 Major Python List Functions / Methods

| Function / Method  | Description                                         | Example                             |
| ------------------ | --------------------------------------------------- | ----------------------------------- |
| `append(x)`        | Add item `x` to the end of the list                 | `my_list.append(4)`                 |
| `extend(iterable)` | Add all elements from `iterable` to the end         | `my_list.extend([5, 6])`            |
| `insert(i, x)`     | Insert `x` at index `i`                             | `my_list.insert(1, "banana")`       |
| `remove(x)`        | Remove first occurrence of value `x`                | `my_list.remove("apple")`           |
| `pop([i])`         | Remove and return item at index `i` (default: last) | `my_list.pop()` or `my_list.pop(2)` |
| `index(x)`         | Return first index of value `x`                     | `my_list.index(3)`                  |
| `count(x)`         | Count occurrences of `x`                            | `my_list.count("apple")`            |
| `sort()`           | Sort the list in-place (ascending by default)       | `my_list.sort()`                    |
| `reverse()`        | Reverse the elements of the list in-place           | `my_list.reverse()`                 |
| `copy()`           | Return a shallow copy of the list                   | `copy_list = my_list.copy()`        |
| `clear()`          | Remove all elements from the list                   | `my_list.clear()`                   |
| `len()`            | Get the number of items in the list                 | `len(my_list)`                      |
| `in`               | Check if an item exists in the list                 | `'apple' in my_list`                |
| `list()`           | Create a list from an iterable                      | `list("abc")  # ['a', 'b', 'c']`    |

---

### 🔸 Access and Modify Elements

```python
x = my_list[0]        # Access first element
my_list[1] = "orange" # Modify second element
```

---

### 🔸 Looping Over a List

```python
for item in my_list:
    print(item)
```

---

#Algorithm 