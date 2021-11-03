# imports
import random as rnd
from State import State


class Machine:

    def __init__(self, upper_bound, input_alphabet=(0, 1), output_alphabet=None):
        self.input_alphabet = input_alphabet
        self.upper_bound = upper_bound
        self.output_alphabet = output_alphabet if output_alphabet is not None else input_alphabet
        self.num_states = rnd.randint(2, self.upper_bound)
        self.states = self.make_state_list(self.num_states, self.input_alphabet, self.output_alphabet)

    @staticmethod
    def make_state_list(num_states, input_alphabet, output_alphabet):
        state_list = []
        temp_states = []
        for i in range(0, num_states):
            s = 's' + str(i)
            temp_states.append(s)
            state_list.append(State('s' + str(i), {}))

        for state in state_list:
            for j in range(0, len(input_alphabet)):
                state.transitions[input_alphabet[j]] = (rnd.choice(temp_states), rnd.choice(output_alphabet))

        return state_list

    def run_input(self, inputString, starting_state=0):

        outputString = ''
        current_state = starting_state  # index of the initial state
        for i in range(len(inputString)):

            temp = inputString[i]                                               # current char in the input string
            match = self.states[current_state].transitions.get(int(temp))       # see if string char is in dictionary
            if match is None:
                return 'incorrect character in string'                          # if not: give error message

            next_state, output = match
            outputString = outputString + str(output)
            for j in range(0, self.num_states):                                 # update current state index
                if self.states[j].return_name() == next_state:
                    current_state = j
                    break

        return outputString

    # Simple helper to automatically print FSM transition tables
    def show(self):
        for item in self.states:
            print(item)
