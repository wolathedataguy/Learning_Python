def sandwich(*sandwich_items):
    print("Here are the ingredients used to make your sandwich:")
    for item in sandwich_items:
        print("\t",item)

sandwich('Pastrami', 'Tomato', 'Chicken')
sandwich('Cheese', 'Peanut Butter')
sandwich('Egg','Cheese', 'Onions')
sandwich('Butter')