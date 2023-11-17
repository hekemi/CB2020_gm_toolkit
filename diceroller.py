import random

def dice(roll):
    
    roll = roll.split('d')
    temp = roll[1].split('+')
    del roll[1]
    for i in temp:
        roll.append(i)
    roll = list(map(int, roll))
    return roll[0] * random.randint(1, roll[1]) + roll[2]


print(dice(input()))

# Я ДУРАЧОК
# 6d6 + 2