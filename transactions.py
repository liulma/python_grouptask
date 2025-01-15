from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime, date

class Transaction:
    def __init__(self, transaction_amount: int, user_amount: int, product_amount: int):
        self.amount = transaction_amount
        self.user_amount =  user_amount
        self.product_amount = product_amount
        self.fake = Faker()
        self.transactions = self.generate_transactions()

    def generate_transactions(self):
        transaction_list = []
        for i in range(0, self.amount):
            new_transaction = {
                "id" : i,
                "user_id" : np.random.randint(0, self.user_amount),
                "product_id" : np.random.randint(0, self.product_amount),
                "quantity" : np.round(np.random.uniform(0, 100), decimals=2),
                "date" : self.fake.date()
            }
            transaction_list.append(new_transaction)
        df = pd.DataFrame(transaction_list)

        return df
            