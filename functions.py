from numpy.linalg import matrix_power

def find_fixed_vector(matrix):
    return matrix_power(matrix, 100)[0]

def find_steady_state_prob(f_vector, states):
    res = {}

    for i in range(len(states)):
        res[states[i]] = f_vector[i]
    
    return res 

def find_single_color_prob(colors_prob, color):
    color_prob = {}

    for key in colors_prob:
        color_prob[key] = colors_prob[key][color]
    
    return color_prob

def which_state(steady_state_probs, f_vector, colors_prob, color):
    color_prob = find_single_color_prob(colors_prob, color)

    probs = list(color_prob.values())

    denominator = 0 

    for i in range(len(f_vector)):
        summand = f_vector[i] * probs[i]
        denominator += summand 
    
    res = {}

    for key in colors_prob:
        numerator = steady_state_probs[key] * colors_prob[key][color]
        res[key] = numerator / denominator 
    
    max_prob = max(res, key=res.get)
    return f"The marble most likely came from bag {max_prob} with a probability of {res[max_prob]}.\n All the probabilities are {res}" 

def viterbi(tran_matrix_as_dic, emit_matrix, obs, states, steady_state_prob):

    dp_table = []

    for i in range(len(obs)):
        if i == 0:
            probs = {}
            for state in states:
                prob = steady_state_prob[state]*emit_matrix[state][obs[i]]
                
                probs[state] = {"prob": prob, "prev": None}
            dp_table.append(probs)
        else:
            curr = {}
            probs = {}
            for start_state in states:
                for end_state in states:
                    prob = dp_table[-1][start_state]["prob"] * tran_matrix_as_dic[start_state][end_state] * emit_matrix[end_state][obs[i]]
                    
                    if end_state not in curr:
                        curr[end_state] = [{"prob": prob, "prev": start_state}]
                    else:
                        curr[end_state].append({"prob": prob, "prev": start_state})
            
            for key in curr:
                maxThusFar = float("-inf")
                prev = None
                for dic in curr[key]:
                    if dic["prob"] > maxThusFar:
                        maxThusFar = dic["prob"]
                        prev = dic["prev"]
                probs[key] = {"prob": maxThusFar, "prev": prev}
            
            dp_table.append(probs)
        
    sequence = []

    
    
    i = len(obs) - 1
    
    while i > -1:
        currentStep = dp_table[i]
        currentMax = float("-inf")
        currentPrev = None 
        currentState = None 

        for key, value in currentStep.items():
            
            prob = value["prob"]
            if prob > currentMax:
                currentMax = prob
                currentPrev = value["prev"]
                currentState = key 
        
        sequence.append(currentState)
        i -= 1
        

    return sequence