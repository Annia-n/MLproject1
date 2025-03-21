import pandas as pd
df = pd.read_csv("/Users/anya/Desktop/MELBOURNE_HOUSE_PRICES_LESS.csv", header=0 )
print(df) 

#show only the first five row
print(df.head())

#num of features
df.shape[1]

#preprocessing
df.isnull()
# Count missing values per column
null_counts = df.isnull().sum()
print(null_counts)
print(f"num of all missing values in dataset: {df.isnull().sum().sum()}")

#deleting null rows
df.dropna(axis=0,inplace=True)
print(df)

#summarize data
print(df.describe())
""" Count - Counts the number of observations
Mean - The average value
Std - Standard deviation
Min - The lowest value
25%, 50% and 75% are percentiles 
Max - The highest value """