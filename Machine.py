import random
import numpy
from State import State


class Machine:
    INTERNAL_UPPER_BOUND = 9
    state_amount = random.randint(2, INTERNAL_UPPER_BOUND)
    transition_dictionary = None
    current_state = 0
    dictionary = ['a', 'b']
    start_state= 0

    def __init__(self):
        pass

    def run_input(self, input, transition_dictionary):

        output = False
        return output

    #Simple helper to automatically print FSM transition tables
    def show_dictionary(self):
        print("")
        print("Transition dictionary of FSM:")
        for i in self.transition_dictionary:
            i.show()
        print("")

    #Constructs random transition dictionary representing a random FSM
    def define_random_dictionary(self):

        transition_dict = []
        for i in range(0, self.state_amount):
            i = State('q' + i.__str__(), self.random_dictionary_helper(self.dictionary))
            transition_dict.append(i)

        self.transition_dictionary = transition_dict

    def random_dictionary_helper(self, dictionary):
        dict = {}
        for i in dictionary:
            dict[i] = ('q' + str(random.randint(0, self.state_amount - 1)), random.choice(dictionary))
        return dict



