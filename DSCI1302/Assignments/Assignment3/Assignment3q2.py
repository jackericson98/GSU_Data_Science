import pandas as pd

df = pd.read_csv('cinemaTicket_Ref.csv')

# Determine common factors in poor-performing ticket sales?
# Is there a connection between ticket sales and price?
# Is there a connection between ticket sales and time of day?
# Is there a connection between ticket sales and the time of year?
corr = df.corr().abs()['tickets_sold']
print(corr.sort_values(ascending=False))

# Can you tell off of this Data set if certain theaters are under performing?
best_cinemas = df.groupby('cinema_code').mean()['tickets_sold'].sort_values()
print(best_cinemas)
