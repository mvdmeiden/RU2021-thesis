class State(object):

    def __init__(self, id, transitions):
        self.id = id
        self.transitions = transitions

    def return_name(self):
        return self.id

    def return_transitions(self):
        return self.transitions

    # Returns all potential states this state can progress towards
    def return_next_state_options(self):
        state_numbers = []
        for value in self.transitions.values():
            string_number = value[0]
            actual_number = int(string_number[1])
            state_numbers.append(actual_number)
        return state_numbers

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.id + str(self.transitions)
