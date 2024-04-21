filename = 'responses.txt'

while True:
    prompt = "Why do you like programming: "
    response = input(prompt) +"\n"
    with open(filename, 'a+') as file:
        file.write(response)