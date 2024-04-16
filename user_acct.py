from user import User

class Priveleges():
    """A class to show what priveleges the user has"""
    def __init__(self):
        self.privileges = [ 'can add post', 'can delete post', 'can ban user']
    
    def show_priveleges(self):
        """ Shows what can type of privileges the admin is privy to"""
        message = "What type of priveleges does this user have? "
        print(message)
        for privelege in self.privileges:
            print(privelege)

class Admin(User):
    """ A representation of a type of User"""
    def __init__(self, first_name, last_name, age, email):
        """Initializing the parent and child attributes"""
        super().__init__(first_name, last_name, age, email)
        self.privileges = Priveleges()