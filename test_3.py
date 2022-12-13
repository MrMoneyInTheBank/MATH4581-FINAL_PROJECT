from functions import find_fixed_vector, find_steady_state_prob, find_single_color_prob, which_state, viterbi

colors_prob = {
    "A": {"red": 0.8, "black": 0.2},
    "B": {"red": 0.5, "black": 0.5},
    "C": {"red": 0.2, "black": 0.8},
    "D": {"red": 0.3, "black": 0.7}
}

states = [key for key in colors_prob]


tran_matrix = [
    [0.2, 0.3, 0.3, 0.2],
    [0.2, 0.4, 0.1, 0.3],
    [0.1, 0.6, 0.1, 0.2],
    [0.4, 0.1, 0.3, 0.2]
]

tran_matrix_as_dic = {
    "A": {"A": 0.2, "B": 0.3, "C": 0.3, "D": 0.2},
    "B": {"A": 0.2, "B": 0.4, "C": 0.1, "D": 0.3},
    "C": {"A": 0.1, "B": 0.6, "C": 0.1, "D": 0.2},
    "D": {"A": 0.4, "B": 0.1, "C": 0.3, "D": 0.2}
}

observations = ["red", "black", "red", "red", "red", "black", "red"]

# Executing the calculations
if __name__ == "__main__":

    fixed_vector = find_fixed_vector(tran_matrix)

    print(f"\nThe fixed vector for this model is {fixed_vector}\n")

    steady_state_prob = find_steady_state_prob(fixed_vector, states)

    print(f"We observe a red marble. Which bag did it likely come from?\n")

    print(which_state(steady_state_prob, fixed_vector, colors_prob, "red"))

    print(
        f"We observe the sequence {observations}. What is the most likely sequence of states?\n")

    seq = viterbi(tran_matrix_as_dic, colors_prob,
                  observations, states, steady_state_prob)

    print(f"The most likely sequence is {seq}.")
