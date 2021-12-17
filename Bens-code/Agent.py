from Machine import Machine
import statistics
import numpy as np
import State as State
import copy as copy


class Agent:
    # Parameters
    # ______________________
    accuracy = 0
    number_of_states = 0
    # ______________________
    # Pools results over all FSTs
    results_pool = []
    # ______________________
    alphabet = None
    BIAS = 0
    agent_machine = None

    # ____________________________Agent_Initialization__________________________________________________________________

    # Initialization
    def __init__(self, alphabet, bias_factor):
        self.alphabet = alphabet
        self.BIAS = bias_factor
        self.agent_machine = Machine(alphabet)
        pass

    # Agent behaviour that defines how the agent builds an incrementally designed FST
    def build_model(self, unidentified_machine, data, comp_lim):

        # Variable used for reverting model if needed

        previous_state = copy.deepcopy(self.agent_machine)

        if self.number_of_states == 0:
            base_state = State.State('q0', {})
            self.agent_machine.transition_table.append(base_state)

        # Check all future options and choose one based on percentage information gain and the bias factor

        all_possible_machines = self.agent_machine.check_all_options()

        # Add probabilities associated with all created machines

        accuracy_list = []

        for m in all_possible_machines:
            temp_agent = Agent(self.alphabet, self.BIAS)
            temp_agent.agent_machine = m
            model_accuracy = temp_agent.check_model_accuracy(unidentified_machine, data)
            accuracy_list.append(model_accuracy)

        biased_options = self.softmax(accuracy_list).tolist()

        self.agent_machine = np.random.choice(all_possible_machines, 1, p=biased_options)
        self.agent_machine = self.agent_machine[0]

        # Adjust accuracy and complexity

        self.accuracy = self.check_model_accuracy(unidentified_machine, data)
        self.number_of_states = len(self.agent_machine.transition_table)

        if self.number_of_states == comp_lim + 1:
            self.agent_machine = copy.deepcopy(previous_state)

        pass

    # Accuracy checker compares outputs between own model and base machine, returns averaged accuracy over some data set
    def check_model_accuracy(self, other_model, data):
        agent_model = self.agent_machine
        machine_model = other_model
        accuracy_list = []

        # Compare outputs of agent to outputs of randomly generated FSM and return average over data set
        for d in data:
            model_output = machine_model.run_input(d)
            agent_output = agent_model.run_input(d)

            if model_output == "" and not agent_output == "":
                accuracy = 0
            elif not model_output == "" and agent_output == "":
                accuracy = 0
            elif model_output == "" and agent_output == "":
                accuracy = 1
            else:
                accuracy = (sum(agent_output[i] == model_output[i] for i in
                                range(len(min(agent_output, model_output, key=len)))) / len(
                    min(agent_output, model_output, key=len)))

            accuracy_list.append(accuracy)

        averaged_accuracy = statistics.mean(accuracy_list)
        return averaged_accuracy

    # Output printer consistent with output FSM and output accuracy
    def print_results(self):
        print("Agent found machine: ")
        self.agent_machine.show_fsm()
        print("_________")
        print("With accuracy rating: " + self.accuracy.__str__())
        print("")
        return 0

    # Softmax a probability distribution given the bias value of the agent
    def softmax(self, prop_dis):
        prop_dis = np.array(prop_dis)
        e_x = np.exp(prop_dis / self.BIAS)
        return e_x / e_x.sum()

    # Reset all variables for purpose of new model iteration
    def reset(self):
        self.number_of_states = 0
        self.accuracy = 0
        self.agent_machine = Machine(self.alphabet)
        self.agent_machine.transition_table = []

    # Simple checker for model stop conditions
    def model_not_done(self, comp_lim, acc_thresh):
        return self.number_of_states < comp_lim + 1 and self.accuracy < acc_thresh
