# Author
# Mieke van der Meiden  Radboud University, The Netherlands

# Imports
import numpy as np
import random as rnd
from Machine import Machine
from Base import Base
from Specialist import Specialist


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

a = Specialist(0, data, comp_limit=10, acceptance=0.5)
m = Machine(0)
result = m, None, None
while not a.satisfied and len(result[0].states) < a.comp_limit:
    result = a.act(result[0])
    print(result[1])

# print(a.output())
# print(a.current_machine.emptytrans)




