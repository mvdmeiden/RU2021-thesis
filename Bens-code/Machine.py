import random
from State import State
import copy as copy


class Machine:

    # __________________________Parameters______________________________________________________________________________

    # Define maximum number of states for a finite-state machine
    INTERNAL_UPPER_BOUND = 9
    state_amount = random.randint(2, INTERNAL_UPPER_BOUND)

    # Essential components of a finite-state machine
    transition_table = []
    alphabet = None

    # Define state positions for input run-through
    start_state = 0
    current_state = None
    copy_of_previous_state = []

    # Initializer
    def __init__(self, alphabet):
        self.alphabet = alphabet
        pass

    # _______________________Model_FMS_construction_(Randomised)________________________________________________________

    # Constructs random transition table that represents some FSM
    def define_random_fsm(self):

        transition_dict = []
        for i in range(0, self.state_amount):
            i = State('q' + i.__str__(), self.random_fsm_helper(self.alphabet))
            transition_dict.append(i)

        # Checks to see if all states in FSM connect to one another
        if not self.valid_fsm(transition_dict):
            self.define_random_fsm()

        self.transition_table = transition_dict

    # Helper function for filling out transition table
    def random_fsm_helper(self, alphabet):
        dict = {}
        # Random amount of transitions, making sure to grab at least one
        number_of_transitions = random.randint(1, len(self.alphabet))
        while len(dict) != number_of_transitions:
            choice = random.choice(self.alphabet)
            if not dict.__contains__(choice):
                dict[choice] = ('q' + str(random.randint(0, self.state_amount - 1)), random.choice(alphabet))
        return dict

    # _________________________Agent_FSM_construction_(Incrementally_built)_____________________________________________

    # Create machine lists for all possible transformations of current machine (also acts as handy checklist for possible changes (backtracking, removing))   (ALL OPTIONS COME OUT THE SAME< FIX)
    def check_all_options(self):

        all_possible_machines = []

        # Go through all possible mutations for the current states

        for from_state in range(len(self.transition_table)):  # For all states
            for any_letter in self.alphabet:  # For all alphabet letter
                for to_state in range(len(self.transition_table)):
                    for any_output_letter in self.alphabet:  # Again, for all alphabet letters
                        if not self.transition_table[to_state].contains(any_letter):
                            temp = copy.deepcopy(self.transition_table)

                            temp[from_state].next_states[any_letter] = ('q' + str(to_state), any_output_letter)

                            temp_machine = Machine(self.alphabet)
                            temp_machine.transition_table = temp

                            all_possible_machines.append(temp_machine)

        # Additionally, create new state and sent all possible mutations that way

        for from_state in range(len(self.transition_table)):  # For all states
            for any_letter in self.alphabet:      # For all alphabet letter
                for any_output_letter in self.alphabet:  # Again, for all alphabet letters

                    temp = copy.deepcopy(self.transition_table)
                    temp.append(State('q' + str(len(self.transition_table)), {}))

                    temp[from_state].next_states[any_letter] = ('q' + str(len(self.transition_table)), any_output_letter)

                    temp_machine = Machine(self.alphabet)
                    temp_machine.transition_table = temp

                    all_possible_machines.append(temp_machine)

        return all_possible_machines

    # ________________________FSM_consistency_checks____________________________________________________________________
    # Input checker, makes sure every input adheres to dictionary
    def valid_input(self, input):
        valid_input = True
        if not isinstance(input, str):
            valid_input = False
            return valid_input
        for letter in input:
            if not self.alphabet.__contains__(letter):
                valid_input = False
        return valid_input

    # FSM checker, makes sure every state in FSM is reachable
    def valid_fsm(self, dictionary):
        all_connected_states = []
        for state in dictionary:
            list = state.return_next_state_options()
            for v in list:
                all_connected_states.append(v)
        for i in range(0, self.state_amount):
            if not all_connected_states.__contains__(i):
                return False
        return True

    # __________________________User_Functions__________________________________________________________________________
    # Runs input through this machine, returning the full conversion of the input string if possible
    def run_input(self, input):

        output = ""
        current_state = self.transition_table[self.start_state]  # Returns first state from the transition table

        # Input consistency check
        if not self.valid_input(input):
            print("Invalid input, input should be instance of string with subset of dictionary.")
            return None

        # NonEmpty transition table check
        if len(self.transition_table) == 0:
            return input

        # Loop over all letters in the input and add conversion letters to the output

        for letter in input:
            if current_state.possible_to_continue(letter):

                # add conversion letter from second value in the tuple corresponding to input letter
                output = output + current_state.return_corresponding_output(letter)

                # new state becomes first value in the tuple corresponding to input letter
                current_state = self.transition_table[current_state.return_corresponding_new_state(letter)]

            else:
                return output
        return output

    # Print function to display FSM
    def show_fsm(self):
        if not self.transition_table == []:
            print("")
            for i in self.transition_table:
                i.show()
            print("")
        else:
            print("None")
