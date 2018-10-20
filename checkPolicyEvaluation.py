import newGridWorld as gw
import numpy as np

def policy_eval_in_place(state_count, gamma, theta, get_policy, get_transitions):
    """
    This function uses the two-array approach to evaluate the specified policy for the specified MDP:
    
    'state_count' is the total number of states in the MDP. States are represented as 0-relative numbers.
    
    'gamma' is the MDP discount factor for rewards.
    
    'theta' is the small number threshold to signal convergence of the value function (see Iterative Policy Evaluation algorithm).
    
    'get_policy' is the stochastic policy function - it takes a state parameter and returns list of tuples, 
        where each tuple is of the form: (action, probability).  It represents the policy being evaluated.
        
    'get_transitions' is the state/reward transiton function.  It accepts two parameters, state and action, and returns
        a list of tuples, where each tuple is of the form: (next_state, reward, probabiliity).  
         
    """
    V = state_count*[0]
    Theta = 10
    while (Theta > theta):
    	diff = []
    	for state in xrange(state_count):
	    	updValue = 0
	    	policy = get_policy(state)
	    	for eachPolicy in policy:
	    		determinants = get_transitions(state,eachPolicy[0])
	    		nextState = determinants[0][0]
	    		reward = determinants[0][1]
	    		updValue = updValue + eachPolicy[1]*(reward + gamma*V[nextState])
	    	diff.append(abs(V[state]-updValue))
	    	V[state] = updValue
		Theta = max(diff)
    #
    # insert code here to evaluate the policy using the in-place approach 
    #
    return V

def get_equal_policy(state):
	# build a simple policy where all 4 actions have the same probability, ignoring the specified state
	policy = ( ("up", .25), ("right", .25), ("down", .25), ("left", .25))
	return policy

n_states = gw.get_state_count()

# test our function
values = policy_eval_in_place(state_count=n_states, gamma=0.9, theta=.001, get_policy=get_equal_policy, \
    get_transitions=gw.get_transitions)

print("Values=", np.around(values,decimals=2))