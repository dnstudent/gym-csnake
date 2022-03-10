from gym.envs.registration import register

register(
    id='csnake-v0',
    entry_point='gym_csnake.envs:CSnakeEnv',
)
