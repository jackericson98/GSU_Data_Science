import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Q1. (20%) Randomly generate a numpy array with 1000 numbers in the shape of (100, 10). The numbers should lie in the
# range of 1 and 50 inclusive. Then

print("\nQuestion 1:\n")
arr1 = np.random.rand(100, 10) * 49 + 1

# 1. calculate the mean, median, max, and standard deviation of all the numbers.

mean = round(np.mean(arr1), 2)
median = round(np.median(arr1), 2)
maxi = round(np.max(arr1), 2)
std = round(np.std(arr1), 2)
print("Overall Mean = {}, Overall Median = {}, Overall Max = {}, Overall STD = {}\n".format(mean, median, maxi, std))

# 2. calculate the mean, median, max, and standard deviation values of each row.

means = []
medians = []
maxis = []
stds = []
for i in range(len(arr1[0])):
    means.append(round(np.mean(arr1[:, i]), 2))
    medians.append(round(np.median(arr1[:, i]), 2))
    maxis.append(round(np.max(arr1[:, i]), 2))
    stds.append(round(np.std(arr1[:, i]), 2))

print("Row Means = {}\nRow Medians = {}\nRow Maxes = {}\nRow STDs = {}".format(means, medians, maxis, stds))


# Q2. (30%) Randomly generate a numpy array with 1000 numbers in the shape of (10000,). The numbers should be in the
#   range of 1 and 50 inclusive. Then

print("\n\nQuestion 2:\n")
arr2 = np.random.rand(10000,)*49 + 1

# 1. print the first 10 numbers, the last 10 numbers and the variance.

print("First 10 numbers = {}\nLast 10 numbers = {}\nVariance = {}\n".format([round(x, 2) for x in arr2[:10]],
                                                                          [round(x, 2) for x in arr2[-10:]],
                                                                          round(arr2.var(), 2)))

# 2. calculate the difference of every two adjacent numbers in the array. For example, if the original array is
#   [2,4,-1], then the array of difference should be [2, -5] because 4-2=2 and -1-4=-5. You should **NOT** use a
#   for/while loop.

arr2_diffs = arr2[1::] - arr2[:-1:]

# 3a. calculate the sum of the difference array that you got in (2).

arr2_diffs_sum1 = np.sum(arr2_diffs)
print("Cumulative difference = {}\n".format(arr2_diffs_sum1))

# 3b. Can you come up with another way to get the sum?

arr2_diffs_sum2 = 0
for i in range(len(arr2) - 1):
    x = arr2[i + 1] - arr2[i]
    arr2_diffs_sum2 += x

# 4. sort the original array.

arr2_srt= np.sort(arr2)

# 5. print the first 10 numbers, the last 10 numbers and the variance of the sorted array. Is the variance changed?

print("First 10 sorted numbers = {}\nLast 10 sorted numbers = {}\nVariance = {}\n"
      .format([round(x, 4) for x in arr2_srt[:10]], [round(x, 4) for x in arr2_srt[-10:]], round(np.var(arr2_srt), 2)))

# 3. calculate the mean, median, max, and standard deviation values of each column.

means2 = []
medians2 = []
maxis2 = []
stds2 = []
for i in range(len(arr2)):
    means2.append(round(np.mean(arr2[i]), 2))
    medians2.append(round(np.median(arr2[i]), 2))
    maxis2.append(round(np.max(arr2[i]), 2))
    stds2.append(round(np.std(arr2[i]), 2))

print("Col Means = {}\n\nCol Medians = {}\n\nCol Maxes = {}\n\nCol STDs = {}".format(means2, medians2, maxis2, stds2))

# 4. compare the mean values you got in (1)-(3) with 25. What do you find? Can you explain it?

"""The means in this example are just the raw data values, so they should on average fall around 25."""

# Q3. (50%) U.S. population data from 1950 to 2020 is provided in **US_population.txt**.
#   United Nations projections are also included through the year 2100.
#
# You can view the file by any text editor. There are two columns in the file separated by a comma: the first column
# corresponds to the year and the second corresponds to the population.
#
# 1. Create a numpy array with the population data.

pops = pd.read_csv("US_population.txt")
years = [x[:4] for x in pops['date']]

# **Hint**: you may need readlines() and split() function.
# 2. Calculate the annual growth rate of the population based on the method you used in Q2(2). Do **NOT** use a
#    for/while loop.

diffs = np.diff(pops[' Population'])
percent_diffs = diffs/pops[' Population'][:-1]*100

# **Hint**: If the population of year 2020 is *a* and the population of year 2021 is *b*, then the annual growth rate
# of 2021 is *(b-a)/a*.
# 3. Plot the population and annual growth rate as **PT5_1.jpg** and **PT5_2.jpg**. Use solid line for historical data
# (1950 through 2020) and dashed line for U.N. projections data (2020 through 2100).

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
ax1.plot(years[:70], percent_diffs[:70])
ax1.plot(years[70:-1], percent_diffs[70:], linestyle='--', color='b')
ax2.plot(years[:70], pops[' Population'][:70])
ax2.plot(years[70:], pops[' Population'][70:], linestyle='--', color='b')
ax1.set_xticks(np.linspace(0, 150, 10))
ax2.set_xticks(np.linspace(0, 150, 10))
ax2.legend(["Reported Data", "Predicted Data"])
ax1.legend(["Reported Data", "Predicted Data"])
ax2.set_xlabel("Year")
ax1.set_xlabel("Year")
ax2.set_ylabel("Population")
ax1.set_ylabel("Percent growth")
ax1.set_title("Population Growth (percentage)")
ax2.set_title("Population")
plt.show()
