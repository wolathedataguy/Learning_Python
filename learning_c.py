filepath = 'learning_python.txt'

with open(filepath) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.replace("Python","C"))

with open(filepath) as file:
    for line in file:
        print(line.replace("Python","C"))