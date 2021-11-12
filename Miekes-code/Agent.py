# imports
import random as rnd
from scipy.spatial import distance
import textdistance
from State import State
from Machine import Machine


class Agent:
    def __init__(self, i, dataset=[], acceptance=0.6, comp_limit=5):
        self.id = i
        self.acceptance = acceptance
        self.comp_limit = comp_limit
        self.current_machine = None
        self.dataset = dataset
        self.satisfied = False

    def generate_machine_onestate(self, input_machine: Machine = Machine(0)):
        # create own machine if input is None
        if input_machine is None:
            input_machine = Machine(0)

        state_index = len(input_machine.states)
        input_machine.states.append(State('q' + str(state_index), {}))
        temp_states = [state.return_name() for state in input_machine.states]

        for j in range(0, len(input_machine.input_alphabet)):
            input_machine.states[state_index].transitions[input_machine.input_alphabet[j]] = \
                (rnd.choice(temp_states), rnd.choice(input_machine.output_alphabet))

        self.current_machine = input_machine

    def check_machine(self):
        output = [self.current_machine.run_input(i) for i in self.dataset[:, 0]]
        print(output)
        correct = 0
        for i in range(0, len(output)):
            if output[i] == self.dataset[i][1]:
                correct += 1

        accuracy = correct/len(self.dataset)
        if accuracy > self.acceptance:
            self.satisfied = True
        return accuracy

    def check_machine_char(self):
        output = [self.current_machine.run_input(i) for i in self.dataset[:, 0]]
        print(output)
        sum = 0
        for i in range(0, len(output)):
            sum += 1 - (textdistance.hamming(output[i], self.dataset[i][1])/len(output[i]))

        accuracy = sum/len(output)
        if accuracy > self.acceptance:
            self.satisfied = True
        return accuracy








