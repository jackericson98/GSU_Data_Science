# Import Numpy so we can create random array of grades
import numpy as np


# Create grade statistics class
class GradeStatistics:
    """(.mean(), .median(), .mode(), .std() (standard deviation) or .variance()) This
    class can be used to return grade statistics for an array of grades."""

    # Initialize the class with raw grades, integer grades and a dictionary
    def __init__(self, grades):
        self.grades = grades
        self.int_grades = self.grades.astype(int)
        self.my_dic = {}

    # Create a dictionary to be used for our mode method
    def create_dic(self):

        # Go through the integer grades and count instances of each grade
        for element in self.int_grades:

            # If we find the grade, add one to it's count
            if element in self.my_dic:
                self.my_dic[element] += 1

            # If we don't find the grade, add it to the dictionary with a value of 1
            else:
                self.my_dic[element] = 1

    # Define our mean method
    def mean(self):
        return sum(self.grades) / len(self.grades)

    # Define our median method
    def median(self):
        mid = len(self.grades) // 2
        return self.grades[mid]

    # Define our mode method
    def mode(self):

        # Start by creating the dictionary
        self.create_dic()

        # Find the most common grade and return it
        return max(self.my_dic, key=self.my_dic.get)

    # Define our standard deviation method
    def std(self):

        # We first need to call our mean method
        mean = self.mean()

        # Calculate the variations of each value
        vars = [((element - mean) ** 2) for element in self.grades]

        # Calculate the standard deviation from the variances
        std = (sum(vars) / len(self.grades)) ** (0.5)
        return std

    # Define our variance method
    def variance(self):

        # Variance is just standard deviation squared
        return self.std() ** 2


# Create our data
grades = np.random.rand(100) * 100

# Create our Grade Statistics for our data
stats = GradeStatistics(grades)



