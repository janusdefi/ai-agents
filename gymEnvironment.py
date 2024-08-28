import gym
from gym import spaces

class DeFiTokenEnv(gym.Env):
    def __init__(self, data):
        super(DeFiTokenEnv, self).__init__()
        
        self.data = data
        self.current_step = 0
        self.max_steps = len(data) - 1
        
        # Observation space: Includes both token prices, supplies, and additional indicators
        self.observation_space = spaces.Box(low=0, high=1, shape=(data.shape[1],), dtype=np.float32)
        
        # Action space: Adjust the supplies (or buy/sell ratios) of the two tokens
        self.action_space = spaces.Box(low=-1, high=1, shape=(2,), dtype=np.float32)

    def reset(self):
        self.current_step = 0
        return self.data[self.current_step]

    def step(self, action):
        self.current_step += 1
        if self.current_step >= self.max_steps:
            self.current_step = self.max_steps

        # Simulate the impact of actions on the token ecosystem
        # Action 0: Adjust supply of token 1, Action 1: Adjust supply of token 2
        token1_adjustment = action[0] * 10
        token2_adjustment = action[1] * 10

        # Get the next state
        next_state = self.data[self.current_step]

        # Calculate rewards based on the goals: low volatility, stable price appreciation, and high rewards
        reward = self.calculate_reward(next_state, token1_adjustment, token2_adjustment)
        
        done = self.current_step == self.max_steps

        return next_state, reward, done, {}

    def calculate_reward(self, state, token1_adjustment, token2_adjustment):
        # Example reward calculation
        token1_price = state[0]
        token2_price = state[1]

        # Reward for smooth price appreciation
        appreciation_reward = (token1_price + token2_price) / 2
        
        # Reward for low volatility
        volatility_penalty = abs(token1_price - 1) + abs(token2_price - 1)
        
        # Reward for generating rewards (which might be a function of price stability)
        reward_generation = appreciation_reward - volatility_penalty
        
        return reward_generation
    
    def render(self, mode='human'):
        print(f"Step: {self.current_step}, Token1 Price: {self.data[self.current_step][0]}, "
              f"Token2 Price: {self.data[self.current_step][1]}")
