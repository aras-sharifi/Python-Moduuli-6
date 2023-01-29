import random
def dice(kerrat):
    return random.randint(1,kerrat)


kerrat = int(input("Kuinka Monta kertaa? "))
roll = dice(kerrat)
while roll != kerrat:
    print(roll)
    roll = dice(kerrat)
print(roll)