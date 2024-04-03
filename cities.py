cities ={
    'Lagos': {'country': 'Nigeria','population':'22 Million', 'fact':'most populous city in Africa'},
    'Newyork': {'country': 'USA','population':'20 Million', 'fact':'the city that never sleeps'},
    'Kaduna': {'country': 'Nigeria','population':'4.5 Million', 'fact':'one of the state with the highest temperatures in Nigeria'}
    }

for city, info in cities.items():
    print(city,":")
    print("\t", info['country'])
    print("\t", info['population'])
    print("\t", info['fact'], "\n")
    
for city in cities:
    print(city, ":")
    for info_key in cities[city].values():
        print("\t",info_key)