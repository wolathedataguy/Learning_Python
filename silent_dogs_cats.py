filepath = ['cats.txt','dogs.txt']

def read_file(filename):
    """Read and print out the contents of the file"""
    try:
        with open(filename) as file:
            contents = file.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in contents:
            print(line.strip())

for file in filepath:
    read_file(file)