# Importing packages
import numpy as np
import matplotlib.pyplot as plt


# Creating Network class
class Simulation:

    # Initializing network with number of computers, number of infected, probability of infecting another computer, and
    # the maximum number of computers that can be cured per day
    def __init__(self, num_comps=20, num_infected=1, infect_prob=.09, max_cure_pd=5, num_sims=10000):

        # Set input variables
        self.init_infected = num_infected
        self.infect_prob = infect_prob
        self.max_cure_pd = max_cure_pd
        self.num_comps = num_comps
        self.num_sims = num_sims

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
        plt.title("Days to clear network of viruses. Average = %3.5f" % avg)
        plt.xlabel("Simulation")
        plt.ylabel("Time (days)")
        plt.legend(["Average", "Time"])

        # Show the plot
        plt.show()

    # Define our choices method
    def choices(self):

        # Ask the user if they want to make any changes with the simulation
        changes = input("Which of the following would you like to change:\n"
                        "1. Number of computers    2. Infected computers    3. Infection Rate    "
                        "4. Number of simulations\n").lower()

        # Create a list of changes from users input string
        my_changes = changes.split(', ')

        # Input pools for each
        num_comps = ["number of computers", '1.', '1', 'computers']
        infected_computers = ['infected computers', 'number infected', 'infected', '2.', '2']
        infection_rate = ['infection rate', 'infection', '3', '3.']
        num_sims = ["number of simulations", 'num sims', '4.', '4']

        # Check if user indicated to change the number of computers
        if any(x in num_comps for x in my_changes):
            self.num_comps = int(input("How many computers would you like to simulate?"))

        # Check if user indicated to change the number of infected computers
        if any(x in infected_computers for x in my_changes):
            self.init_infected = int(input("How many infected computers would you like to start with?"))

        # Check if user indicated to change the infection rate
        if any(x in infection_rate for x in my_changes):
            self.infect_prob = float(input("What is the infection rate you would like to test?"))

        # Check if user indicated to change the number of simulations
        if any(x in num_sims for x in my_changes):
            self.num_sims = int(input("How many simulations would you like to run?"))

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

        choices = input("\n1. Number of computers = {}\n2. Initially infected computers = {}\n3. Infection Rate = {}\n"
                        "4. Number of simulations = {}\n5. Number of computers repaired daily = {}\n\n"
                        "Would you like to change any of the above settings for your simulation? (y/n):"
                        .format(self.num_comps, self.init_infected, self.infect_prob, self.num_sims, self.max_cure_pd))

        if choices.lower() != 'n':
            self.choices()

        # Set our average back to 0 and reset our data arrays
        avg = 0
        avg_arr = []
        sim_length_arr = []

        # Run the number of simulations specified
        for i in range(self.num_sims):

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
            print("\rSimulation #: %6d, length = %3d days, average = %3f days per simulation" % (i + 1, days, avg),
                  end='')

        # Plot the results
        self.plot(self.num_sims, avg, sim_length_arr, avg_arr)


# Driver code
mySim = Simulation()
mySim.run()
