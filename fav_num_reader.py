import json

def read_fav_num():
    """Reads my favourite number from a file"""
    filename = 'fav_number.json'
    with open(filename) as file:
        fav_num = json.load(file)
    message = f"I know your favorite number! It's {fav_num}"
    print(message)
    return fav_num

read_fav_num()