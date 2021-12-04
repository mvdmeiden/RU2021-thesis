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
        return False
