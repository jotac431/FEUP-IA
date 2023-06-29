from gym.envs.registration import register

register(
    id='gekitai-env-v0',
    entry_point='gym_gekitai.envs:gekitai_env',
)