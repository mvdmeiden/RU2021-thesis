# Author
# Mieke van der Meiden - Radboud University, The Netherlands
# email: mieke.vandermeiden@ru.nl

# Imports
import random as rnd
import numpy as np
from Machine import Machine
from Specialist import Specialist
from Generalist import Generalist


# MULTI-AGENT SIMULATIONS
# create the world FST and base knowledge machines
sl = 30
world = Machine(50, max_length=sl)
while len(world.states) < 5:
    world = Machine(50, max_length=sl)
world_size = len(world.states)

world.show()

# agent generation
agents = [[], [], [], [], [], [], [], [], [], []]
num_agents = 100     # total number of agents
split = 5            # number of specialists in a group(10 - split = number of generalists in a group)
for i in range(num_agents):
    group = i//10
    if i % 10 < split:
        agents[group].append(Specialist(i, comp_limit=2*world_size, acceptance=0.9))
    else:
        agents[group].append(Generalist(i, comp_limit=2*world_size, acceptance=0.9))

# initialize parameters
largest_c = 0
num_machines = 0
num_iters = 0
machines = [[], [], [], [], [], [], [], [], [], []]
num_satisfied = 0

# setup output to save results
results = None
path = 'output.npy'

while num_iters < 100 and num_satisfied < num_agents:
    row = [0] * num_agents
    for i, group in enumerate(agents):
        for a in group:
            prev = results[num_iters-1][a.id] if results is not None else None
            if not a.satisfied:
                if a.type == 'S':
                    m, c = rnd.choice(machines[i]) if machines[i] else (None, 0)
                    if c > a.acceptance:
                        a.satisfied = True
                    else:
                        data = world.observe(n=100)
                        m, c, t = a.act(m, data, method='accuracy')

                elif a.type == 'G':
                    g1 = rnd.choice(machines)
                    m1, c1 = rnd.choice(g1) if g1 else (None, 0)
                    g2 = rnd.choice(machines)
                    m2, c2 = rnd.choice(g2) if g2 else (None, 0)
                    if c1 > a.acceptance:
                        a.satisfied = True
                        m = m1
                        c = c1
                    elif c2 > a.acceptance:
                        a.satisfied = True
                        m = m2
                        c = c2
                    else:
                        data = world.observe(n=100)
                        m, c, t = a.act(m1, m2, data, method='accuracy')  # if machines else None, 0, a.type

                else:
                    print('unrecognized scientist type.')
                    m, c, t = None, 0, None

                m_size = len(m.states) if m is not None else 0
                new = [world_size, a.type, m, m_size, c, a.satisfied]

                if new[2] is not None:
                    print("{}'s accuracy: {}".format(a.id, c))
                    machines[i].append((m, c))
                    num_machines += 1
                if c > largest_c:
                    largest_c = c

                if a.satisfied:
                    print("I am satisfied with my machine. Let me go and tell all the others in my group.")
                    for aa in group:
                        aa.satisfied = True
                        row[aa.id] = new
                        num_satisfied += 1
                    break

                row[a.id] = new

            else:
                row[a.id] = prev

        if len(machines[i]) > 100:
            del machines[i][:10]

    results = np.vstack([results, [row]]) if results is not None else np.array([row])
    num_iters += 1

# some information about the run
print("largest found accuracy: ", largest_c)
print("amount of machines made: ", num_machines)
print("amount of satisfied agents: ", num_satisfied)
print("amount of iterations: ", num_iters)

# save the results array locally
np.save(path, results)
