from users import UserDataGenerator
from transactions import Transaction
users = 20
products = 50
transactions = 100
user_generator = UserDataGenerator(num_users=users) 
transaction_generator = Transaction(transaction_amount=transactions, user_amount=users, product_amount=products)
user_data = user_generator.get_user_data()

print(user_data)
print(transaction_generator.transactions)