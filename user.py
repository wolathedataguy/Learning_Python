class User():
    """ A representation of a user"""
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