from numpy.linalg import matrix_power

def find_fixed_vector(matrix):
    '''Takes in a matrix and returns the fixed vector array'''
    # Since we have a complete matrix, we can raise it to a high power 
    # and take the first row to be our fixed vector

    # If the matrix dimensions grow very large in size, then it might
    # be more efficient to use linear algebra to find the basis vector
    # but as presented, this function has a space complexity of O(1).

    return matrix_power(matrix, 100)[0] 

def find_steady_state_prob(f_vector, states):
    '''Takes in the fixed vector array and states and returns 
       the steady state probabilities for each state'''
    
    # Time complexity - O(n) || Space complexity O(n)

    # Initializing a dictionary to map each state to their steady
    # state probability

    steady_state_prob = {}

    for i in range(len(states)): # Looping through all of the states
        steady_state_prob[states[i]] = f_vector[i] # Mapping the state to their fixed vector element
    
    return steady_state_prob 

def find_single_color_prob(colors_prob, color):
    '''Takes in the emission matrix and returns the probability
       of observing a specific color from every state'''

    # Time complexity - O(n) || Space complexity O(n)

    # Initializing a dictionary to map each state to their probability
    # of observing a specific color 
       
    color_prob = {}

    for key in colors_prob: # Looping through all states in the emission matrix
        color_prob[key] = colors_prob[key][color] # Mapping each state to the probability of a specific color
    
    return color_prob

def which_state(steady_state_probs, f_vector, colors_prob, color):
    '''Takes in the steady state probabilities, the fixed vector,
       the emmission matrix and a specific color to return the probability 
       take a certain color came from a specific state. Returns the state 
       with the highest probability.'''

    # Getting the probability of a specific color from each state 
    color_prob = find_single_color_prob(colors_prob, color)

    # Converting the probabilities into a list for ease of calculations
    probs = list(color_prob.values())

    # The denominator is just the sum of the disjoint probabilities
    # adding together the probability of coming from each state multiplied
    # by the probability of a color from a each state

    denominator = 0 

    for i in range(len(f_vector)):
        summand = f_vector[i] * probs[i]
        denominator += summand 
    
    # Initializing a result dictionary which maps 
    # the probability of a color coming from each state

    res = {}

    for key in colors_prob: # Looping over all the states
        numerator = steady_state_probs[key] * colors_prob[key][color] # Calculating the conditional probability
        res[key] = numerator / denominator # Mapping the quotient to the state
    
    # Getting the state with the highest probability
    max_prob = max(res, key=res.get)
    return f"The {color} marble most likely came from bag {max_prob} with a probability of {res[max_prob]}.\n \nAll the probabilities are {res}\n" 

def viterbi(tran_matrix_as_dic, emit_matrix, obs, states, steady_state_prob):
    '''Takes in the transition matric, the emission matric, the observed sequence
       the state diagrams and the steady state probability and returns the state sequence
       with the highest probability of observing the given sequence.'''

    # Initializing a dynamic table where each index represents 
    # the current probabilities for each state

    dp_table = []

    for i in range(len(obs)): # Iterating for the number of observations 
        # For the first step, we can just calculate the probabilities using the 
        # fixed vector element for each state
        if i == 0:
            probs = {}
            for state in states:
                prob = steady_state_prob[state]*emit_matrix[state][obs[i]]
                
                probs[state] = {"prob": prob, "prev": None}
            dp_table.append(probs)
        # For subsequent steps, we need to the probabilities from the last step,
        # the element from the transition matrix, and the emission probability
        else:
            probs = {} # The probabilities for the current step; initially empty dictionary
            total = {} # All the probabilities for the next step. Only the maximum for each state is kept
            # Looping over from each state to every other state
            for start_state in states: 
                for end_state in states:
                    prob = dp_table[-1][start_state]["prob"] * tran_matrix_as_dic[start_state][end_state] * emit_matrix[end_state][obs[i]]
                    
                    if end_state not in total:
                        total[end_state] = [{"prob": prob, "prev": start_state}]
                    else:
                        total[end_state].append({"prob": prob, "prev": start_state})
            
            # Getting the final probability for the current step
            for key in total: # Looping over every state and all the probabilities of getting there
                maxThusFar = float("-inf")
                prev = None
                for dic in total[key]:
                    if dic["prob"] > maxThusFar:
                        maxThusFar = dic["prob"]
                        prev = dic["prev"]
                probs[key] = {"prob": maxThusFar, "prev": prev}
            
            # Appending the current step probabilities to the dynamic table
            dp_table.append(probs)
        
    # Initializing the most likely sequence with an empty array
    sequence = []

    i = len(obs) - 1 # Initializing an iterator variable
    
    while i > -1: # Iterating over the number of steps
        currentStep = dp_table[i] # Getting the current step probabilities
        currentMax = float("-inf")
        currentPrev = None
        currentState = None 

        # Picking the state with the highest probability
        for key, value in currentStep.items():
            prob = value["prob"]
            if prob > currentMax:
                currentMax = prob
                currentPrev = value["prev"]
                currentState = key 
        
        # Appending the states in reverse sequence since we are working backwords
        sequence.append(currentState)
        i -= 1
    
    # reversing the sequence before returning it
    return sequence[::-1]