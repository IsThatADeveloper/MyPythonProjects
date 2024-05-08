import pandas as pd
import os

rest = "MyFoodService"
print(f"Welcome to {rest}")
name = input("What is your name: ")


print(f"Here is a menu {name}")


pd.read_csv('menu.csv')

