# Authors
# Mieke van der Meiden  Radboud University, The Netherlands
# Benjamin Robijn       Radboud University, The Netherlands

# Imports
import numpy as np
from Machine import Machine
from Agent import Agent

# The rest of the code
datatest = [['00110', '01101'],
            ['0101', '1000'],
            ['110', '111']]
datatest = np.array(datatest)

start = Machine(5)
start.show()
print()

agent = Agent(0, datatest, acceptance=0.3)
agent.current_machine = start

print(agent.check_machines())

# results = []
# results.append(test.run_input('11011'))
# results.append(test.run_input('10110'))
# results.append(test.run_input('001011'))
# results.append(test.run_input('01010011'))
# print(results)
