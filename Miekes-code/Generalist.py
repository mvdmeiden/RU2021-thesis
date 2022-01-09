from Agent import Agent
from State import State
from Machine import Machine
import random as rnd
import itertools


class Generalist(Agent):
    def __init__(self, i, acceptance, comp_limit):
        super().__init__(i, acceptance, comp_limit)
        self.type = 'G'

    def act(self, m1, m2, observations, method='hamming'):
        generated_machine = self.combine_machines(m1, m2)

        situations = [x[0] for x in observations]
        generated_data = self.run_machine(situations, generated_machine)
        accuracy = self.check_machine(observations, generated_data, method)

        if accuracy > self.personalbest:
            self.personalbest = accuracy

        return generated_machine, accuracy, self.type

    def combine_machines(self, m1, m2):
        if m1 is None:
            m1 = Machine(self.comp_limit)
        if m2 is None:
            m2 = Machine(self.comp_limit)
        if m1.input_alphabet is not m2.input_alphabet:
            raise IOError('input alphabet not the same')

        if len(m1.states) > self.comp_limit or len(m2.states) > self.comp_limit:
            print("too complex for me to handle :(")
            return None

        new_state_list = []
        new_emptytrans = []
        new_input_alphabet = m1.input_alphabet
        for q1, q2 in itertools.zip_longest(m1.states, m2.states):
            state = rnd.choice([q1, q2])
            if state:
                new_state_list.append(State('q'+str(len(new_state_list)), state.transitions))

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

