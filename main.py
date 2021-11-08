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

#Initialize FSM pool

    fsm_1 = Machine()
    fsm_1.define_random_fsm()
    fsm_1.show_fsm()

#    fsm_1.run_input("abbabbabbbabbb")

#Initialize Agents
    agent_1 = Agent()
    agent_2 = Agent()

#Run Experimental setup

#    while agent_1.get_acceptance() < ACCEPTANCE_THRESHOLD and agent_1.get_states() < COMPLEXITY_LIMIT:
#        agent_1.refer_on(data, machine_1)


#Gather results

#   agent_1.print_results()
