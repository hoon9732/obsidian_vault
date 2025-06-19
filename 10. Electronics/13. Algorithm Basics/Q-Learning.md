### 🔹 Q-Learning

**Q-Learning** is a **model-free reinforcement learning** algorithm used to learn the **optimal action-selection policy** for an agent interacting with an environment.

It learns a function:

$$
Q(s, a) \rightarrow \text{expected future reward of taking action } a \text{ in state } s
$$

---

### 🔸 Q-Learning Update Rule

$$
Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
$$

* $s$: current state
* $a$: action taken
* $r$: reward received
* $s'$: next state
* $\alpha$: learning rate
* $\gamma$: discount factor
* $Q(s, a)$: current Q-value
* $\max_{a'} Q(s', a')$: best estimated future reward

---

### 🔹 Example Code (Gridworld Q-learning)

```python
import numpy as np
import random

# Environment setup
n_states = 5  # simple 1D world: states 0–4
actions = [0, 1]  # 0 = left, 1 = right
q_table = np.zeros((n_states, len(actions)))
alpha = 0.1      # learning rate
gamma = 0.9      # discount factor
epsilon = 0.2    # exploration rate
episodes = 100

def step(state, action):
    if action == 0:
        next_state = max(0, state - 1)
    else:
        next_state = min(n_states - 1, state + 1)
    reward = 1 if next_state == n_states - 1 else 0
    return next_state, reward

# Q-learning loop
for _ in range(episodes):
    state = 0
    while state != n_states - 1:
        # ε-greedy action selection
        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = np.argmax(q_table[state])

        next_state, reward = step(state, action)

        # Q-value update
        best_next = np.max(q_table[next_state])
        q_table[state, action] += alpha * (reward + gamma * best_next - q_table[state, action])

        state = next_state
```

---

### 🔸 Final Q-table Output

```python
print(np.round(q_table, 2))
```

---

### 💡 Key Concepts

* **Q-table**: stores expected values for state-action pairs.
* **Exploration vs. Exploitation**: ε-greedy strategy balances trying new actions and choosing the best known one.
* **Model-free**: does not need to know transition probabilities.
---

#Algorithm #RL