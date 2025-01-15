from users import UserDataGenerator
from transactions import Transaction
from products import ProductGenerator
import pandas as pd

def clean_products(product_data):
    product_data.dropna(subset=['id'])
    product_data.fillna({'name': 'Unknown', 'category': 'Other', 'price': 0.0})

    product_data.drop_duplicates()

    product_data.drop(product_data[~product_data["id"].apply(lambda x: isinstance(x,int))].index, inplace=True)

    return product_data

users = 20
products = 50
transactions = 100
user_generator = UserDataGenerator(num_users=users) 
transaction_generator = Transaction(transaction_amount=transactions, user_amount=users, product_amount=products)
product_generator = ProductGenerator(num_products=products)
product_data = product_generator.get_product_data()
user_data = user_generator.get_user_data()

print(user_data)
print(transaction_generator.transactions)
print(product_data)

product_cleaned = clean_products(product_data)
print(product_cleaned)