import json

def fav_num():
    """Prompt and store the user's favourite number"""
    filename = 'fav_number.json'
    number = int(input("What is your favourite number? "))
    with open(filename, 'w') as file:
        json.dump(number, file)
    return number

fav_num()