from random import randint
x = randint(1, 6)

class Die():
    """A representation of a Die"""
    def __init__(self, sides=6):
        """Initializing the number of sides the die has"""
        self.sides = sides
    
    def roll_die(self):
        sides = self.sides
        print(randint(1,sides))
    
my_die = Die()
for num in range(1,11):
    my_die.roll_die()