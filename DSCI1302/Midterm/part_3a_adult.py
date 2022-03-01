# Imports
import pandas as pd


adults = pd.read_csv("part_3_data/adult.csv")

lower_class = adults[adults["class"] == " <=50K"]
upper_class = adults[adults["class"] == " >50K"]

# What is the average age of adults that make under 50K? What is the average age of adults that make over 50K?

lc_age_mean = lower_class["age"].mean()
uc_age_mean = upper_class["age"].mean()

print("Average age of adults that make under 50K: {}\nAverage age of adults that make over 50K: {}\n"
      .format(lc_age_mean, uc_age_mean))

# What is the standard deviation of hours worked of adults that make under 50K?
# What is the standard deviation of hours worked of adults that make over 50K? (I assume this is what you meant)

lc_hrs_std = lower_class["hours-per-week"].std()
uc_hrs_std = upper_class["hours-per-week"].std()

print("Standard deviation of hours worked of adults that make under 50K: {}\nStandard deviation of hours worked of "
      "adults that make over 50K: {}\n".format(lc_hrs_std, uc_hrs_std))

# What is the correlation between of hours worked and age of adults that make under 50K?
# What is the correlation between of hours worked and age of adults that make over 50K?

lc_corr_hrs_age = lower_class.corr()["hours-per-week"]["age"]
uc_corr_hrs_age = upper_class.corr()["hours-per-week"]["age"]

print("Correlation between of hours worked and age of adults that make under 50K?: {}\nCorrelation between of hours "
      "worked and age of adults that make over 50K?: {}\n".format(lc_corr_hrs_age, uc_corr_hrs_age))
