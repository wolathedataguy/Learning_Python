filepath = 'guest.txt'

prompt = "Please enter you name: "
name = input(prompt)

with open(filepath, 'x') as file:
    file.write(name)