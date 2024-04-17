filename = 'pi_digits.txt'

#with open(filename) as f:
#    contents = f.read()
#    print(contents.strip())

#with open(filename) as f:
#    for line in f:
#        print(line.strip())

with open(filename) as f:
    lines = f.readlines()
    print(lines)
for line in lines:
    print(line.strip())