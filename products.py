from faker import Faker
import pandas as pd
import json

class ProductGenerator:
    def __init__(self, num_products):
        self.num_products = num_products
        self.fake = Faker()

    def generate_products(self):
        products = []
        for i in range(1, self.num_products + 1):
            product = {
                'id': i,
                'name': self.fake.word() + " " + self.fake.word(),
                'category': self.fake.random_element(elements=('Electronics', 'Clothing', 'Books', 'Groceries')),
                'price': float(self.fake.pydecimal(left_digits=2, right_digits=2, positive=True))
            }

            products.append(product)

        return pd.DataFrame(products)
    
    def get_product_data(self):
        return self.products