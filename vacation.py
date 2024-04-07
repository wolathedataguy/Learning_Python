prompt = "If you could visit one place in the world, where would you go? "

active = True
while active:
    poll_ans = input(prompt)
    print(poll_ans)
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == 'yes':
        continue
    elif repeat.lower() == 'no':
        active = False

