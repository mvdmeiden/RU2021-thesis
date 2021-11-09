class State(object):

    name = 0
    next_state = 0

    def __init__(self, name, next_state):
        self.name = name
        self.next_state = next_state

    def return_name(self):
        return self.name

    def return_input(self):
        return self.next_state
