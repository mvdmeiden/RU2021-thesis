class State(object):

    # Parameters
    name = 0
    next_state = []

    # Initializer
    def __init__(self, name, next_state):
        self.name = name
        self.next_state = next_state

    # Simple getters (Addendum: Might be superfluous given Python's lack of variable security)
    def return_name(self):
        return self.name

    def return_dictionary(self):
        return self.next_state

    # Returns all potential states this state can progress towards
    def return_next_state_options(self):
        state_numbers = []
        for value in self.next_state.values():
            string_number = value[0]
            actual_number = int(string_number[1])
            state_numbers.append(actual_number)
        return state_numbers

    # Returns output character based on given input
    def return_corresponding_output(self, input):

        return self.next_state[input][1]

    # Returns position of new current state based on given input
    def return_corresponding_new_state(self, input):

        return int(self.next_state[input][0][1])

    # Custom print function for FSM states
    def show(self):
        full_string = ""
        full_string = full_string + self.name + ", "
        full_string = full_string + str(self.next_state)
        print(full_string)
