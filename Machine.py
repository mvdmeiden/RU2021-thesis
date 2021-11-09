import random
from State import State


class Machine:
    INTERNAL_UPPER_BOUND = 9
    state_amount = random.randint(2, INTERNAL_UPPER_BOUND)

    transition_dictionary = None
    dictionary = ['a', 'b']

    start_state = 0
    current_state = None

    # __________________________FSM_Construction__________________________________

    # Initializer
    def __init__(self):
        pass

    # Constructs random transition dictionary that represents a random FSM
    def define_random_fsm(self):

        transition_dict = []
        for i in range(0, self.state_amount):
            i = State('q' + i.__str__(), self.random_fsm_helper(self.dictionary))
            transition_dict.append(i)

        # Checks to see if all states in FSM connect to one another
        if not self.valid_fsm(transition_dict):
            self.define_random_fsm()

        self.transition_dictionary = transition_dict

    # Helper function for filling out dictionary
    def random_fsm_helper(self, dictionary):
        dict = {}
        for i in dictionary:
            dict[i] = ('q' + str(random.randint(0, self.state_amount - 1)), random.choice(dictionary))
        return dict

    # ________________________Consistency_Checks________________________________

    # Input checker, makes sure every input adheres to dictionary
    def valid_input(self, input):
        valid_input = True
        if not isinstance(input, str):
            valid_input = False
            return valid_input
        for letter in input:
            if not self.dictionary.__contains__(letter):
                valid_input = False
        return valid_input

    # FSM checker, makes sure every state in FSM is reachable
    def valid_fsm(self, dictionary):
        all_connected_states = []
        for state in dictionary:
            list = state.return_next_state_options()
            for v in list:
                all_connected_states.append(v)
        print(all_connected_states)
        for i in range(0, self.state_amount):
            if not all_connected_states.__contains__(i):
                return False
        return True

    # __________________________FSM_User_Functions__________________________

    def run_input(self, input):
        output = ""
        current_state = self.transition_dictionary[self.start_state]

        # Input consistency check
        if not self.valid_input(input):
            print("Invalid input, input should be instance of string with subset of dictionary.")
            return None
        if self.transition_dictionary == []:
            print(input)
            return input

        for letter in input:
            output = output + current_state.return_corresponding_output(letter)
            current_state = self.transition_dictionary[current_state.return_corresponding_new_state(letter)]

        print("Input:")
        print(input)
        print("Output:")
        print(output)
        return output

    # Print function to display FSM
    def show_fsm(self):
        print("")
        print("Transition dictionary of FSM:")
        for i in self.transition_dictionary:
            i.show()
        print("")
