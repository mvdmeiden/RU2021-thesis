class State(object):
    # State object class representing one node in an FSM model

    # Parameters
    state_name = ""  # String representation
    next_states = {}  # Dictionary

    # Initializer
    def __init__(self, name, next_states):
        self.name = name
        self.next_states = next_states

    # Returns all potential states this state can progress towards for the sake of connected FSM structures
    def return_next_state_options(self):
        state_numbers = []
        for value in self.next_states.values():
            string_number = value[0]
            actual_number = int(string_number[1])
            state_numbers.append(actual_number)
        return state_numbers

    # Returns output character based on given input
    def return_corresponding_output(self, input):
        return self.next_states[input][1]

    # Returns position of new current state based on given input
    def return_corresponding_new_state(self, input):
        value = self.next_states.get(input)
        return int(value[0][1])

    # Custom print function for FSM states
    def show(self):
        full_string = ""
        full_string = full_string + self.name + ", "
        full_string = full_string + str(self.next_states)
        print(full_string)

    # Checks if a given letter is represented in the FSM as to make sure the transition process can continue
    def possible_to_continue(self, letter):
        return list(self.next_states.keys()).__contains__(letter)

    def contains(self, letter):
        return list(self.next_states.keys()).__contains__(letter)

    def add_to_dictionary(self, non_present_letters, state, any_letter):
        self.next_states[non_present_letters] = (state, any_letter)
        pass
