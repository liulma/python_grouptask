from users import UserDataGenerator

user_generator = UserDataGenerator(num_users=20) 
user_data = user_generator.get_user_data()

print(user_data)