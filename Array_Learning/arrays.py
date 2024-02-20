import pandas as pd

df = pd.read_csv('Array_Learning/data.csv')
# print(df.head())
# print(df['Height (inches)'])

total_height = df['Height (inches)'].sum()
# print("Total height", total_height)
