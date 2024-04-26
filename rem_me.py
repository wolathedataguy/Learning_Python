import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as file:
            username = json.dump(file)
    except:
        return None
    else:
        return username

def get_new_username():
    """Greet the user by name"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()