#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum


# 状態クラス
class State():
    def __init__(self, row=-1, column=-1):
        self.row = row
        self.column = column
        
    def __repr__(self):
        return '<State: [{}, {}]>'.format(self.row, self.column)
        
    def clone(self):
        return State(self.row, self.column)
        
    def __hash__(self):
        return hash((self.row, self.column))
        
    def __eq__(self, other):
        return self.row == other.row and self.column == other.column
        
# 行動クラス
class Action(Enum):
    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2
    
# 環境クラス
class Environment():
    def __init__(self, grid, move_prob=0.8):
        # grid is 2d-array. Its values are treated as an attribute.
        # Kinds of attribute is following.
        #  0: ordinary cell
        # -1: damage cell (game end)
        #  1: reward cel (game end)
        #  9: block cell (can't locate agent)
        self.grid = grid
        self.agent_state = State()
        
        # Default reward is minus. Just like a poison swamp.
        # It means the agent has to reach the goal fast!
        self.default_reward = -0.04
        
        # Agent can move to a selected direction in move_prob.
        # It means the agent will move different direction
        # in (1 - move_prob)
        self.move_prob = move_prob
        self.reset()
        
    @property
    def row_length(self):
        return len(self.grid)
        
    @property
    def column_length(self):
        return len(self.grid[0])
        
    @property
    def actions(self):
        return [Action.UP, Action.DOWN, ACTION.LEFT, Action.RIGHT]
        
    @property
    def states(self):
        states =[]
        for row in range(self.row_length):
            for column in range(self.column_length):
                # Block cells are not included to the state
                if self.grid[row][column] != 9:
                    # Create State instance for each cell
                    states.append(State(row, column))
        return states
        
    def transit_func(self, state, action):
        tansition_probs = {}
        if not self.can_action_at(state):
            # Already on the terminal cell.
            return transition_probs
            
        opposite_direction = Action(action.value * -1)
        
        for a in self.actions:
            prob = 0
            if a == action:
                prob = self.move_prob
            elif a != opposite_direction:
                prob = (1 - self.move_prob) / 2
                
            next_state = self._move(state, a)
            if next_state not in transition_probs:
                transition_probs[next_state] = prob
            else:
                transition_probs[next_state] += prob
                
        return transition_probs
        
    def can_action_at(self, state):
        if self.grid[state.row][state.column] == 0:
            return True
        else:
            return False
            
    def _move(self, state, action):
        if not self.can_action_at(state):
            raise Exception("Can't move from here!")
            
        next_state = state.clone()

if __name__ == '__main__':
    
