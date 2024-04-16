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

class Admin(User):
    """ A representation of a type of User"""
    def __init__(self, first_name, last_name, age, email):
        """Initializing the parent and child attributes"""
        super().__init__(first_name, last_name, age, email)
        self.privileges = [ 'can add post', 'can delete post', 'can ban user']
    
    def show_priveleges(self):
        """ Shows what can type of privileges the admin is privy to"""
        message = "What type of priveleges does this user have? "
        print(message)
        for privelege in self.privileges:
            print(privelege)


user_admin = Admin('Samuel', 'Adekoya', 23, 'Dekoyo@gmail.com')
user_admin.show_priveleges()