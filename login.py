class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print("Here the details of this user: \n")
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.email)
    
    def greet_user(self):
        message = f"Hello {self.first_name} {self.last_name}, "
        print(message)
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("John", "Doe", 30, "john.doe@example.com")
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)