my_pizzas = ['BBQ','Pepperoni','Chicken']
friend_pizzas = my_pizzas[:]

my_pizzas.append('Chicken Suya')
friend_pizzas.append('Meat Suya')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)