people = [
        {
            'first_name':'Marvelous',
            'last_name':'Akindele',
            'age':'23',
            'city':'Lagos'
        },
        {
            'first_name':'Tobi',
            'last_name':'Oyelowo',
            'age':'24',
            'city':'Lagos'
        },
        {
            'first_name':'Florence',
            'last_name':'Togbe',
            'age':'24',
            'city':'Abuja'
        }
]


for number in people:
        identity = number['first_name'] + " " + number['last_name'] + ", " + number['age'] + ", " + number['city'] + "\n"
        print(identity)
