from Machine import Machine
from Agent import Agent
import random

# Main environment

if __name__ == "__main__":

    # -------------------Model Parameters________________________

    # Internal limiters
    ACCEPTANCE_THRESHOLD = 0.65
    COMPLEXITY_LIMIT = 5
    DATA_LIMIT = 10

    # Finite State Machine dictionary
    dictionary = ['a', 'b']

    # Data and Finite State Machines
    data_pool = []
    fsm_pool = []

# ______________________________________________________

    # Initialize data pool

    for _ in range(1, 31):
        data_point = ""
        count = random.randint(3, DATA_LIMIT)

        while count > 0:
            data_point = data_point + random.choice(dictionary)
            count = count - 1
        data_pool.append(data_point)

    # Initialize FSM pool

    for i in range(0, 5):
        fsm_pool.append(Machine(dictionary))
        fsm_pool[i].define_random_fsm()

    fsm1 = Machine(dictionary)
    fsm1.define_random_fsm()

    # Initialize Agents

    agent_rationale = Agent(dictionary, 1)
    agent_neutral = Agent(dictionary, 0.5)
    agent_non_rationale = Agent(dictionary, 0)

    # Run Experimental setup

    agent_neutral.build_model_incrementally()

    # Gather results

    agent_neutral.print_results()
