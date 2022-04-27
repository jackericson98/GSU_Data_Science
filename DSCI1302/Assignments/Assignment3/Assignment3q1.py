import pandas as pd
import numpy as np

df = pd.read_csv('airline.csv.shuffle', encoding='iso8859-1')
# print(df.head())
# df[:1000].to_csv('airline_test.csv')

# df = pd.read_csv('airline_test.csv')

# When is the best time of day/day of week/time of year to fly to minimize delays?

df['Hour'] = df['CRSDepTime'].div(100).apply(np.floor)  # Create hour column
tod_av_del = df.groupby(df['Hour']).mean()['DepDelay'].sort_values()  # Sum of delays for hour of day
dow_av_del = df.groupby('DayOfWeek').mean()['DepDelay'].sort_values()  # Sum of delays for day of week
toy_av_del = df.groupby('Month').mean()['DepDelay'].sort_values()  # Sum of delays for each month

# Do older planes suffer more delays?

yr_av_del = df.groupby('Year').mean()['DepDelay']  # Sum of delays for each month

# How does the number of people flying between different locations change over time?

yr_num_flts = df.groupby('Year').size()

# How well does weather predict plane delays?

weather_delay_corr = df.corrwith(df['WeatherDelay'])['DepDelay']

# Can you detect cascading failures as delays in one airport create delays in others? Are there critical links in the system?

ans = 'No'

# Rank the Airlines by delay

al_av_del = df.groupby('UniqueCarrier').mean()['DepDelay'].sort_values()

# Rank Airports by delay

ap_av_del = df.groupby('Origin').mean()['DepDelay'].sort_values()

