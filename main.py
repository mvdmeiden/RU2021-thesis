# Authors
# Mieke van der Meiden  Radboud University, The Netherlands
# Benjamin Robijn       Radboud University, The Netherlands

# Imports
import numpy as np
from Machine import Machine
from Agent import Agent

# The rest of the code
test = Machine(2)
agent = Agent(0)
test.show()

print()
agent.generate_machine_onestate()
agent.current_machine.show()

print()
test.show()

# results = []
# results.append(test.run_input('11011'))
# results.append(test.run_input('10110'))
# results.append(test.run_input('001011'))
# results.append(test.run_input('01010011'))
# print(results)
