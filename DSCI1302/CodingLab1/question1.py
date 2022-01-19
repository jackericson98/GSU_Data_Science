# Name: John Ericson
# Email: jericson1@gsu.edu
# Class: DSCI 1302, 19712


# Question:
""" Create a Python script that asks the user for a number and then prints out a
    list of all the divisors of each number less than the asked number."""


def askquestion():
    number = int(input("Enter a number: "))
    divisors = []
    for i in range(1, number//2):
        if number % i == 0:
            divisors.append(i)
    print("Your number, {}, is divisible by the following numbers: \n{}" .format(number, divisors))


askquestion()