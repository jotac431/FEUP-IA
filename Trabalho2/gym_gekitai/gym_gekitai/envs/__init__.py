from gym.envs.registration import register

register(
    id='Gekitai-4x4-1',
    entry_point='gym_gekitai.envs:GekitaiEnv',
    kwargs={'board_size': 4, 'game_mode': 2, 'difficulty': 2, 'player':1},
    max_episode_steps=2000
)