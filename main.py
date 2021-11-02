# Authors
# ...
# ...

# Imports
import numpy as np

# The rest of the code

class Agent:

    # constructor
    def __init__(self, i,  D, M_prime): #each d in D is a pair of (s, b) [situation, behaviour] and M_prime is a pair (M, accuracy)
        self.id = i


class Transition:
    def __init__(self, next_state, output):
        self.next = next_state
        self.output = output


class Environment:
    # constructor
    def __init__(self, numstates, alphabetlength):
        self.transitions = np.full((numstates, alphabetlength), None)


# all actions go down here
num_of_states = int(input("How many states would you like: "))
test = np.empty(num_of_states, 2)

print(test)
test[0][0] = Transition(0, 0)
test[0][1] = Transition(1, 1)
test[1][0] = Transition(1, 1)
test[1][1] = Transition(2, 0)
test[2][0] = Transition(2, 1)
test[2][1] = Transition(0, 0)

inputString = input("input: ")
outputString = ''
currentState = 0

for i in range(len(inputString)):
    temp = inputString[i]
    outputChar, nextState = test[currentState].


