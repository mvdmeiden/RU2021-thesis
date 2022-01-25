# imports
import textdistance


class Agent:
    def __init__(self, i, acceptance=0.5, comp_limit=10):
        self.id = i
        self.acceptance = acceptance
        self.comp_limit = comp_limit
        self.satisfied = False

    @staticmethod
    def run_machine(data, m):
        return m.observe(situations=data) if m is not None else None

    def check_machine(self, observed, generated, method='hamming'):
        if generated is None or observed is None:
            return 0

        sum = 0
        if method == 'hamming':
            for i, a, b in zip(observed, observed, generated):
                distance = textdistance.hamming(a[1], b[1])
                sum += 1-(distance/len(a[0]))

            result = sum/len(observed)
            if result > self.acceptance:
                self.satisfied = True

            return result

        if method == 'accuracy':
            correct = 0
            for a, b in zip(observed, generated):
                if a[1] == b[1]:
                    correct += 1
            accuracy = correct/len(observed)

            if accuracy > self.acceptance:
                self.satisfied = True
            return accuracy

        print('unrecognized method. 0 returned')
        return 0
