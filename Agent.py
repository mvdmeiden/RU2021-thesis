# imports
import random as rnd
from State import State
from Machine import Machine


class Agent:
    def __init__(self, i, acceptance=0.6, comp_limit=5):
        self.id = i
        self.acceptance = acceptance
        self.comp_limit = comp_limit
        self.current_machine = None

    def generate_machine_onestate(self, input_machine: Machine=None):
        # add behaviour for if input_machine is None
        if input_machine is None:
            input_machine = Machine(0)

        state_index = len(input_machine.states)
        input_machine.states.append(State('s' + str(state_index), {}))
        temp_states = [state.return_name() for state in input_machine.states]

        for j in range(0, len(input_machine.input_alphabet)):
            input_machine.states[state_index].transitions[input_machine.input_alphabet[j]] = \
                (rnd.choice(temp_states), rnd.choice(input_machine.output_alphabet))

        self.current_machine = input_machine



