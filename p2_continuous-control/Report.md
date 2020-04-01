# Project report
Author: Mykhaylo Marfeychuk
## Learning algorithm

The solution uses the DDPG algorithm previously provided in the for the pendulum exercise. Each network in, actor and critic, have 2 fully-connected hidden layers layers with 128 neurons each.

Parameters used in DQN algorithm:

- Learning rate: 0.001
- Mini-batches: 256
- Replay Buffer: 100000
- Discount: 0.9
- Weight decay: 0.000001
- Sigma: 0.1
- Tau: 0.001

## Results

![results](p2_navigation/scores.png)

```
Episode 100	Average Score: 11.86
Episode 151	Average Score: 30.26
Environment solved in 151 episodes!	Average Score: 30.26
```
## Ideas for future work

1. Automatic hyperparamter tuning
2. Shared network between actor and critic
3. PPO
