import newGridWorld as gw
# import episodicGridWorld as gw
import numpy as np

def policy_iteration(state_count, gamma, theta, get_available_actions, get_transitions):
    V = state_count*[0]               
    pi = state_count*[0]

    for states in range(state_count):
        avail_actions = get_available_actions(states)
        pi[states] = avail_actions[np.random.randint(0,4)]

    while(True):
        Theta = 10
        while(Theta > theta):
            diff = []
            for state in range(state_count): 
                updValue = 0
                action = pi[state]
                determinants = get_transitions(state,action)
                nextState = determinants[0][0]
                reward = determinants[0][1]
                updValue = reward + gamma*V[nextState]
                diff.append(abs(V[state]-updValue))
                V[state] = updValue
            Theta = max(diff)

        policyStable = True
        for state in range(state_count):
            old_action = pi[state]
            allPossibleActions = get_available_actions(state)
            allPossibleReturns = []
            for possAction in allPossibleActions:
                determinant = get_transitions(state,possAction)
                next_state = determinant[0][0]
                Reward = determinant[0][1]
                allPossibleReturns.append(Reward+gamma*V[next_state])
            bestReturnindex = allPossibleReturns.index(max(allPossibleReturns))
            best_action = allPossibleActions[bestReturnindex]
            pi[state] = best_action
            if (old_action != best_action):
                policyStable = False
            print(pi)
        if (policyStable):
            break

    return (V, pi)        # return both the final value function and the final policy

n_states = gw.get_state_count()
# test our function
values, policy = policy_iteration(state_count=n_states, gamma=0.9, theta=.001, get_available_actions=gw.get_available_actions, get_transitions=gw.get_transitions)
print("Values=", np.around(values,decimals=2))
print("Policy=", policy)