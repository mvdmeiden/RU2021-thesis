# imports
import random as rnd
from State import State
import copy


class Machine:

    def __init__(self, num_states, input_alphabet=('0', '1'), output_alphabet=None):
        # prep work
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet if output_alphabet is not None else input_alphabet

        if num_states > 50:
            raise ValueError('Too many states')

        # the actual FST is created here; a list of states with transitions and a list of possible transitions
        self.emptytrans = []
        self.states = self.build_machine(num_states)

    def build_machine(self, num_states):
        ''' This function creates the list of states and empty transitions for an FST machine.
        :return: temp_states. A list of states.
        '''

        temp_states = [State('q0', {})]
        for char in self.input_alphabet:
            self.emptytrans.append(('q0', char))                                              # add tuple (state id, input)

        for i in range(1, num_states):
            state_name = 'q' + str(i)
            temp_states.append(State(state_name, {}))
            nr_in = rnd.randint(1, len(self.emptytrans)) if len(self.emptytrans) > 1 else 1
            nr_out = rnd.randint(0, len(self.input_alphabet))

            for j in range(0, nr_in):
                source_state_id, inp = self.emptytrans.pop(rnd.randrange(len(self.emptytrans)))
                temp_states[int(source_state_id[1])].transitions[inp] = (state_name, rnd.choice(self.output_alphabet))

            for char in self.input_alphabet:
                self.emptytrans.append((state_name, char))

            for j in range(0, nr_out):
                target_state = rnd.choice(temp_states).id
                (state, inp) = rnd.choice(self.emptytrans[-2+j:])
                temp_states[i].transitions[inp] = (target_state, rnd.choice(self.output_alphabet))
                self.emptytrans.remove((state, inp))

            if not self.emptytrans:                       # if there are no transitions left, the FST can't be completed
                print('prematurely terminated')
                return temp_states

        return temp_states

    def run_input(self, inputString, starting_state=0):
        '''
        Run an input string through the machine and get output.
        :param inputString: the string to be parsed
        :param starting_state: optional parameter to change the initial state
        :return: output string of the translated input
        '''

        outputString = ''
        current_state = starting_state  # index of the initial state
        for char in inputString:                                               # current char in the input string
            if char not in self.states[current_state].transitions:
                return outputString     # + '_' + inputString[i:len(inputString)]

            next_state, output = self.states[current_state].transitions[char]
            outputString = outputString + str(output)
            for j in range(0, len(self.states)):                                 # update current state index
                if self.states[j].return_name() == next_state:
                    current_state = j
                    break

        return outputString

    # Simple helper to automatically print FSM transition tables
    def show(self):
        '''to nicely print a machine'''
        for item in self.states:
            print(item)

    def copy(self):
        '''to make a copy. avoids call by reference troubles.'''
        return copy.deepcopy(self)
