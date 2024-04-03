fav_numbers = {
    'Marvy': 39,
    'Lawal': 23,
    'Flo': 69,
    'Kome': 20,
    'Segun': 59
    }

for person in fav_numbers:
    message = person + '\'s' + ' favourite number is ' + str(fav_numbers[person]) + '\n'
    print(message, "\n")

fav_numbers = {
    'Marvy': ['39','37'],
    'Lawal': ['2','3'],
    'Flo': ['6','9'],
    'Kome': ['20','0'],
    'Segun': ['59','19']
    }

for person in fav_numbers:
    message = person + "'s favourite numbers are:" 
    print(message)
    for num in fav_numbers[person]:
        print("\t", num )


#items() can only be used on dictionaries 
for person, numbers in fav_numbers.items():
    print(person)
    for num in numbers:
        print(num)