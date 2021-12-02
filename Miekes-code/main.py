# Author
# Mieke van der Meiden  Radboud University, The Netherlands

# Imports
import numpy as np
import random as rnd
from Machine import Machine
from Agent import Agent


def generate_data(n, min_length, max_length, machine):
    data = []
    while n != 0:
        string = ''
        for i in range(0, rnd.randint(min_length, max_length)):
            string = string + rnd.choice(machine.input_alphabet)
        data.append([string, machine.run_input(string)])
        n = n - 1

    return data


# The rest of the code
test = Machine(8)
test.show()
print(test.emptytrans)
print()
data = generate_data(100, 3, 10, test)
data = np.array(data)
# print(data)

a = Agent(0, data, comp_limit=10, acceptance=0.7)
a.given_machine = Machine(0)
while not a.satisfied and len(a.given_machine.states) < a.comp_limit:
    a.add_one_state(a.given_machine)
    a.run_machine()
    # print(a.check_machine('hamming'))

# a.current_machine.show()




