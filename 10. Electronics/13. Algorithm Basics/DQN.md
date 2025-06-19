### 🔹 DQN (Deep Q-Network)

**DQN** extends Q-learning by using a **neural network** to approximate the Q-function $Q(s, a)$ instead of using a table. It's suitable for high-dimensional or continuous state spaces (e.g., images, sensor data).

---

### 🔸 Core Components

1. **Q-Network**: neural network that predicts $Q(s, a)$
2. **Replay Buffer**: stores experience tuples $(s, a, r, s', done)$ for training
3. **Target Network**: a copy of Q-network used for stable target calculation
4. **ε-greedy**: exploration strategy

---

### 🔹 Q-Learning Target (used to train NN)

$$
y = r + \gamma \cdot \max_{a'} Q_{\text{target}}(s', a')
$$

$$
\text{Loss} = \left( y - Q(s, a) \right)^2
$$

---

### 🔹 Simplified Example Code (DQN on Toy Environment)

```python
import torch
import torch.nn as nn
import torch.optim as optim
import random
import numpy as np
from collections import deque

class DQN(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.ReLU(),
            nn.Linear(64, action_dim)
        )
    
    def forward(self, x):
        return self.fc(x)

# Parameters
state_dim = 4    # e.g., for CartPole
action_dim = 2
gamma = 0.99
epsilon = 0.1
lr = 1e-3
batch_size = 32
buffer = deque(maxlen=10000)

# Initialize networks
q_net = DQN(state_dim, action_dim)
target_net = DQN(state_dim, action_dim)
target_net.load_state_dict(q_net.state_dict())
optimizer = optim.Adam(q_net.parameters(), lr=lr)

# Experience replay sample
def sample_batch():
    minibatch = random.sample(buffer, batch_size)
    s, a, r, s_, d = zip(*minibatch)
    return (torch.tensor(s, dtype=torch.float),
            torch.tensor(a),
            torch.tensor(r, dtype=torch.float),
            torch.tensor(s_, dtype=torch.float),
            torch.tensor(d, dtype=torch.float))

# Training step
def train_step():
    if len(buffer) < batch_size:
        return
    states, actions, rewards, next_states, dones = sample_batch()
    
    q_values = q_net(states).gather(1, actions.unsqueeze(1)).squeeze()
    with torch.no_grad():
        max_q_next = target_net(next_states).max(1)[0]
        targets = rewards + gamma * max_q_next * (1 - dones)
    
    loss = nn.MSELoss()(q_values, targets)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

---

### 💡 Key Concepts

* **Function approximation**: Q-values via neural networks.
* **Replay buffer**: breaks correlation in data.
* **Target network**: stabilizes learning.
* **Mini-batch gradient descent**: used instead of one-step updates.
---
#Algorithm #NN 