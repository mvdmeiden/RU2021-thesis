# RU2021-thesis
This is the repository for my Bachelor's thesis in Artificial intelligence. Here you'll find the code, images, and data used during the project. Below is an overview of what you will find in each of the folders above.

## code
This folder contains all code used during the project. Everything is written in Python 3.7.  
the `MealyMachine.py` file is taken from another repository and served as the basis for the further implementation of the finite state transducers.  
the code for the base agent, found in `Base.py` is outdated. Since the base agent was not used for later testing any adjustments to the agent code needed for the generalist and specialist agents, were not carried out in the base agent class anymore.

## data
Here, all generated data used for the plots is stored. For each distribution of agents, 10 runs were done. The filename of each `.npy` file is structured as follows: `<number of generalists>.<number of specialists>-yyyy-mm-dd.npy`. The data is not viewable raw, but has to be opened in python using Numpy.

## imgs
This folder contains all images used in the thesis paper, as well as plots generated from the data that were not shown in the paper itself.  
The folders with the _averages_ suffix contain the plots where all populations were compared to each other. The other folders have different plots for each different population of agents. The distribution of the agents is given in the file name.