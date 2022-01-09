from Agent import Agent
from State import State
from Machine import Machine
import random as rnd


class Specialist(Agent):
    def __init__(self, i, acceptance, comp_limit):
        super().__init__(i, acceptance, comp_limit)
        self.type = 'S'

    def act(self, m, observations, method='accuracy'):
        generated_machine = self.add_one_state(m)
        if generated_machine is None:
            return None, 0, self.type

        situations = [x[0] for x in observations]
        generated_data = self.run_machine(situations, generated_machine)
        accuracy = self.check_machine(observations, generated_data, method)

        if accuracy > self.personalbest:
            self.personalbest = accuracy

        return generated_machine, accuracy, self.type

    def add_one_state(self, given_machine=None):
        if given_machine is None:
            return Machine(2)
        else: new_machine = given_machine.copy()

        emptytrans = new_machine.emptytrans
        if not emptytrans:
            print('Full FST. Can\'t add any more states. I\'ll make a new one.')
            # return Machine(2)
            return None

        i = len(new_machine.states)
        if i >= self.comp_limit:
            print('too large. None type returned.')
            return None

        state_name = 'q' + str(i)
        new_machine.states.append(State(state_name, {}))
        nr_in = rnd.randint(1, len(emptytrans)) if len(emptytrans) > 1 else 1
        nr_out = rnd.randint(0, len(new_machine.output_alphabet))

        for j in range(0, nr_in):
            source_state_id, inp = emptytrans.pop(rnd.randrange(len(emptytrans)))
            new_machine.states[int(source_state_id[1])].transitions[inp] = (state_name, rnd.choice(new_machine.output_alphabet))

        for char in new_machine.input_alphabet:
            emptytrans.append((state_name, char))

        for j in range(0, nr_out):
            target_state = rnd.choice(new_machine.states).id
            (state, inp) = rnd.choice(emptytrans[-2 + j:])
            new_machine.states[i].transitions[inp] = (target_state, rnd.choice(new_machine.output_alphabet))
            emptytrans.remove((state, inp))

        return new_machine
