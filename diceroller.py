import random

def dice(roll):
    
    roll = roll.split('d')
    roll[1] = roll[1].split(' ')

    del roll[1][1]
    roll[0] = int(roll[0]) *  int(roll[1][0])
    del roll[1][0]
    roll[0] = int(roll[0]) + int(roll[1][0])
    del roll[1][0]

    roll[1][0]
    print(roll)

    return roll


print(dice(input()))

# Я ДУРАЧОК
# 6d6 + 2