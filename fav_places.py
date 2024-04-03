favourite_places = {
    'Sam':'Norway',
    'Helen':'Maryland',
    'Angel':'Abuja'
    }

for person, place in favourite_places.items():
    print(person)
    print(place)
    print("\n")

for person in favourite_places:
    print(person) 
    print(favourite_places[person], "\n")