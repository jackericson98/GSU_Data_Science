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
    def plot(self, avg, sim_length_arr, avg_arr):

        # Plot the number of days for each simulation to run
        plt.scatter(np.linspace(1, self.num_sims, self.num_sims), sim_length_arr)
        plt.plot(np.linspace(1, self.num_sims, self.num_sims), avg_arr, color='r', linewidth=2.0)

        # Plot attributes
        plt.title("Days to clear network of viruses. Average = %3.5f" % avg)
        plt.xlabel("Simulation")
        plt.ylabel("Time (days)")
        plt.legend(["Average", "Time"])

        # Show the plot
        plt.show()

    # Define our choices method
    def choices(self):

        input_found = False

        # Ask the user if they want to make any changes with the simulation
        choices = input("\n Default settings: \n    1. Number of computers = {}\n    2. Initially infected computers"
                        " = {}\n    3. Infection Rate = {}\n    4. Number of simulations = {}\n    5. Number of "
                        "computers repaired daily = {}\n\nWould you like to change any of the above settings? If so, "
                        "which setting(s)? (use numbers separated by commas or 'all') Type 'n' if not.\n\n"
                        .format(self.num_comps, self.init_infected, self.infect_prob, self.num_sims,
                                self.max_cure_pd)).lower()  #

        if choices == 'n':
            input_found = True

        elif choices == 'y':
            choices = input("Which setting(s)? (use numbers separated by commas or 'all')\n")

        # Create a list of changes from users input string
        choice_list = choices.split(',')  # Splits by space comma space, comma space or comma

        # Input pools for each
        num_comps_keys = ['1.', '1', ' 1.', ' 1', 'all']
        infected_computers_keys = ['2.', '2', ' 2.', ' 2', 'all']
        infection_rate_keys = ['3', '3.', ' 3.', ' 3', 'all']
        num_sims_keys = ['4.', '4', ' 4.', ' 4', 'all']
        mc_pd_keys = ['5', '5.', ' 5.', ' 5', 'all']

        # Check if user indicated to change the number of computers
        if any(x in num_comps_keys for x in choice_list):
            input_found = True
            self.num_comps = int(input("1. How many computers would you like to simulate?\n"))

        # Check if user indicated to change the number of infected computers
        if any(x in infected_computers_keys for x in choice_list):
            input_found = True
            self.init_infected = int(input("2. How many infected computers would you like to start with?\n"))

        # Check if user indicated to change the infection rate
        if any(x in infection_rate_keys for x in choice_list):
            input_found = True
            self.infect_prob = float(input("3. What is the infection rate you would like to test?\n"))

        # Check if user indicated to change the number of simulations
        if any(x in num_sims_keys for x in choice_list):
            input_found = True
            self.num_sims = int(input("4. How many simulations would you like to run?\n"))

        # Check if user indicated to change the number of repaired computers per day
        if any(x in mc_pd_keys for x in choice_list):
            input_found = True
            self.max_cure_pd = int(input("5. How many repaired computers per day?\n"))

        # Catch all other
        if not input_found:
            print("\nSorry \"{}\" is not a valid input. Please try again. \n".format(choices))
            self.choices()

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

        self.choices()

        # Set our average back to 0 and reset our data arrays
        avg = 0
        avg_arr = []
        sim_length_arr = []

        # Run the number of simulations specified
        for i in range(self.num_sims):

            # Reset our lists and day counter for each simulation
            self.comp_list = [True] * self.init_infected + [False] * (self.num_comps - self.init_infected)
            self.infected_list = list(range(0, self.init_infected, 1))
            days = 0

            # Keep running days until all computers are cured
            while len(self.infected_list) > 0 and days <= 1000000:
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
        self.plot(avg, sim_length_arr, avg_arr)

        # Ask the user if they would like to run another simulation.
        cont = input("\n\nWould you like to run another simulation?\n")
        if cont.lower() == 'y':
            self.run()


# Driver code
mySim = Simulation()
mySim.run()
