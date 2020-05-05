#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import random
import pdb

# 状態sにおける価値を算出する価値関数（報酬が状態のみで決まる場合（R(s)の場合））
def V(s, gamma=0.99):
    V = R(s) + gamma * max_V_on_next_state(s)
    print('V='+str(V))
    return V

# 状態sにおける報酬を算出する報酬関数（状態のみで報酬が決まる場合）
# エピソード終了時点で1か-1の報酬、それ以外は0を返す
def R(s):
    if s == 'happy_end':
        return 1
    elif s == 'bad_end':
        return -1
    else:
        return 0

# 遷移先の価値を遷移確率で期待値をとって算出し、最大の価値を返す
def max_V_on_next_state(s):
    # If game end, expected value is 0.
    if s in ['happy_end', 'bad_end']:
        return 0

    actions = ['up', 'down']
    values = []
    # すべての行動でvを計算し、値が最大になる価値を返す
    for a in actions:
        print('state, a = {}, {}'.format(s, a))
        transition_probs = transit_func(s, a)
        print('transition_probs = {}'.format(transition_probs))
        v = 0
        for next_state in transition_probs:
            # 各状態での遷移確率を取り出す
            prob = transition_probs[next_state]
            # 遷移確率×遷移先の価値
            print('next_state={}'.format(next_state))
            v += prob * V(next_state)
        print('v=' + str(v))
        values.append(v)
        print('values={}'.format(values))
        #print(v)
    print('values_Return={}'.format(values))
    breakpoint()
    return max(values)

# 遷移関数
def transit_func(s, a):
    '''
    Make next state by adding action str to state.
    ex : (s = 'state', a = 'up') => 'state_up'
         (s = 'state_up', a = 'down') => 'state_up_down'
    '''
    
    actions = s.split('_')[1:]  # 接続したアクションを分割する
    LIMIT_GAME_COUNT = 5        # アクション回数の上限
    HAPPY_END_BORDER = 4        # 
    MOVE_PROB = 0.9             # 遷移確率
    
    # 文字列を'_'で接続する
    def next_state(state, action):
        return '_'.join([state, action])
        
    if len(actions) == LIMIT_GAME_COUNT:
    # アクション回数が5回に達した場合
        # upの数をカウント
        up_count = sum([1 if a == 'up' else 0 for a in actions])
        # upがHAPPY_END_BORDER以上であればhappy_end、それ以外はbad_endを状態に入れる
        state = 'happy_end' if up_count >= HAPPY_END_BORDER else 'bad_end'
        prob = 1.0
        # 終了状態と遷移確率(ただし1.0)を辞書型で返却
        return {state: prob}
    else:
    # アクション回数が5回に達していない場合
        opposite = 'up' if a == 'down' else 'down'
        # 次の状態'state_up_down_up_...など'と遷移確率をセットで返却
        return {
            next_state(s, a): MOVE_PROB,
            next_state(s, opposite): 1 - MOVE_PROB
        }
        
# 実際の価値の計算
if __name__ == '__main__':
    print(V('state'))
    exit()
    print(V('state_up_up'))
    print(V('state_down_down'))