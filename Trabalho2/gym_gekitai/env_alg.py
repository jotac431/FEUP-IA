import random
import gym
import numpy as np
import gym_gekitai.envs.GekitaiEnv
from enum import Enum

class EpsilonDecay(Enum):
    Exponential = "exp"
    Linear = "linear"
    NoDecay = "none"

# Base algorithm class
# Contains all parameters
class EnvAlg():

    def __init__(self,
                env="Gekitai-4x4-1",
                max_episodes=100,
                learning_rate=0.8,
                max_steps=99,
                gamma=0.95,
                starting_epsilon=0.9,
                ending_epsilon=0.01,
                decay_rate=0.001,
                epsilon_decay=EpsilonDecay.Exponential):

        self.env = gym.make(env)

        # Calculates action size
        self.action_size = self.env.action_space.__sizeof__

        print(f"Action size = {self.action_size}")
    
        self.reset_qtable()

        self.max_episodes = max_episodes # Total episodes
        self.learning_rate = learning_rate  # Learning rate
        self.max_steps = max_steps  # Max steps per episode
        self.gamma = gamma  # Discounting rate

        # Exploration
        self.starting_epsilon = starting_epsilon
        self.ending_epsilon = ending_epsilon
        self.decay_rate = decay_rate
        self.epsilon_decay = epsilon_decay
    
    def print_qtable(self):
        for key in self.qtable:
            print(f"{key}: [", end="")
            
            for value in self.qtable[key]:
                if value != 0:
                    action = np.where(self.qtable[key] == value)
                    print(f"{action[0][0]}: {value}", end=" ")

            print("]", end="\n")

    def reset_qtable(self):
        self.qtable = { }

    def import_qtable(self, qtable):
        self.qtable = qtable

    def export_qtable(self):
        return self.qtable