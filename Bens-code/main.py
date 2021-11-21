from Machine import Machine
from Agent import Agent
import random

#Main experiment environment

if __name__ == "__main__":

    # Parameters
    ACCEPTANCE_THRESHOLD = 0.65
    COMPLEXITY_LIMIT = 5
    DATA_LIMIT = 10
    dictionary = ['a', 'b']
    data = "abbaabababa"
    data_pool = []
    fsm_pool = []

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

    # Initialize Agents

    agent_rationale = Agent(ACCEPTANCE_THRESHOLD, COMPLEXITY_LIMIT, dictionary)
    agent_neutral = Agent(ACCEPTANCE_THRESHOLD, COMPLEXITY_LIMIT, dictionary)
    agent_non_rationale = Agent(ACCEPTANCE_THRESHOLD, COMPLEXITY_LIMIT, dictionary)

    # Run Experimental setup

#    while agent_1.get_acceptance() < ACCEPTANCE_THRESHOLD and agent_1.get_states() < COMPLEXITY_LIMIT:
#        agent_1.refer_on(data, machine_1)


    #Gather results

    agent_rationale.print_results()
    agent_neutral.print_results()
    agent_non_rationale.print_results()
