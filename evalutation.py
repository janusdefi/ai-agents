from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

obs = env.reset()
for i in range(100):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
