prompt = "How old are you? or quit "


while True:
    age = int(input(prompt))
    if age == 0:
        print("Exiting")
        break
    elif age < 3:
        print("The ticket is free\n")
    elif age <= 12:
        print("The ticket is $10\n")
    else:
        print("The ticket is $15\n")