# Authors
# ...
# ...

# Imports
import numpy as np
from Machine import Machine
from Agent import Agent

# The rest of the code
test = Machine(4)
agent = Agent()
test.show()

results = []
results.append(test.run_input('12011'))
results.append(test.run_input('10110'))
results.append(test.run_input('001011'))
results.append(test.run_input('01010011'))
print(results)




## all actions go down here