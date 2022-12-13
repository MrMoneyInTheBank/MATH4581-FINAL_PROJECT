from functions import find_fixed_vector, find_steady_state_prob, which_state, viterbi

colors_prob = {
    "A": {"red": 0.4, "black": 0.6},
    "B": {"red": 0.7, "black": 0.3},
}

states = [key for key in colors_prob]


tran_matrix = [[0.8, 0.2],
               [0.5, 0.5]]

tran_matrix_as_dic = {
    "A": {"A": 0.8, "B": 0.2},
    "B": {"A": 0.5, "B": 0.5}
}

observations = ["red", "red", "black", "red"]


# Executing the calculations
if __name__ == "__main__":

    fixed_vector = find_fixed_vector(tran_matrix)

    print(f"\nThe fixed vector for this model is {fixed_vector}\n")

    steady_state_prob = find_steady_state_prob(fixed_vector, states)

    print(f"We observe a red marble. Which bag did it likely come from?\n")

    print(which_state(steady_state_prob, fixed_vector, colors_prob, "red"))

    print("We observe the sequence red, red, black, red. What is the most likely sequence of states?\n")

    seq = viterbi(tran_matrix_as_dic, colors_prob,
                  observations, states, steady_state_prob)
    print(f"The most likely sequence is {seq}.")
