class State(object):

    def __init__(self, id, transitions):
        self.id = id
        self.transitions = transitions

    def return_name(self):
        return self.id

    def return_transitions(self):
        return self.transitions

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.id + str(self.transitions)
