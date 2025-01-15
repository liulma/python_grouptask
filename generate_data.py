from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime, date

class Transaction:
    def __init__(self, transaction_amount: int):
        self.amount = transaction_amount
        self.fake = Faker()

    def generate(self):
        transaction_list = []
        for i in range(0, self.amount):
            new_transaction = {
                "id" : i,
                "user_id" : np.random.randint(0, 21),
                "product_id" : np.random.randint(0, 51),
                "quantity" : np.round(np.random.uniform(0, 100), decimals=2),
                "date" : self.fake.date()
            }
            