import numpy as np


class Network:

    def __init__(self, num_comps=20, num_infected=1):

        self.infected = True  #
        self.tot_infected = num_infected
        self.comp_list = []  # List of bool values: True = infected

        self.today = 0
        self.num_infected = 0
        self.num_cured = 0

        for i in range(num_infected):
            self.comp_list.append(True)
        for i in range(num_infected, num_comps):
            self.comp_list.append(False)

    # Function for testing if our entire network is infected or not
    def isInfected(self):
        for comp in self.comp_list:
            if comp:
                return True
        return False

    def runSim(self, days=np.inf):
        self.today = 0
        if days != np.inf:
            for day in range(days):
                self.day()
                self.today += 1
                print("Day: {}. {} new cases. {} Total".format(self.today, self.num_infected, self.tot_infected))
            return

        while self.infected:
            self.day()
            self.today += 1
            print("Day: {}. {} new cases. {} Total".format(self.today, self.num_infected, self.tot_infected))

            if self.tot_infected <= 0:
                print("finished")
                self.infected = False
        return

    def day(self):
        self.num_infected = 0
        self.num_cured = 0
        for comp in self.comp_list:
            if comp:
                for i in range(len(self.comp_list)):
                    if not self.comp_list[i] and np.random.rand(1) < .09:
                        self.num_infected += 1
                        self.tot_infected += 1
                        self.comp_list[i] = True

        num_curable = min(self.tot_infected, 5)
        while self.num_cured <= num_curable - 1:
            rand_ndx = np.random.randint(20)
            if self.comp_list[rand_ndx]:
                self.comp_list[rand_ndx] = False
                self.num_cured += 1
                self.tot_infected -= 1

# Driver code
myNet = Network(20, 1)

myNet.runSim()