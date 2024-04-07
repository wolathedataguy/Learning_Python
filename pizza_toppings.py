prompt = "What pizza toppings do you want? "

while True:
    toppings = input(prompt)
    if toppings != "quit":
        print("I'll add that topping to their pizza")
    else:
        break