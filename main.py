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

def clean_transactions(transaction_data: pd.DataFrame):
    #poistetaan duplikaatit
    transaction_data.drop_duplicates(inplace=True)

    #Korvataan tyhjät sarakkeilta quantity, date
    transaction_data["quantity"] = transaction_data["quantity"].fillna(0.00)
    transaction_data["date"] = transaction_data["date"].fillna(np.datetime64("1900-01-01"))

    #pudotetaan tyhjät sarakkeilta product_id, user_id, id
    transaction_data.dropna(subset=["product_id", "user_id", "id"], inplace=True)
    
    #pudotetaan sarake, jos ei int-tyyppinen (product_id, user_id, id)
    transaction_data.drop(transaction_data[~transaction_data["id"].apply(lambda x: isinstance(x,int))].index, inplace=True)
    transaction_data.drop(transaction_data[~transaction_data["product_id"].apply(lambda x: isinstance(x,int))].index, inplace=True)
    transaction_data.drop(transaction_data[~transaction_data["user_id"].apply(lambda x: isinstance(x,int))].index, inplace=True)

users = 20
products = 50
transactions = 100
user_generator = UserDataGenerator(num_users=users) 
transaction_generator = Transaction(transaction_amount=transactions, user_amount=users, product_amount=products)
product_generator = ProductGenerator(num_products=products)
product_data = product_generator.get_product_data()
user_data = user_generator.get_user_data()

# print(user_data)
print(transaction_generator.transactions)

user_data_cleaned = clean_user_data(user_data)

# print(product_data)

df_transactions = transaction_generator.transactions
clean_transactions(df_transactions)

