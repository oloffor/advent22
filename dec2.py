def read_file_num():
    f=open('input2.txt', 'r')
    inter  = f.readlines()
    
    return inter

def countpoints():
    inter = read_file_num()
    points = 0
    for index in inter:
        if index == 'A X\n':
            points += 4
        elif index == 'A Y\n':
            points += 8
        elif index == 'A Z\n':
            points += 3
        elif index == 'B X\n':
            points += 1
        elif index == 'B Y\n':
            points += 5
        elif index == 'B Z\n':
            points += 9
        elif index == 'C X\n':
            points += 7
        elif index == 'C Y\n':
            points += 2
        elif index == 'C Z\n':
            points += 6
    return points


print(countpoints())

def countpoints2():
    inter = read_file_num()
    points = 0
    for index in inter:
        if index == 'A X\n':
            points += 3
        elif index == 'A Y\n':
            points += 4
        elif index == 'A Z\n':
            points += 8
        elif index == 'B X\n':
            points += 1
        elif index == 'B Y\n':
            points += 5
        elif index == 'B Z\n':
            points += 9
        elif index == 'C X\n':
            points += 2
        elif index == 'C Y\n':
            points += 6
        elif index == 'C Z\n':
            points += 7
    return points

print(countpoints2())