import pandas as pd

df = pd.read_csv('Pandas/pokemon_data.csv')

# print(df.loc[df['Name'] == 'Delphox'])

# print(df.tail(3))
# print(df['Name'][0:5])

# print(df[['Name', 'Type 1', 'HP']])
# print(df.iloc[1:4]) or [1]
# print(df.iloc[2,1])

# for index, row in df.iterrows():
#     print(index, row['Name'])

# print(df.describe())

# print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))

# df['Total'] = df['HP'] + df['Attack']

# df = df.drop(columns=['Name'])

# df['Total'] = df.iloc[:, 4:10].sum(axis=1)

# cols = list(df.columns.values)
# df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

# # print(df.head(5))

# df.to_csv('Pandas/modified.csv', index=False)


# new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)] # | is or, & is and

# # new_df.to_csv('Pandas/filtered.csv')

# new_df.reset_index(drop=True, inplace=True)
# print(new_df)

# import re

# # print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]) #not is ~

# # print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]) #not is ~, ^ means start of line, * means 0 or more

# df.loc[df['Type 1'] == 'Flamer', 'Legendary'] = True

# print(df)