from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1, self.sides)

die_six = Die()

for n in range(10):
    print(str(n+1) + ' - Die roll result: ' + str(die_six.roll_die()))

print ('----------------------')

die_twenty = Die(20)

for n in range(10):
    print(str(n+1) + ' - Die roll result: ' + str(die_twenty.roll_die()))
