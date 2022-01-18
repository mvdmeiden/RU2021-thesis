# Copied in part from https://github.com/Lemon-cmd/Moore-Mealy-Machines-Python/blob/master/Moore%26Mealy.py
# A simple binary mealy machine. To be adjusted into what we want to do.


class State(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self, name, next_state):
        self.name = name
        self.next_state = next_state

    def return_name(self):
        return self.name

    def return_input(self):
        return self.next_state


# Example
# s0 = State('s0', {0:('s1', 1), 1:('s2',0)})

def add_states():
    num_of_states = int(input("How many states would you like: "))

    count = num_of_states
    statesL = []

    while (count != 0):
        name = str(input("Name of state: "))
        inputs = str(input("Inputs and outputs of the state 0:x, o1 and 1:y,o2 : "))
        x, o1, y, o2 = inputs.split(' ')

        name = State(str(name), {0: (str(x), int(o1)), 1: (str(y), int(o2))})
        statesL.append(name)

        count = count - 1

    return statesL


statesL = add_states()


def iterate_through_states(statesL, inputString):
    # set current state
    current_state = statesL[0]
    # create an empty string for concatenation
    outputString = ''

    # loop through inputString
    for i in range(len(inputString)):

        temp = inputString[i]  # temp for an element in the inputString

        Input = current_state.return_input()  # a variable for the dictionary of the current state
        # Example of Input
        # {0:('s1', 1), 1:('s2',0)}

        # loop through the current state's dictionary
        # do calculation when current element in inputString is equal to a key in the inputs dict of statesL[i]
        # grab the item and add it to the empty string
        for item in Input:

            if int(temp) == item:
                output = Input[item]
                outputString = outputString + str(output[1])
                next_state = output[0]
                for state in statesL:
                    if state.return_name() == next_state:
                        current_state = state
                        break

    # return back to the first loop and continue on until inputString is done looping
    print("Output String: ", outputString)


iterate_through_states(statesL, '10100')
