import pandas as pd

df2 = pd.read_csv('nba2021_advanced.csv')
df1 = pd.read_csv('nba2022_advanced.csv', encoding="ISO-8859-1")


# Model the data using PER and TrueShooting percentage to determine the best players in the league and the most average players in the league.

best_TS_players = df2.loc[df2['TS%'] >= 0.7, 'Player']
best_PER_players = df2.loc[df2['PER'] >= 30, 'Player']

av_PER = df2['PER'].mean()
av_TS = df2['TS%'].mean()

av_TS_Players = df2.loc[df2['TS%'].between(av_TS - 0.001*av_TS, av_TS + 0.001*av_TS), 'Player']
av_PER_Players = df2.loc[df2['PER'].between(av_PER - 0.004*av_PER, av_PER + 0.004*av_PER), 'Player']

# What players have become much better in that year?
df1['PER1'] = df1.eval('PTS + TRB + AST + STL + BLK + (-FGA) + FG + (-FTA) + FT + (-TOV)')
print(df1['PER1'])
print(df2['PER'])
merged = df2.merge(df1, how='left', left_on=['Player', 'PER'], right_on=['Player', 'PER1'])
print(merged['PER1'])
merged_diffs = merged.eval('PER1-PER')

print(merged_diffs)

# What players have become much worst?
# Show a scatter plot of all above average players regarding TS% and PER one one year in one color and the other in a different color?
