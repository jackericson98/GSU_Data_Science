import numpy as np


class BigMatrixMath:
    """Used to do matrix math with object"""

    def __init__(self):

        self.myList = []

    def addMatrix(self, userArray=None):

        """Parameters: {Array} Adds an array/matrix to our list. If no array is
        provided, the function will generate a 40x40 matrix with random floats from -70 to 159"""

        if userArray is None:
            userArray = np.random.rand(40, 40) * 229 - 70

        self.myList.append(userArray)

        return self.myList

    def printDimension(self):

        """Prints the dimensions of every NumPy array in the list"""

        if len(self.myList) == 0:
            print("Sorry your list is empty, please try the \".addMatrix()\" method.")
        else:
            for i in range(len(self.myList)):
                print("List {} dimensions are: {}\n".format(i + 1, self.myList[i].shape))

    def dotProductEligible(self, index1, index2):

        """Takes in the indices of two matrices in our list and checks if they are eligible for a dot product"""

        if index1 <= len(self.myList) and index2 <= len(self.myList):
            if self.myList[index1].shape == self.myList[index2].shape:
                return True
            else:
                return False
        else:
            print("Sorry your indexes are out of range please try again")
