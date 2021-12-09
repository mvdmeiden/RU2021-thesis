# Author
# Mieke van der Meiden  Radboud University, The Netherlands

# Imports
import numpy as np
import random as rnd
from Machine import Machine
from Base import Base
from Specialist import Specialist
from Generalist import Generalist


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
test = Machine(50, input_alphabet=['1', '0'])
test.show()
# print(test.emptytrans)
print()
data = generate_data(100, 3, 10, test)
data = np.array(data)
# print(data)

# a = Generalist(0, data, comp_limit=10, acceptance=0.5)
# m1 = Machine(3)
# m2 = Machine(8)
#
# m, c, t = a.act(m1, m2)
# m.show()


# MULTI-AGENT IMPLEMENTATION
agents = []
machines = []
num_agents = 3
for i in range(num_agents):
    agents.append(Specialist(i, data, comp_limit=5, acceptance=0.9))

agents.append(Generalist(num_agents, data, comp_limit=5, acceptance=0.9))

finished = False
largest_c = 0
while not finished:
    for s in agents:
        if s.type == 'S':
            m, c, t = s.act(rnd.choice(machines)) if machines else s.act(None)
        elif s.type == 'G':
            m, c, t = s.act(rnd.choice(machines), rnd.choice(machines)) if machines else s.act(None, None)
        else:
            print('unrecognized scientist type.')
            m, c, t = None, 0, None
        # m.show()
        print("{}'s accuracy: {}".format(s.id, c))
        if m is not None:
            machines.append(m)
        if c > largest_c:
            largest_c = c
        if s.satisfied:
            print("final accuracy: {}, found by {}".format(c, t))
            m.show()
            finished = True
            break
        if len(machines) > 10000:
            finished = True
            print("largest found accuracy: ", largest_c)
            break





