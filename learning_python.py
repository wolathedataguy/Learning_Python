filename = 'learning_python.txt'

for num in range(1,4):
    #with open(filename) as file_object:
    #    contents = file_object.read()
    #    print(contents + "\n")
    
    #with open(filename) as f:
    #    for line in f:
    #        print(line.strip())
    
    with open(filename) as f:
        lines = f.readlines()
        
    for line in lines:
        print(line.strip())