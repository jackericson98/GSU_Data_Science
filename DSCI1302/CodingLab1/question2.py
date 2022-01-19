# Name: John Ericson
# Email: jericson1@gsu.edu
# Class: DSCI 1302, 19712


# Question:
"""Consider the following string: nums = '10,20,30,40,50'
Create a Python script that creates a list of integers from the string.
The resulting list will be: [10, 20, 30, 40, 50]"""


testString = '10,20,30,40,50'


# First attempt
def string2int(userStr):
    i = 0
    int_list = []
    for char in userStr:
        if char == ',':
            int_list.append(int(userStr[i-2:i]))
        i += 1
    int_list.append(int(userStr[-2:]))
    return int_list


# Second attempt
def string2int1(userStr):
    strList = userStr.split(',')
    return list(map(int, strList))


print('First function result: {}. \nSecond function result: {}.' .format(string2int(testString), string2int1(testString)))
