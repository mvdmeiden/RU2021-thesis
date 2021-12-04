from Agent import Agent
from State import State
from Machine import Machine
import random as rnd


class Generalist(Agent):
    def __init__(self, i, dataset, acceptance, comp_limit):
        super().__init__(i, dataset, acceptance, comp_limit)

    def act(self, m1, m2, method='hamming'):
        generated_machine = self.combine_machines(m1, m2)
        generated_data = self.run_machine(generated_machine)
        accuracy = self.check_machine(generated_data, method)

        return generated_machine, accuracy, 'G'

    def combine_machines(self, m1, m2):
        if m1.input_alphabet is not m2.input_alphabet:
            raise IOError('input alphabet not the same')

        new_state_list = []
        new_emptytrans = []
        new_input_alphabet = m1.input_alphabet
        for q1, q2 in zip(m1.states, m2.states):
            state = rnd.choice([q1, q2])
            new_state_list.append(state)

        for state in new_state_list:
            for key, value in list(state.transitions.items()):
                if int(value[0][1]) >= len(new_state_list):
                    del state.transitions[key]
            for char in new_input_alphabet:
                if char not in state.transitions:
                    new_emptytrans.append((state.id, char))

        new_m = Machine(0)
        new_m.states = new_state_list
        new_m.emptytrans = new_emptytrans
        return new_m

