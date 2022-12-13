import unittest
from functions import find_fixed_vector, find_steady_state_prob, which_state, viterbi


class TestViterbi(unittest.TestCase):

    def test_viterbi(self):

        # HMM with pictures testcase
        colors_prob_one = {
            "A": {"red": 0.4, "black": 0.6},
            "B": {"red": 0.7, "black": 0.3},
        }
        states_one = [key for key in colors_prob_one]
        tran_matrix_one = [[0.8, 0.2],
                           [0.5, 0.5]]
        tran_matrix_as_dic_one = {
            "A": {"A": 0.8, "B": 0.2},
            "B": {"A": 0.5, "B": 0.5}
        }
        observations_one = ["red", "red", "black", "red"]

        fixed_vector_one = find_fixed_vector(tran_matrix_one)
        steady_state_prob_one = find_steady_state_prob(
            fixed_vector_one, states_one)
        seq_one = viterbi(tran_matrix_as_dic_one, colors_prob_one,
                      observations_one, states_one, steady_state_prob_one)
        self.assertEqual(seq_one, ['A', 'A', 'A', 'A'])

        # Takehome fall 2022 testcase
        colors_prob_two = {
            "A": {"red": 0.8, "black": 0.2},
            "B": {"red": 0.5, "black": 0.5},
            "C": {"red": 0.2, "black": 0.8}
        }
        states_two = [key for key in colors_prob_two]
        tran_matrix_two = [
            [0.2, 0.3, 0.5],
            [0.2, 0.4, 0.4],
            [0.1, 0.6, 0.3]
        ]
        tran_matrix_as_dic_two = {
            "A": {"A": 0.2, "B": 0.3, "C": 0.5},
            "B": {"A": 0.2, "B": 0.4, "C": 0.4},
            "C": {"A": 0.1, "B": 0.6, "C": 0.3}
        }
        observations_two = ["red", "black", "red"]

        fixed_vector_two = find_fixed_vector(tran_matrix_two)
        steady_state_prob_two = find_steady_state_prob(
            fixed_vector_two, states_two)
        seq_two = viterbi(tran_matrix_as_dic_two, colors_prob_two,
                          observations_two, states_two, steady_state_prob_two)
        self.assertEqual(seq_two, ['B', 'C', 'B'])

        # Long HMM testcase

        colors_prob_three = {
            "A": {"red": 0.8, "black": 0.2},
            "B": {"red": 0.5, "black": 0.5},
            "C": {"red": 0.2, "black": 0.8},
            "D": {"red": 0.3, "black": 0.7}
        }
        states_three = [key for key in colors_prob_three]
        tran_matrix_three = [
            [0.2, 0.3, 0.3, 0.2],
            [0.2, 0.4, 0.1, 0.3],
            [0.1, 0.6, 0.1, 0.2],
            [0.4, 0.1, 0.3, 0.2]
        ]
        tran_matrix_as_dic_three = {
            "A": {"A": 0.2, "B": 0.3, "C": 0.3, "D": 0.2},
            "B": {"A": 0.2, "B": 0.4, "C": 0.1, "D": 0.3},
            "C": {"A": 0.1, "B": 0.6, "C": 0.1, "D": 0.2},
            "D": {"A": 0.4, "B": 0.1, "C": 0.3, "D": 0.2}
        }
        observations_three = ["red", "black",
                              "red", "red", "red", "black", "red"]

        fixed_vector_three = find_fixed_vector(tran_matrix_three)
        steady_state_prob_three = find_steady_state_prob(
            fixed_vector_three, states_three)
        seq_three = viterbi(tran_matrix_as_dic_three, colors_prob_three,
                            observations_three, states_three, steady_state_prob_three)
        self.assertEqual(seq_three, ['A', 'C', 'B', 'B', 'B', 'D', 'A'])

