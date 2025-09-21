import random

import matplotlib.pyplot as plt
import numpy as np
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    for _ in range(CURRENTRABBITPOP):
        if CURRENTRABBITPOP < MAXRABBITPOP:
            birth_probe = 1.0 - (CURRENTRABBITPOP / MAXRABBITPOP)
            if random.random() < birth_probe:
                CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    new_foxpop = CURRENTFOXPOP

    for _ in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            hunt_prob = CURRENTRABBITPOP / MAXRABBITPOP
            if random.random() < hunt_prob:
                CURRENTRABBITPOP -= 1
                if random.random() < 1/3:
                    new_foxpop += 1
            else:
                if random.random() < 0.1 and new_foxpop > 90:
                    new_foxpop -= 1
        else:
            if random.random() < 0.1 and new_foxpop > 90:
                new_foxpop -= 1

    CURRENTFOXPOP = new_foxpop


    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbit_populations = []
    fox_populations = []

    for _ in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)

    return rabbit_populations, fox_populations


rabbits, foxes = runSimulation(200)
# plt.plot(rabbits, label='Rabbits')
# plt.plot(foxes, label='Foxes')
# plt.xlabel('Time Steps')
# plt.ylabel('Population')
# plt.legend()
# plt.title('Rabbit and Fox Population Over Time')
# plt.show()

time_steps = list(range(len(rabbits)))

rabbit_coeff = np.polyfit(time_steps, rabbits, 2)
fox_coeff = np.polyfit(time_steps, foxes, 2)

rabbit_fit = np.polyval(rabbit_coeff, time_steps)
fox_fit = np.polyval(fox_coeff, time_steps)

plt.plot(time_steps, rabbits, label='Rabits (real)', color='green', alpha=0.6)
plt.plot(time_steps, foxes, label='Foxes (real)', color='orange', alpha=0.6)

plt.plot(time_steps, rabbit_fit, label='Rabbits (fit)', color='darkgreen', linestyle='--')
plt.plot(time_steps, fox_fit, label='Foxes (fit)', color='red', linestyle='--')

plt.xlabel('Time Steps')
plt.ylabel('Population')
plt.title('Rabbit and Fox Population Over Time (with 2nd-degree Fit')
plt.legend()
plt.grid(True)
plt.show()