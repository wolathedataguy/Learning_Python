class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
    
    def describe_user(self):
        print("Here the details of this user: \n")
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.email)
    
    def greet_user(self):
        message = f"Hello {self.first_name} {self.last_name}, "
        print(message)


user1 = User("John", "Doe", 30, "john.doe@example.com")
user2 = User("Alice", "Smith", 25, "alice.smith@example.com")
user3 = User("Bob", "Johnson", 40, "bob.johnson@example.com")

# Calling methods for each user
user1.describe_user()
user1.greet_user()

print("\n")

user2.describe_user()
user2.greet_user()

print("\n")

user3.describe_user()
user3.greet_user()