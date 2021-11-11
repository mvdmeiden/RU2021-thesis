from Machine import Machine


class Agent:
    # Parameters
    minimum_accuracy = 0
    accuracy = 0
    max_amount_of_states = 0
    data = 0
    current_machine = None
    dictionary = None
    bias = 0

    # ____________________________Agent_Initialization_______________________________________

    # Initialization
    def __init__(self, acceptance_threshold, complexity_limit, dictionary):
        self.minimum_accuracy = acceptance_threshold
        self.max_amount_of_states = complexity_limit
        self.dictionary = dictionary
        current_machine = Machine(dictionary)
        pass

    def check_current_Model(self, input, own_machine):
        return 0

    def refer_on(self, data, machine):
        self.amount_of_states = self.amount_of_states + 1
        return 0

    def get_states(self):

        return self.amount_of_states

    def get_acceptance(self):

        return self.current_acceptance

    def print_results(self):
        print("Agent found machine: ")
        print(self.current_machine)
        print("_________")
        print("With accuracy rating:" + self.accuracy.__str__())
        print("")
        return 0
