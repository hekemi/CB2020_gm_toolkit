import random


def dice(roll):
    rd = []
    roll = roll.split('d')
    if '+' in roll[1]:
        temp = roll[1].split('+')
        del roll[1]
        for i in temp:
            roll.append(i)
        roll = list(map(int, roll))
        for i in range(roll[0]):
            rd.append(random.randint(1, roll[1]))
        return sum(rd) + roll[2]
    roll = list(map(int, roll))
    for i in range(roll[0]):
        rd.append(random.randint(1, roll[1]))
    return sum(rd)


if __name__ == '__main__':
    pass