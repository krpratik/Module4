# gridworkd_mdp.py - provides a full MDP specification for a 4x4 gridworld. 
# The Gridworld has a "single goal state", located in the upper/left and lower/right corners 
# of the grid.
import numpy as np
import copy as cp

def get_state_count():
    return 25

def get_available_actions(state):
    actions = ["right", "left", "down", "up"]
    # shuffled_actions = cp.copy(actions)
    # np.random.shuffle(shuffled_actions)
    return actions

def get_transitions(state, action):
    prob = 1
    next_state_num = next_state[(state, action)]
    if (next_state_num == 1):
        if (state == next_state_num):
            reward = 0
            trans=(next_state_num,reward,prob)
            return [trans]
        else :
            reward = 10
            trans=(next_state_num,reward,prob)
            return [trans]

    if (next_state_num == 3):
        if (state == next_state_num):
            reward = 0
            trans = (next_state_num,reward,prob)
            return [trans]
        else :
            reward = 5
            trans = (next_state_num,reward,prob)
            return [trans]

    elif (next_state_num != state):
        reward = 0
        trans = (next_state_num, reward, prob)
        return [trans]
    
    else :
        reward = -1
        trans = (next_state_num, reward, prob)
        return [trans]
    
    
def build_next_state_dictionary():
    next_state = {}
    next_state[(0, "left")] = 0
    next_state[(0, "up")] = 0
    next_state[(0, "right")] = 1
    next_state[(0, "down")] = 5

    next_state[(1, "left")] = 1
    next_state[(1, "up")] = 1
    next_state[(1, "right")] = 1
    next_state[(1, "down")] = 1

    next_state[(2, "left")] = 1
    next_state[(2, "up")] = 2
    next_state[(2, "right")] = 3
    next_state[(2, "down")] = 7

    next_state[(3, "left")] = 3
    next_state[(3, "up")] = 3
    next_state[(3, "right")] = 3
    next_state[(3, "down")] = 3

    next_state[(4, "left")] = 3
    next_state[(4, "up")] = 4
    next_state[(4, "right")] = 4
    next_state[(4, "down")] = 9

    next_state[(5, "left")] = 5
    next_state[(5, "up")] = 0
    next_state[(5, "right")] = 6
    next_state[(5, "down")] = 10

    next_state[(6, "left")] = 5
    next_state[(6, "up")] = 1
    next_state[(6, "right")] = 7
    next_state[(6, "down")] = 11

    next_state[(7, "left")] = 6
    next_state[(7, "up")] = 2
    next_state[(7, "right")] = 8
    next_state[(7, "down")] = 12

    next_state[(8, "left")] = 7
    next_state[(8, "up")] = 3
    next_state[(8, "right")] = 9
    next_state[(8, "down")] = 13

    next_state[(9, "left")] = 8
    next_state[(9, "up")] = 4
    next_state[(9, "right")] = 9
    next_state[(9, "down")] = 14

    next_state[(10, "left")] = 10
    next_state[(10, "up")] = 5
    next_state[(10, "right")] = 11
    next_state[(10, "down")] = 15

    next_state[(11, "left")] = 10
    next_state[(11, "up")] = 6
    next_state[(11, "right")] = 12
    next_state[(11, "down")] = 16

    next_state[(12, "left")] = 11
    next_state[(12, "up")] = 7
    next_state[(12, "right")] = 13
    next_state[(12, "down")] = 17

    next_state[(13, "left")] = 12
    next_state[(13, "up")] = 8
    next_state[(13, "right")] = 14
    next_state[(13, "down")] = 18

    next_state[(14, "left")] = 13
    next_state[(14, "up")] = 9
    next_state[(14, "right")] = 14
    next_state[(14, "down")] = 19

    next_state[(15, "left")] = 15
    next_state[(15, "up")] = 10
    next_state[(15, "right")] = 16
    next_state[(15, "down")] = 20

    next_state[(16, "left")] = 15
    next_state[(16, "up")] = 11
    next_state[(16, "right")] = 17
    next_state[(16, "down")] = 21

    next_state[(17, "left")] = 16
    next_state[(17, "up")] = 12
    next_state[(17, "right")] = 18
    next_state[(17, "down")] = 22
    
    next_state[(18, "left")] = 17
    next_state[(18, "up")] = 13
    next_state[(18, "right")] = 19
    next_state[(18, "down")] = 23

    next_state[(19, "left")] = 18
    next_state[(19, "up")] = 14
    next_state[(19, "right")] = 19
    next_state[(19, "down")] = 24

    next_state[(20, "left")] = 20
    next_state[(20, "up")] = 15
    next_state[(20, "right")] = 21
    next_state[(20, "down")] = 20

    next_state[(21, "left")] = 20
    next_state[(21, "up")] = 16
    next_state[(21, "right")] = 22
    next_state[(21, "down")] = 21

    next_state[(22, "left")] = 21
    next_state[(22, "up")] = 17
    next_state[(22, "right")] = 23
    next_state[(22, "down")] = 22

    next_state[(23, "left")] = 22
    next_state[(23, "up")] = 18
    next_state[(23, "right")] = 24
    next_state[(23, "down")] = 23

    next_state[(24, "left")] = 23
    next_state[(24, "up")] = 19
    next_state[(24, "right")] = 24
    next_state[(24, "down")] = 24

    return next_state

# main code
next_state = build_next_state_dictionary()
