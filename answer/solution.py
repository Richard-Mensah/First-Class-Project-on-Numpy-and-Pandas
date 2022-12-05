## importing the pandas and numpy library

import pandas as pd
import numpy as np

#### Creating a DataFrame from a list of dictionaries

data = [{'product_id':23, 'name':'computer', 'wholesale_price': 500, 'retail_price':1000, 'sales':100}, 
{'product_id':96, 'name':'Python Workout', 'wholesale_price': 35,'retail_price':75, 'sales':1000},
{'product_id':97, 'name':'Pandas Workout', 'wholesale_price': 35, 'retail_price':75, 'sales':500},
{'product_id':15, 'name':'banana', 'wholesale_price': 0.5,'retail_price':1, 'sales':200},
{'product_id':87, 'name':'sandwich', 'wholesale_price': 3,'retail_price':5, 'sales':300}]

df = pd.DataFrame(data)

df

#### Total net revenue you received from all of these sales?

Total_net_revenue = df['net_revenue_per_product'].sum()
Total_net_revenue

#### What product is product retail price more than twice the wholesale price?
df_product = df.loc[df['retail_price'] > (2 * df['wholesale_price'])]
df_product

#### How much did the store make from food vs. computers vs. books?

# Amount made from food
df_food = df.loc[3:4]
df_food

food_revenue = df_food['net_revenue_per_product'].sum()
food_revenue

# Amount made from computer
df_computer = df.loc[df['name'] == 'computer'] 
df_computer

computer_revenue = df_computer['net_revenue_per_product'].sum()
computer_revenue

# Amount made from books
df_book = df.loc[1:2]
df_book

book_revenue = df_book['net_revenue_per_product'].sum()
book_revenue


#### New net revenue after a 30% discount on the wholesale price of goods

# calculate new wholesale price

new_wholesale_price = 0.70 * df['wholesale_price']
df['new_wholesale_price'] = new_wholesale_price
df


df['new_net_revenue_per_product'] = (df['retail_price'] - df['new_wholesale_price']) * df['sales']
df