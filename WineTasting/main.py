import pandas as pd

#1 Load the datafram
#2 How many wines have been given a 100pt rating?
#3 What is the name of the most expensive wine.
#4 Calculate a new column showing the ratings in a 0 - 5 scale
#5 Create a price histogram for wines that cost less than 100
#6 Plot a scatter graph - x = price, y = points


# DATA ANALYSIS

# 1
df = pd.read_csv("wines.csv")

# 2
perfect_rating = len(df.loc[df['points'] == 100])

# 3
most_expensive = df.loc[df['price'] == df['price'].max()]['name'].squeeze()

# 4 Add new column with value
df['rate'] = df['points'] / 20

# 5 Create Histograph of all with a price value below 100
df.loc[df['price'] < 100]['price'].hist()


# 6 Plot a scatter graph showing the relationship between price and score
df.plot(x='price', y='points', figsize=(15, 3), kind='scatter')


