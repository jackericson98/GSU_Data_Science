# Importing packages
import numpy as np
import matplotlib.pyplot as plt
import time


# Creating Network class
class Simulation:

    # Initializing network with number of computers, number of infected, probability of infecting another computer, and
    # the maximum number of computers that can be cured per day
    def __init__(self, num_comps=20, num_infected=1, infect_prob=.09, max_cure_pd=5):

        # Set input variables
        self.tot_infected = num_infected
        self.infect_prob = infect_prob
        self.max_cure_pd = max_cure_pd
        self.num_comps = num_comps

        # List of our computers: Boolean list, whether the system is infected or not: Bool
        self.comp_list = [True] * num_infected + [False] * (num_comps - num_infected)
        self.infected = self.comp_list[0]  # Boolean value indicating network infection
        self.infected_list = list(range(0, num_infected, 1))  # List holding infected indices

    # Method to simulate a day
    def day(self):

        # Resetting the daily counter of infected and cured computers
        new_infected = 0
        new_cured = 0
        self.infected_list = []
        self.tot_infected = 0

        # Create a list of indices for infected computers our computer list
        for num in range(len(self.comp_list)):
            if self.comp_list[num]:
                self.infected_list.append(num)
                self.tot_infected += 1

        # Infection process:
        # Go through the infected computer list
        for i in range(len(self.infected_list)):
            # For each infected computer try to infect all other non-infected computers
            for num in range(len(self.comp_list)):
                # If the computer isn't already infected and our random number is larger than our infected probability
                # threshold infect that computer
                if not self.comp_list[num] and np.random.rand(1) < self.infect_prob:
                    # Add one to our new infected and total infected
                    new_infected += 1
                    self.tot_infected += 1
                    # Change the computer list entry for this computer to True (i.e. infected)
                    self.comp_list[num] = True
                    self.infected_list.append(num)

        # Cure process:
        # Keep curing computers until we reach the desired number of cured computers or all computers are healthy
        while new_cured <= self.max_cure_pd and self.tot_infected > 0:
            # Choose a random index from our infected computer list, remove that index (pop) and cure the
            # corresponding computer (i.e. set it's value to False)
            self.comp_list[self.infected_list.pop(np.random.randint(len(self.infected_list)))] = False
            # Increment our tallies accordingly
            new_cured += 1
            self.tot_infected -= 1

    # Method for running the simulation
    def run(self):

        # Set the day counter to 0
        days = 0
        # Keep running days until all computers are cured
        while self.tot_infected > 0:
            # Call the day method
            self.day()
            # Add a day to our day counter
            days += 1

        return days


# Driver code
num_sims = int(input("How many simulations would you like to run?"))

avg = 0
avg_arr = []
sim_length_arr = []

for i in range(num_sims):
    myNet = Simulation(20, 1)
    sim_length = myNet.run()
    avg = (i * avg + sim_length) / (i + 1)
    avg_arr.append(avg)
    sim_length_arr.append(sim_length)

    print("\rSimulation %8d length = %3d days, average = %3f days per simulation" % (i + 1, sim_length, avg), end='')

plt.scatter(np.linspace(1, num_sims, num_sims), sim_length_arr)
plt.plot(np.linspace(1, num_sims, num_sims), avg_arr, color='r', linewidth=2.0)

plt.title("Time to clear viruses in days")
plt.xlabel("Simulation")
plt.ylabel("Time (days)")
plt.legend(["Average", "Time"])
plt.show()
