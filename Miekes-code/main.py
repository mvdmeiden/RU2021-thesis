# Authors
# Mieke van der Meiden  Radboud University, The Netherlands
# Benjamin Robijn       Radboud University, The Netherlands

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
datatest = [['00110', '01101'],
            ['0101', '1000'],
            ['110', '111']]
datatest = np.array(datatest)

test = Machine(2)
test.show()
print()
data = generate_data(10, 3, 10, test)
data = np.array(data)
# test.show()
# print(data)

a = Agent(0, data)
changed = a.add_one_state()

changed.show()

