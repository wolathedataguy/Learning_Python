sandwich_orders = ["tuna", "club", "ham and cheese", "vegetarian", "chicken","pastrami","pastrami","pastrami"]
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami sandwiches.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for order in sandwich_orders[:]:
    print(order)
    finished_sandwiches.append(order)
    sandwich_orders.remove(order)

print(finished_sandwiches)
