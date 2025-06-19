### 🔹 Hash

A **hash** is a function that **maps data to a fixed-size value** (hash value or hash code). It is used in **hash tables**, **dictionaries**, and for **data integrity**, **security**, etc.

---

### 🔸 Hash Function Characteristics

* Deterministic: same input → same output
* Fast computation
* Uniform distribution
* Irreversible (for cryptographic hash functions)

---

### 🔹 In Python

#### 🔸 Built-in `hash()` Function

Returns an integer hash value for hashable objects.

```python
print(hash("apple"))     # e.g., 182191511380666284
print(hash(42))          # hash of an integer
```

#### 🔸 Dictionary (Hash Table)

Python's `dict` uses a **hash table** internally.

```python
d = {"a": 1, "b": 2}
print(hash("a"))         # hash used internally to index key "a"
```

---

### 🔹 Custom Object Hashing

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

p1 = Person("Alice")
p2 = Person("Alice")
print(hash(p1) == hash(p2))  # True
```

---

### 🔸 Hash Collision

When two inputs produce the same hash. Handled in hash tables using **chaining** or **open addressing**.

---

### 🔸 Cryptographic Hashes (via `hashlib`)

```python
import hashlib

m = hashlib.sha256()
m.update(b"hello")
print(m.hexdigest())  # 2cf24dba5f... (64 hex chars)
```

---

### 🔹 Common Hash Functions

| Name     | Description                            |
| -------- | -------------------------------------- |
| `hash()` | Built-in, not cryptographically secure |
| `md5`    | Fast, insecure (for checksums only)    |
| `sha256` | Secure, widely used in cryptography    |

---

#Algorithm #Hash