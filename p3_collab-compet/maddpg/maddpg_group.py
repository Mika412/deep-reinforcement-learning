import numpy as np
import random
import copy
from collections import namedtuple, deque

from .maddpg_model import Actor, Critic
from .maddpg_agent import ReplayBuffer, Agent

import torch
import torch.nn.functional as F
import torch.optim as optim

BUFFER_SIZE = int(1e5)         # replay buffer size
BATCH_SIZE = 256               # minibatch size
GAMMA = 0.9                    # discount factor
TAU = 1e-3                     # for soft update of target parameters
LR_ACTOR = 1e-3                # learning rate of the actor 
LR_CRITIC = 1e-3               # learning rate of the critic
WEIGHT_DECAY = 1e-6            # L2 weight decay

SIGMA = 0.1                    # for OUNoise
GPU = 2                        # GPU ID for multi-GPU machines

device = torch.device(f"cuda:{GPU}" if torch.cuda.is_available() else "cpu")

class Group():
    def __init__(self, num_agents, state_size, action_size, random_seed):
        self.memory = ReplayBuffer(action_size, BUFFER_SIZE, BATCH_SIZE, random_seed)
        self.agents = [Agent(self.memory, state_size, action_size, random_seed) for _ in range(num_agents)]
        
    def reset_noise(self):
        for agent in self.agents:
            agent.reset()
        
    def step(self, states, actions, rewards, next_states, dones):
        for agent, state, action, reward, next_state, done in \
        zip(self.agents, states, actions, rewards, next_states, dones):
            agent.step(state, action, reward, next_state, done)
        
    def act(self, states):
        actions = list()
        for agent, state in zip(self.agents, states):
            actions.append(agent.act(state))
        return actions
    
    def checkpoint(self):
        return [{
            'actor': agent.actor_local.state_dict(),
            'critic': agent.critic_local.state_dict()
        } for agent in self.agents]
