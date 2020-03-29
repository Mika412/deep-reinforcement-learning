# Project report
Author: Mykhaylo Marfeychuk
## Learning algorithm

The solution uses the DDPG algorithm previously provided in the for the pendulum exercise. Each network in, actor and critic, have 2 fully-connected hidden layers layers with 128 neurons each.

Parameters used in DQN algorithm:

- Learning rate: 0.001
- Mini-batches: 256
- Replay Buffer: 100000
- Discount: 0.9
- Sigma: 0.1
- Tau: 0.001

## Results

![results](p2_navigation/scores.png)

```
Episode 100 	Average score:  1.15
Episode 200 	Average score:  5.15
Episode 300 	Average score:  7.89
Episode 400 	Average score:  10.92
Episode 471 	Average score:  13.08
Environment solved in  371 episodes!	Average Score:  13.08
Episode 473 	Average score:  13.18
Environment solved in  373 episodes!	Average Score:  13.18
Episode 474 	Average score:  13.22
Environment solved in  374 episodes!	Average Score:  13.22
Episode 475 	Average score:  13.23
Environment solved in  375 episodes!	Average Score:  13.23
Episode 476 	Average score:  13.29
Environment solved in  376 episodes!	Average Score:  13.29
Episode 478 	Average score:  13.30
Environment solved in  378 episodes!	Average Score:  13.30
Episode 480 	Average score:  13.39
Environment solved in  380 episodes!	Average Score:  13.39
Episode 482 	Average score:  13.40
Environment solved in  382 episodes!	Average Score:  13.40
Episode 484 	Average score:  13.44
Environment solved in  384 episodes!	Average Score:  13.44
Episode 486 	Average score:  13.46
Environment solved in  386 episodes!	Average Score:  13.46
Episode 487 	Average score:  13.50
Environment solved in  387 episodes!	Average Score:  13.50
Episode 490 	Average score:  13.51
Environment solved in  390 episodes!	Average Score:  13.51
Episode 491 	Average score:  13.53
Environment solved in  391 episodes!	Average Score:  13.53
Episode 492 	Average score:  13.55
Environment solved in  392 episodes!	Average Score:  13.55
Episode 493 	Average score:  13.65
Environment solved in  393 episodes!	Average Score:  13.65
Episode 494 	Average score:  13.71
Environment solved in  394 episodes!	Average Score:  13.71
Episode 495 	Average score:  13.78
Environment solved in  395 episodes!	Average Score:  13.78
Episode 496 	Average score:  13.79
Environment solved in  396 episodes!	Average Score:  13.79
Episode 497 	Average score:  13.81
Environment solved in  397 episodes!	Average Score:  13.81
Episode 498 	Average score:  13.82
Environment solved in  398 episodes!	Average Score:  13.82
Episode 500 	Average score:  13.80
Episode 502 	Average score:  13.84
Environment solved in  402 episodes!	Average Score:  13.84
Episode 509 	Average score:  13.92
Environment solved in  409 episodes!	Average Score:  13.92
Episode 510 	Average score:  14.04
Environment solved in  410 episodes!	Average Score:  14.04
Episode 511 	Average score:  14.06
Environment solved in  411 episodes!	Average Score:  14.06
Episode 512 	Average score:  14.09
Environment solved in  412 episodes!	Average Score:  14.09
Episode 514 	Average score:  14.10
Environment solved in  414 episodes!	Average Score:  14.10
Episode 515 	Average score:  14.19
Environment solved in  415 episodes!	Average Score:  14.19
Episode 516 	Average score:  14.20
Environment solved in  416 episodes!	Average Score:  14.20
Episode 519 	Average score:  14.21
Environment solved in  419 episodes!	Average Score:  14.21
Episode 521 	Average score:  14.27
Environment solved in  421 episodes!	Average Score:  14.27
Episode 526 	Average score:  14.29
Environment solved in  426 episodes!	Average Score:  14.29
Episode 527 	Average score:  14.37
Environment solved in  427 episodes!	Average Score:  14.37
Episode 528 	Average score:  14.39
Environment solved in  428 episodes!	Average Score:  14.39
Episode 529 	Average score:  14.42
Environment solved in  429 episodes!	Average Score:  14.42
Episode 531 	Average score:  14.43
Environment solved in  431 episodes!	Average Score:  14.43
Episode 533 	Average score:  14.44
Environment solved in  433 episodes!	Average Score:  14.44
Episode 534 	Average score:  14.52
Environment solved in  434 episodes!	Average Score:  14.52
Episode 535 	Average score:  14.59
Environment solved in  435 episodes!	Average Score:  14.59
Episode 536 	Average score:  14.60
Environment solved in  436 episodes!	Average Score:  14.60
Episode 600 	Average score:  14.11
Episode 700 	Average score:  14.02
Episode 800 	Average score:  14.10
Episode 900 	Average score:  13.22
Episode 1000 	Average score:  13.37
```
## Ideas for future work

1. Automatic hyperparamter tuning
2. Shared network between actor and critic
3. PPO
