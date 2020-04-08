# Project report
Author: Mykhaylo Marfeychuk
## Learning algorithm
Actor-critic methods use two components, the actor which is a neural network which updates the policy and the critic which is another neural network which evaluates the policy being learned which is, in turn, used to train the actor. Generally the algorithm uses policy-based methods like REINFORCE, which uses a Monte-Carlo estimate and TD estimates.

Deep Deterministic Policy Gradient (DDPG) is a variation of the Actor Critic Methods. The actor produces a deterministic policy instead of the usual stochastic policy and the critic evaluates the deterministic policy. The critic is updated using the TD-error and the actor is trained using the deterministic policy gradient algorithm.

The solution uses a DDPG implementation provided in the pendulum exercise. Each network in, actor and critic, have 2 fully-connected hidden layers layers with 128 neurons each.

Parameters used in DQN algorithm:

- Learning rate: 0.001
- Mini-batches: 256
- Replay Buffer: 100000
- Discount: 0.9
- Weight decay: 0.000001
- Sigma: 0.1
- Tau: 0.001

## Results

![results](scores.png)

```
Episode 100	Average Score: 11.86
Episode 151	Average Score: 30.26
Environment solved in 151 episodes!	Average Score: 30.26
```
## Ideas for future work

1. Automatic hyperparamter tuning
2. Shared network between actor and critic
3. PPO
