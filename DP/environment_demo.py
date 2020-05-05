#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from environment import Environment
import time
import os

class Agent():
    def __init__(self, env):
        self.actions = env.actions

    def policy(self, state):
        return random.choice(self.actions)

def main():
    # Make grid environment.
    grid = [
        [0, 0, 0, 1],
        [0, 9, 0, -1],
        [0, 0, 0, 0]
    ]
    grid_disp = [
        [0, 0, 0, 1],
        [0, 9, 0, -1],
        [0, 0, 0, 0]
    ]
    env = Environment(grid)
    agent = Agent(env)

    # Try 10 game.
    for i in range(10):
        # Initialize position of agent.
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = agent.policy(state)
            next_state, reward, done = env.step(action)
            total_reward += reward
            state = next_state
            #os.system('cls')
            print('{}, {}'.format(state.column, state.row))
            grid_disp[state.column][state.row] = 'x'
            print(*grid_disp, sep='\n')
            time.sleep(1)
            grid_disp[state.column][state.row] = grid[state.column][state.row]

        print('Episode {}: Agent gets {} reward.'.format(i, total_reward))

if __name__ == '__main__':
    main()
