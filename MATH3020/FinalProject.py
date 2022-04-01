# Importing packages
import numpy as np
import matplotlib.pyplot as plt
import time


# Creating Network class
class Simulation:

    # Initializing network with number of computers, number of infected, probability of infecting another computer, and
    # the maximum number of computers that can be cured per day
    def __init__(self, num_comps=20, num_infected=1, infect_prob=.09, max_cure_pd=5):

        # Set variables
        self.tot_infected = num_infected
        self.infect_prob = infect_prob
        self.max_cure_pd = max_cure_pd
        self.num_comps = num_comps

        # List of our computers: Boolean list, whether the system is infected or not: Bool
        self.comp_list = [True] * num_infected + [False] * (num_comps - num_infected)
        self.infected = self.comp_list[0]  # Boolean value indicating network infection
        self.infected_list = list(range(0, num_infected, 1))  # List holding infected indices

        # Variables for each day of a simulation
        self.today = 0  # Day counter for simulations
        self.new_infected = 0  # number of infected people in the current sim
        self.new_cured = 0  # number of cured people in the current sim

    # Method to simulate a day
    def day(self):

        # Resetting the daily counter of infected and cured computers
        self.new_infected = 0
        self.new_cured = 0

        self.infected_list = []

        for num in range(len(self.comp_list)):
            if self.comp_list[num]:
                self.infected_list.append(num)

        # Infection process. Go through the computer list and look for infected computers
        for i in range(len(self.infected_list)):
            for num in range(len(self.comp_list)):
                # num = int(num1)
                if not self.comp_list[num] and np.random.rand(1) < self.infect_prob:
                    # If we get a match add one to relevant counters and change value in computer list
                    self.new_infected += 1
                    self.tot_infected += 1
                    self.comp_list[num] = True
                    self.infected_list.append(num)

        # Cure process. Keep trying curing the maximum number of cured computers per day is reached or all are curred

        while self.new_cured <= self.max_cure_pd and self.tot_infected > 0:
            # Choose a random index in our
            rand_ndx = np.random.randint(len(self.infected_list))
            infected_index = self.infected_list[rand_ndx]
            self.comp_list[infected_index] = False
            self.infected_list.pop(rand_ndx)
            self.new_cured += 1
            self.tot_infected -= 1

    def run(self, days=np.inf):

        self.today = 0
        if days != np.inf:
            for day in range(days):
                self.day()
                self.today += 1
            return

        while self.tot_infected > 0:
            self.day()
            self.today += 1

        return self.today


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
