from users import UserDataGenerator
from transactions import Transaction
from products import ProductGenerator
import pandas as pd
import numpy as np


def clean_user_data(df_users):
    df_users['signup_date'] = pd.to_datetime(df_users['signup_date'], errors='coerce')
    df_users['signup_date'] = df_users['signup_date'].dt.date
    df_users['user_id'] = df_users['user_id'].apply(lambda x: x if isinstance(x, int) else np.nan)
    df_users = df_users.dropna(subset=["user_id"])
    df_users = df_users.drop_duplicates(subset=['user_id'])
    df_users['email'] = df_users['email'].fillna("email missing")
    df_users['name'] = df_users['name'].fillna("name missing")
    df_users['name'] = df_users['name'].str.strip().str.replace(r'\n|\r', ' ', regex=True)
    df_users['email'] = df_users['email'].str.strip().str.replace(r'\n|\r', ' ', regex=True)
    return df_users

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
user_data_cleaned = clean_user_data(user_data)
print(user_data_cleaned)
