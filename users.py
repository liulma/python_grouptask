from faker import Faker

import pandas as pd
import numpy as np
from faker import Faker

class UserDataGenerator:
    def __init__(self, num_users):
        self.num_users = num_users
        self.fake = Faker()
        self.users = self.generate_users()

    def generate_users(self):
        user_data = []
        for user_id in range(1, self.num_users + 1):
            name = self.fake.name()
            email = self.fake.email()
            signup_date = self.fake.date()
            user_data.append({
                "user_id": user_id,
                "name": name,
                "email": email,
                "signup_date": signup_date
            })

        return pd.DataFrame(user_data)

    def get_user_data(self):
        return self.users
