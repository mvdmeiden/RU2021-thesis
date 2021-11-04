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

    def run_input(self, input):
        current_state = self.transition_dictionary[self.start_state]
        output = ""
        if not self.valid_input(input):
            print("Invalid input, input should be instance of string with subset of dictionary.")
            return None
        for letter in input:
            output = output + self.transition_dictionary[letter]
            current_state = self.transition_dictionary[letter]

        return output

    #Print function to display FSM
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

    #Helper function for filling out dictionary
    def random_dictionary_helper(self, dictionary):
        dict = {}
        for i in dictionary:
            dict[i] = ('q' + str(random.randint(0, self.state_amount - 1)), random.choice(dictionary))
        return dict

    #Input checker
    def valid_input(self, input):
        valid_input = True
        if not isinstance(input, str):
            valid_input = False
            return valid_input
        for l in input:
            if not self.dictionary.__contains__(l):
                valid_input = False
        return valid_input


