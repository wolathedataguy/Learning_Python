sandwich_orders = ['BLT','Panini','Tortas','Cheese','Egg']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    message = "I made your " + sandwich + " sandwich"
    print(message)
    finished_sandwiches.append(sandwich)

print("\nA list of sandwiches that was made: ")
for sandwich in finished_sandwiches:
    message = sandwich + " was made"
    print("\t",message)
