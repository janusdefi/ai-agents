#Janus Defi code to setup Reinforcement Learning for an AI agent to control price stability
#in a two token ecosystem
#using the Proximal Policy Optimization (PPO) algorithm 

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

# Create the environment
env = make_vec_env(lambda: TwoTokenEnv(), n_envs=1)

# Create the PPO model
model = PPO("MlpPolicy", env, verbose=1)

# Train the model
model.learn(total_timesteps=10000)
