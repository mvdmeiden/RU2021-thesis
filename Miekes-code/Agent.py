# imports
import random as rnd
import textdistance
from State import State
from Machine import Machine


class Agent:
    def __init__(self, i, dataset=None, acceptance=0.5, comp_limit=10):
        self.id = i
        self.dataset = dataset if not None else []
        self.acceptance = acceptance
        self.comp_limit = comp_limit
        self.given_machine = None
        self.generated = None
        self.satisfied = False

    def add_one_state(self, given_machine=None):
        if given_machine is None:
            new_machine = Machine(0)
        else: new_machine = given_machine.copy()

        i = len(new_machine.states)
        state_name = 'q' + str(i)
        emptytrans = new_machine.emptytrans
        nr_out = rnd.randint(0, 2)
        nr_in = rnd.randint(1, len(emptytrans))

        if not emptytrans or i >= self.comp_limit:
            # maybe add transitions
            return new_machine

        for j in range(0, nr_in):
            source_state_id, inp = emptytrans.pop(rnd.randrange(len(emptytrans)))
            new_machine.states[source_state_id].transitions[inp] = (state_name, rnd.choice(new_machine.output_alphabet))

        new_machine.states.append(State(state_name, {}))
        for char in new_machine.input_alphabet:
            emptytrans.append((i, char))
        for j in range(0, nr_out):
            target_state = rnd.choice(new_machine.states).id
            new_machine.states[i].transitions[rnd.choice(new_machine.input_alphabet)] = (
                target_state, rnd.choice(new_machine.output_alphabet))
        self.given_machine = new_machine

    def run_machine(self):
        self.generated = [self.given_machine.run_input(i) for i in self.dataset[:, 0]]
        # print(self.generated)

    def check_machine(self, method='hamming'):
        if self.generated is None:
            return 'No output generated yet. Please first run the input through a machine.'

        sum = 0
        if method == 'hamming':
            for i, a, b in zip(self.dataset[:, 0], self.dataset[:, 1], self.generated):
                distance = textdistance.hamming(a, b)
                sum += 1-(distance/len(i))

            result = sum/len(self.dataset)
            if result > self.acceptance:
                self.satisfied = True

            return 'hamming accuracy: ' + str(result)

        if method == 'accuracy':
            correct = 0
            for a, b in zip(self.dataset[:, 1], self.generated):
                if a == b:
                    correct += 1
            accuracy = correct/len(self.dataset)

            if accuracy > self.acceptance:
                self.satisfied = True
            return 'accuracy: ' + str(accuracy)








