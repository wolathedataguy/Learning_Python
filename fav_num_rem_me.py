import json

def read_fav_num():
    """Reads my favourite number from a file"""
    filename = 'fav_number.json'
    try:
        with open(filename) as file:
            fav_num = json.load(file)
    except:
        return None
    else:
        return fav_num

def fav_num():
    """Prompt and store the user's favourite number"""
    filename = 'fav_number.json'
    fav_num = read_fav_num()
    if fav_num:
        message = f"I know your favorite number! It's {fav_num}"
        print(message)
    else:
        number = int(input("What is your favourite number? "))
        with open(filename, 'w') as file:
            json.dump(number, file)


fav_num()