# imports
import random as rnd
from State import State
import copy


class Machine:

    def __init__(self, upper_bound, input_alphabet=('0', '1'), output_alphabet=None):
        # prep work
        self.input_alphabet = input_alphabet
        self.upper_bound = upper_bound
        self.output_alphabet = output_alphabet if output_alphabet is not None else input_alphabet
        self.num_states = rnd.randint(2, self.upper_bound) if upper_bound >= 2 else upper_bound


        # the actual FST is created here; a list of states with transitions and a list of possible transitions
        self.emptytrans = []
        self.states = self.build_incrementally()

    def build_incrementally(self):
        temp_states = [State('q0', {})]
        for char in self.input_alphabet:
            self.emptytrans.append((0, char))   # add tuple (state id, input)

        for i in range(1, self.num_states):
            state_name = 'q' + str(i)
            nr_out = rnd.randint(0, 2)
            nr_in = rnd.randint(1, int(len(self.emptytrans)/2))

            if not self.emptytrans:
                print('prematurely terminated')
                self.num_states = len(temp_states)
                return temp_states

            for j in range(0, nr_in):
                source_state_id, inp = self.emptytrans.pop(rnd.randrange(len(self.emptytrans)))
                temp_states[source_state_id].transitions[inp] = (state_name, rnd.choice(self.output_alphabet))

            temp_states.append(State(state_name, {}))
            for char in self.input_alphabet:
                self.emptytrans.append((i, char))
            for j in range(0, nr_out):
                target_state = rnd.choice(temp_states).id
                temp_states[i].transitions[rnd.choice(self.input_alphabet)] = (target_state, rnd.choice(self.output_alphabet))

        return temp_states

    def run_input(self, inputString, starting_state=0):
        outputString = ''
        current_state = starting_state  # index of the initial state
        for i in range(len(inputString)):

            temp = inputString[i]                                               # current char in the input string
            if temp not in self.states[current_state].transitions:
                return outputString     # + '_' + inputString[i:len(inputString)]

            next_state, output = self.states[current_state].transitions[temp]
            outputString = outputString + str(output)
            for j in range(0, len(self.states)):                                 # update current state index
                if self.states[j].return_name() == next_state:
                    current_state = j
                    break

        return outputString

    # Simple helper to automatically print FSM transition tables
    def show(self):
        for item in self.states:
            print(item)

    def copy(self):
        return copy.deepcopy(self)
