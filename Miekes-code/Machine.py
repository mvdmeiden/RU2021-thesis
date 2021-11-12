# imports
import random as rnd
from State import State


class Machine:

    def __init__(self, upper_bound, input_alphabet=('0', '1'), output_alphabet=None):
        # prep work
        self.input_alphabet = input_alphabet
        self.upper_bound = upper_bound
        self.output_alphabet = output_alphabet if output_alphabet is not None else input_alphabet
        self.num_states = rnd.randint(2, self.upper_bound) if upper_bound >= 2 else upper_bound

        # the actual FST is created here; a list of states with transitions
        self.states = None
        #while not self.is_valid():
        #    print('i tried')
            # self.states = self.make_state_list(self.num_states, self.input_alphabet, self.output_alphabet)
        self.build_incrementally()

    def make_state_list(self, num_states, input_alphabet, output_alphabet):
        state_list = []
        temp_states = []
        for i in range(0, num_states):
            s = 'q' + str(i)
            temp_states.append(s)
            state_list.append(State('q' + str(i), {}))

        for state in state_list:
            for j in range(0, len(input_alphabet)):
                state.transitions[input_alphabet[j]] = (rnd.choice(temp_states), rnd.choice(output_alphabet))

        return state_list

    def build_incrementally(self):
        self.states = [State('q0', {})]
        for i in range(1, self.num_states):
            state_name = 'q' + str(i)
            nr_out = rnd.randint(0, 2)
            nr_in = rnd.randint(1, self.num_states)

            for j in range(0, nr_in):
                source_state = rnd.choice(self.states)
                rnd_inp = rnd.choice(self.input_alphabet)
                if rnd_inp not in source_state.transitions:
                    source_state.transitions[rnd_inp] = (state_name, rnd.choice(self.output_alphabet))

            self.states.append(State(state_name, {}))
            for j in range(0, nr_out):
                target_state = self.states[rnd.randrange(0, len(self.states))].id
                self.states[i].transitions[rnd.choice(self.input_alphabet)] = (target_state, rnd.choice(self.output_alphabet))

            self.show()
            print()

    def is_valid(self):
        # if no state list exists, the machine is not valid
        if self.states is None:
            return False

        # if a list does exist start checking consistency
        all_connected_states = []
        for state in self.states:
            list = state.return_next_state_options()
            for v in list:
                all_connected_states.append(v)
        for i in range(0, self.num_states):
            if not all_connected_states.__contains__(i):
                return False
        return True


    def run_input(self, inputString, starting_state=0):

        outputString = ''
        current_state = starting_state  # index of the initial state
        for i in range(len(inputString)):

            temp = inputString[i]                                               # current char in the input string
            match = self.states[current_state].transitions.get(temp)            # see if string char is in dictionary
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
