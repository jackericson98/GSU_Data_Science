import pandas as pd

cars_raw = pd.read_csv("part_3_data/car.csv")


# Replace each text value for a meaningful integer equivalent for each column in the data.

def replace_string(df):
    """Used to replace specific string values in our data frame with meaningful (plottable) values"""
    for seq in df:
        for i in range(len(df[seq])):
            if df[seq][i] == '5more' or df[seq][i] == 'more' or df[seq][i] == 5:
                df[seq][i] = 5
            elif df[seq][i] == 'vhigh' or df[seq][i] == 4:
                df[seq][i] = 4
            elif df[seq][i] == 'high' or df[seq][i] == 'big' or df[seq][i] == 3:
                df[seq][i] = 3
            elif df[seq][i] == 'med' or df[seq][i] == 'med' or df[seq][i] == 2:
                df[seq][i] = 2
            elif df[seq][i] == 'low' or df[seq][i] == 'small' or df[seq][i] == 'acc' or df[seq][i] == 1:
                df[seq][i] = 1
            elif df[seq][i] == 'unacc' or df[seq][i] == 0:
                df[seq][i] = 0
            else:
                df[seq][i] = 0

    return df


print("Car data set before replacement:\n\n{}\n\n".format(cars_raw.head()))
cars = replace_string(cars_raw)
print("Car data set after replacement:\n\n{}\n\n".format(cars.head()))


# What’s the correlation between buying, safety, and maintenance?

cars_buy_safe_corr = cars.astype('float64').corr()["Buying"]["Safety"]
cars_buy_maint_corr = cars.astype('float64').corr()["Buying"]["Maintenance"]
cars_maint_safe_corr = cars.astype('float64').corr()["Maintenance"]["Safety"]

print("Correlation between buying and safety: {}\nCorrelation between buying and maintenance: {}\nCorrelation between "
      "maintenance and safety: {}\n".format(cars_buy_safe_corr, cars_buy_maint_corr, cars_maint_safe_corr))
