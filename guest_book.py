filepath = 'guest_book.txt'

while True:
    prompt = "Please enter your name: "
    guest_name = input(prompt) + "\n"
    
    with open(filepath, 'a+') as file:
        file.write(guest_name)