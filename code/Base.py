
from Agent import Agent
from State import State
from Machine import Machine
import random as rnd


class Base(Agent):
    def __init__(self, i, dataset, acceptance, comp_limit):
        super().__init__(i, dataset, acceptance, comp_limit)
        self.type = 'B'

    def act(self, m=None, method='hamming'):
        generated_machine = self.add_one_state(m)
        generated_data = self.run_machine(generated_machine)
        accuracy = self.check_machine(generated_data, method)

        return generated_machine, accuracy, self.type

    @staticmethod
    def add_one_state(given_machine=None):
        if given_machine is None:
            new_machine = Machine(0)
        else: new_machine = given_machine.copy()
        emptytrans = new_machine.emptytrans
        if not emptytrans:  # or i >= self.comp_limit:
            print('Full FST. Can\'t add any more states')
            return None

        i = len(new_machine.states)
        state_name = 'q' + str(i)
        new_machine.states.append(State(state_name, {}))
        nr_in = rnd.randint(1, len(emptytrans)-1) if len(emptytrans) > 1 else 1
        nr_out = rnd.randint(0, len(new_machine.output_alphabet))

        for j in range(0, nr_in):
            source_state_id, inp = emptytrans.pop(rnd.randrange(len(emptytrans)))
            new_machine.states[int(source_state_id[1])].transitions[inp] = \
                (state_name, rnd.choice(new_machine.output_alphabet))

        for char in new_machine.input_alphabet:
            emptytrans.append((state_name, char))

        for j in range(0, nr_out):
            target_state = rnd.choice(new_machine.states).id
            (state, inp) = rnd.choice(emptytrans[-2 + j:])
            new_machine.states[i].transitions[inp] = (target_state, rnd.choice(new_machine.output_alphabet))
            emptytrans.remove((state, inp))

        return new_machine
