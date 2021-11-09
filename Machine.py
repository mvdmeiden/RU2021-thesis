import random
import numpy
from State import State


class Machine:
    INTERNAL_UPPER_BOUND = 9
    state_amount = random.randint(2, INTERNAL_UPPER_BOUND)
    transition_dictionary = None
    current_state = 0

    def __init__(self):
        pass

    def run_input(self, input):

        output = False
        return output

    # Simple helper to automatically print FSM transition tables
    def show_dictionary(self):

        print(self.transition_dictionary)
        print(" ")

    # Constructs random transition dictionary representing a random FSM
    def define_random_dictionary(self):

        transition_dict = []
        for i in range(0, self.state_amount):
            i = State('s' + i.__str__(), {})
            transition_dict.append(State('s2', {0: ('s1', 1), 1: ('s2', 0)}))

        self.transition_dictionary = transition_dict



