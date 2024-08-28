import gym
from gym import spaces
import numpy as np

class TwoTokenEnv(gym.Env):
    def __init__(self):
        super(TwoTokenEnv, self).__init__()
        
        # Observation space: Prices of the two tokens and their supply
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(4,), dtype=np.float32)
        
        # Action space: Buy/Sell actions for both tokens
        self.action_space = spaces.Box(low=-1, high=1, shape=(2,), dtype=np.float32)
        
        # Initial conditions
        self.token1_price = 1.0
        self.token2_price = 1.0
        self.token1_supply = 1000
        self.token2_supply = 1000
        self.time_step = 0
        
    def reset(self):
        # Reset the environment to the initial state
        self.token1_price = 1.0
        self.token2_price = 1.0
        self.token1_supply = 1000
        self.token2_supply = 1000
        self.time_step = 0
        return np.array([self.token1_price, self.token2_price, self.token1_supply, self.token2_supply])
    
    def step(self, action):
        # Unpack action
        token1_action, token2_action = action
        
        # Adjust token supplies based on actions
        self.token1_supply += token1_action * 10  # Scale actions to make an impact
        self.token2_supply += token2_action * 10
        
        # Simulate price dynamics based on supply and demand
        self.token1_price = 1000 / self.token1_supply
        self.token2_price = 1000 / self.token2_supply
        
        # Smooth appreciation factor
        self.token1_price *= 1.001
        self.token2_price *= 1.001
        
        # Reward is based on price stability and controlled appreciation
        reward = -abs(self.token1_price - 1) - abs(self.token2_price - 1)
        
        # Time step increment
        self.time_step += 1
        done = self.time_step >= 100
        
        return np.array([self.token1_price, self.token2_price, self.token1_supply, self.token2_supply]), reward, done, {}
    
    def render(self, mode='human'):
        print(f"Token1 Price: {self.token1_price}, Token2 Price: {self.token2_price}, "
              f"Token1 Supply: {self.token1_supply}, Token2 Supply: {self.token2_supply}")
