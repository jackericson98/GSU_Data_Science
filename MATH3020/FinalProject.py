# Importing packages
import numpy as np
import matplotlib.pyplot as plt


# Creating Network class
class Simulation:

    # Initializing network with number of computers, number of infected, probability of infecting another computer, and
    # the maximum number of computers that can be cured per day
    def __init__(self, num_comps=20, num_infected=1, infect_prob=.09, max_cure_pd=5):

        # Set input variables
        self.init_infected = num_infected
        self.infect_prob = infect_prob
        self.max_cure_pd = max_cure_pd
        self.num_comps = num_comps

        # List of our computers: Boolean list, whether the system is infected or not: Bool
        self.comp_list = []
        self.infected_list = []

    # Define our plot method. Since it does not call on the object we declare it as a static method
    @staticmethod
    def plot(num_sims, avg, sim_length_arr, avg_arr):

        # Plot the number of days for each simulation to run
        plt.scatter(np.linspace(1, num_sims, num_sims), sim_length_arr)
        plt.plot(np.linspace(1, num_sims, num_sims), avg_arr, color='r', linewidth=2.0)

        # Plot attributes
        plt.title("Time to clear viruses in days. Average = %3.5f" % avg)
        plt.xlabel("Simulation")
        plt.ylabel("Time (days)")
        plt.legend(["Average", "Time"])

        # Show the plot
        plt.show()

    # Method to simulate a day
    def day(self):

        # Infection process:

        # Go through the infected computer list
        for i in range(len(self.infected_list)):

            # For each infected computer try to infect all other non-infected computers
            for num in range(len(self.comp_list)):

                # Add one to our new infected and total infected
                if self.comp_list[num] or np.random.rand(1) >= self.infect_prob:
                    continue

                # Change the computer list entry for this computer to True (i.e. infected)
                self.comp_list[num] = True
                self.infected_list.append(num)

        # Cure process:

        cured = 0

        # Keep curing computers until we reach the desired number of cured computers or all computers are healthy
        while cured <= self.max_cure_pd and len(self.infected_list) > 0:

            # Choose a random index from our infected computer list, remove that index (pop) and cure the
            # corresponding computer (i.e. set it's value to False)
            self.comp_list[self.infected_list.pop(np.random.randint(len(self.infected_list)))] = False

            # Increment our tallies accordingly
            cured += 1

    # Method for running the simulation
    def run(self):

        # Ask the user how many simulations they want to run
        num_sims = int(input("How many simulations would you like to run?"))

        # Set our average back to 0 and reset our data arrays
        avg = 0
        avg_arr = []
        sim_length_arr = []

        # Run the number of simulations specified
        for i in range(num_sims):

            # Reset our lists for each simulation
            self.comp_list = [True] * self.init_infected + [False] * (self.num_comps - self.init_infected)
            self.infected_list = list(range(0, self.init_infected, 1))

            # Set the day counter to 0
            days = 0

            # Keep running days until all computers are cured
            while len(self.infected_list) > 0:

                # Call the day method and add a day to our counter
                self.day()
                days += 1

            # Update our data
            sim_length_arr.append(days)
            avg = (i * avg + days) / (i + 1)
            avg_arr.append(avg)

            # Update our running print statement to show the current sim number, current sim length & running average
            print("\rSimulation %8d length = %3d days, average = %3f days per simulation" % (i + 1, days, avg),
                  end='')

        # Plot the results
        self.plot(num_sims, avg, sim_length_arr, avg_arr)


# Driver code
Simulation().run()
