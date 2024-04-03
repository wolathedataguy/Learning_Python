sandy = {
    'kind': 'Dog',
    'name': 'Charlie'
    }
riley = {
    'kind': 'cat',
    'name': 'Alan'
    }
ben = {
    'kind': 'Dog',
    'name': 'Sam'
    }

pets = [sandy, riley,ben]


for pet in pets:
    message = "This " + pet['kind'] + " is owned by " + pet['name'] + "\n"
    print(message)