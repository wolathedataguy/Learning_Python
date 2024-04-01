foods = ('Amala','Fried rice','Gbegiri','Akara','Semo')
for food in foods:
    print(food)
print("\n")
#foods[1] = 'Moi Moi'
foods = ('Amala','Fried rice','Gbegiri','Yam','Spaghetti')
for food in foods:
    print(food)

foods = list(foods)
foods.append('Fufu')
foods = tuple(foods)
print(foods)