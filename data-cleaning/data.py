import pandas as pd

# import modules + read file csv
df = pd.read_csv('contoh.csv')
df2 = pd.read_csv('games.csv')

# print data
# print(df)
# print(df2.head())

# basic logic to print `usia` less than x
dm = df[df['usia']<30]

print(dm)
print(br)

# sort value
sv = df.sort_values(by='usia')

print(sv)
