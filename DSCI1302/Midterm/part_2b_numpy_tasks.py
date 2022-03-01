import numpy as np


# Array with values that are spaced linearly in a specified interval 
# between 0.0 100.0 as a numpy.float64, over 25 values:

myArray = np.linspace(0, 100, 25)


# Combine the values into a larger array:

a = np.array([[56, 12], [39, 74]])
b = np.array([[65, 76]])
c = np.append(a, b, axis=0)


# Command to reformat a singular dimension array of 12 elements into a 3, 4 matrix:

d = np.linspace(1, 12, 12)

e = d.reshape(3, 4)
