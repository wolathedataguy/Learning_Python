filename = 'pi_million_digits.txt'

with open(filename) as f:
    lines = f.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')