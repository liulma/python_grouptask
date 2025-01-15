from users import UserDataGenerator
from transactions import Transaction
from products import ProductGenerator
import pandas as pd
import numpy as np

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
# print(product_data)

df_transactions = transaction_generator.transactions
clean_transactions(df_transactions)
print(transaction_generator.transactions)