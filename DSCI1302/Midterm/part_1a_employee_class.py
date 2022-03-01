class Employee:
    """Parameters: {Name, Year of Joining, Address, Salary, Hours Worked per Day}
        Class used to create an employee and assign work information to."""

    def __init__(self, name=None, yoj=2022, adr=None, sal=0, hrs_day=0):
        self.sal = sal
        self.hrs_day = hrs_day
        self.name = name
        self.yoj = yoj
        self.adr = adr

    def getInfo(self, sal, hrs_day):

        """Parameters: {Salary, Hours Worked per Day}. Takes the salary and
        number of hours worked per day as parameters and assigns them to employee"""

        self.sal = sal
        self.hrs_day = hrs_day
        print("Employee's sal is: {}".format(self.sal))

    def AddSal(self):

        """Adds $10 to employee's salary if they make less than $500"""

        if self.sal < 500:
            self.sal += 10
        print("Employee's sal is: {}".format(self.sal))

    def AddWork(self):

        """Adds $5 to employee's salary if they work 6 hours a day or more."""

        if self.hrs_day >= 6:
            self.sal += 5
        print("Employee's salary is: {}".format(self.sal))

    def printEmployee(self):

        """Prints employee name, year of joining and address."""

        print('Employee Information:\n\n\tName:\t\tYear of Joining:\tadr:\n'
              '\t{}\t\t{}\t\t\t{}'.format(self.name, self.yoj, self.adr))
