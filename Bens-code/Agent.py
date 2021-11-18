from Machine import Machine
import statistics
from State import State


class Agent:
    # Parameters
    # ______________________
    accuracy = 0  # !!!!
    number_of_states = 0

    agent_machine = None
    # ______________________

    dictionary = None
    bias = 0

    # ____________________________Agent_Initialization_______________________________________

    # Initialization
    def __init__(self, dictionary, bias_factor):

        self.dictionary = dictionary
        self.bias = bias_factor
        self.current_machine = Machine(dictionary)
        pass

    # Supports incremental building of the Agent's FSM by means of probabilistic logic
    def build_model_incrementally(self):
        new_state = self.current_machine.add_incremental_layer(self.number_of_states + 1)
        self.current_machine.transition_dictionary.append(new_state)
        self.number_of_states = self.number_of_states + 1
        pass


#    while agent_neutral.accuracy < ACCEPTANCE_THRESHOLD and agent_neutral.number_of_states < COMPLEXITY_LIMIT:
#        agent_neutral.build_model_incrementally()
 #       if agent_neutral.check_model_accuracy(fsm1, data_pool) < agent_neutral.accuracy:
#          # revert and choose other option
#        pass

    # Accuracy checker compares outputs between own model and base machine, returns averaged accuracy over some data set
    def check_model_accuracy(self, other_model, data):
        agent_model = self.current_machine
        machine_model = other_model
        accuracy_list = []

        for d in data:
            agent_output = agent_model.run_input(d)
            model_output = machine_model.run_input(d)
            accuracy = (sum(agent_output[i] != model_output[i] for i in range(len(model_output)))) / len(model_output)
            accuracy_list.append(accuracy)

        averaged_accuracy = statistics.mean(accuracy_list)
        return averaged_accuracy

    # Output printer consistent with output FSM and output accuracy
    def print_results(self):
        print("Agent found machine: ")
        print(self.current_machine)
        print("_________")
        print("With accuracy rating:" + self.current_accuracy.__str__())
        print("")
        return 0
