from Machine import Machine
from Agent import Agent

#Main experiment environment

if __name__ == "__main__":

#Parameters
    ACCEPTANCE_THRESHOLD = 0.6
    COMPLEXITY_LIMIT = 5
    DATA_LIMIT = 10
    dictionary = ['a', 'b']
    data = 0

#Initialize Machine pool

    machine_1 = Machine()
    machine_1.define_random_dictionary()
    machine_1.show_dictionary()

#Initialize Agents
    agent_1 = Agent()
    agent_2 = Agent()

#Run Experimental setup

    while agent_1.get_acceptance() < ACCEPTANCE_THRESHOLD and agent_1.get_states() < COMPLEXITY_LIMIT:
        agent_1.refer_on(data, machine_1)


#Gather results

    agent_1.print_results()
