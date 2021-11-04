class State(object):

    name = 0
    next_state= []

    def __init__(self, name, next_state):
        self.name = name
        self.next_state = next_state

    def return_name(self):
        return self.name

    def return_dictionary(self):
        return self.next_state

    def show(self):
        full_string = ""
        full_string = full_string + self.name + ", "
        full_string = full_string + str(self.next_state)
        print(full_string)
