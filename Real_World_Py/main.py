import pandas as pd
import glob
import numpy as np

#### Merging 12 months of sales data into a single file

# list all csv files only
csv_files = glob.glob('Real_World_Py/Sales_Data/*.{}'.format('csv'))

df_csv_append = pd.DataFrame()
 
# append the CSV files
for file in csv_files:
    df = pd.read_csv(file)
    df_csv_append = pd.concat([df_csv_append, df], ignore_index=True)


# df_csv_append.to_csv('Real_World_Py/Total_Data.csv', index=False)
    
new_df = pd.read_csv('Real_World_Py/Total_Data.csv')

#### What was the best month for sales? How much was earned that month

max_total_price = float('-inf')  # Initialize max_total_price to negative infinity
file_with_max_total = None  # Initialize variable to store the file name with the greatest total price

for file in csv_files:
    total_price = 0  # Initialize the total price accumulator for each file
    df = pd.read_csv(file)
    prices = df['Price Each']
    for price in prices:
        if pd.notnull(price) and price != 'Price Each':  # Check if price is not NaN and not the header
            total_price += float(price)  # Add the price to the total_price accumulator
    if total_price > max_total_price:
        max_total_price = total_price
        file_with_max_total = file

# print("File with Greatest Total Price:", file_with_max_total)  # Print the file name with the greatest total price
# print("Greatest Total Price:", max_total_price)  # Print the greatest total price



#### Youtube method

#### Clean Data
new_df

# new_df['Month'] = new_df['Order Date'].str[0:2]
# new_df['Month'] = new_df['Month'].astype('int32')
# print(new_df.head())