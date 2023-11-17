import random

def dice(roll):
    
    roll = roll.split('d')
    temp = roll[1].split('+')
    del roll[1]
    for i in temp:
        roll.append(i)
    roll = list(map(int, roll))
    rd = []
    for i in range(roll[0]):
        rd.append(random.randint(1, roll[1]))
    return sum(rd) + roll[2]


print(dice(input()))

# Я ДУРАЧОК
# 6d6 + 2