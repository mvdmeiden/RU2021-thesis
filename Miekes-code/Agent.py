# imports
import textdistance


class Agent:
    def __init__(self, i, dataset=None, acceptance=0.5, comp_limit=10):
        self.id = i
        self.dataset = dataset if not None else []
        self.acceptance = acceptance
        self.comp_limit = comp_limit
        self.satisfied = False

    def run_machine(self, m):
        return [m.run_input(i) for i in self.dataset[:, 0]]

    def check_machine(self, data, method='hamming'):
        sum = 0
        if method == 'hamming':
            for i, a, b in zip(self.dataset[:, 0], self.dataset[:, 1], data):
                distance = textdistance.hamming(a, b)
                sum += 1-(distance/len(i))

            result = sum/len(self.dataset)
            if result > self.acceptance:
                self.satisfied = True

            return result

        if method == 'accuracy':
            correct = 0
            for a, b in zip(self.dataset[:, 1], data):
                if a == b:
                    correct += 1
            accuracy = correct/len(self.dataset)

            if accuracy > self.acceptance:
                self.satisfied = True
            return accuracy









