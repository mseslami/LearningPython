import copy
import random


table = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]


def Move_down():
    for i in range(len(table) - 1):
        for j in range(len(table)):
            if table[len(table) - 2 - i][j] != 0 and table[len(table) - 1 - i][j] == 0:
                table[len(table) - 1 - i][j], table[len(table) - 2 - i][j] = table[len(table) - 2 - i][j], \
                                                                             table[len(table) - 1 - i][j]


def Add_down():
    for i in range(len(table) - 1):
        for j in range(len(table)):
            if table[len(table) - 2 - i][j] != 0 and table[len(table) - 1 - i][j] == table[len(table) - 2 - i][j]:
                table[len(table) - 2 - i][j] = 0
                table[len(table) - 1 - i][j] *= 2


def Move_up():
    for i in range(len(table) - 1):
        for j in range(len(table)):
            if table[1 + i][j] != 0 and table[i][j] == 0:
                table[i][j], table[1 + i][j] = table[1 + i][j], table[i][j]


def Add_up():
    for i in range(len(table) - 1):
        for j in range(len(table)):
            if table[1 + i][j] != 0 and table[i][j] == table[1 + i][j]:
                table[1 + i][j] = 0
                table[i][j] *= 2


def Move_left():
    for i in range(len(table)):
        for j in range(len(table) - 1):
            if table[i][j + 1] != 0 and table[i][j] == 0:
                table[i][j], table[i][j + 1] = table[i][j + 1], table[i][j]


def Add_left():
    for i in range(len(table)):
        for j in range(len(table) - 1):
            if table[i][j + 1] != 0 and table[i][j] == table[i][j + 1]:
                table[i][j + 1] = 0
                table[i][j] *= 2


def Move_right():
    for i in range(len(table)):
        for j in range(len(table) - 1):
            if table[i][len(table) - 2 - j] != 0 and table[i][len(table) - 1 - j] == 0:
                table[i][len(table) - 1 - j], table[i][len(table) - 2 - j] = table[i][len(table) - 2 - j], \
                                                                             table[i][len(table) - 1 - j]


def Add_right():
    for i in range(len(table)):
        for j in range(len(table) - 1):
            if table[i][len(table) - 2 - j] != 0 and table[i][len(table) - 1 - j] == table[i][len(table) - 2 - j]:
                table[i][len(table) - 2 - j] = 0
                table[i][len(table) - 1 - j] *= 2


def Show_table():
    tabletoshow = ""
    for i in range(len(table)):
        for j in range(len(table)):
            tabletoshow += str(table[i][j]) + " "
        tabletoshow += "\n"
    print(tabletoshow)


def Generaterand():
    emptyindexes = []
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 0:
                emptyindexes.append(i * len(table) + j)
    randindex = emptyindexes[random.randint(0, len(emptyindexes)) - 1]
    randdata = random.randint(1, 2)
    if randdata == 1:
        randdata = 2
    elif randdata == 2:
        randdata = 4
    table[randindex // len(table)][randindex % len(table)] = randdata


if __name__ == '__main__':
    Generaterand()
    Show_table()
while True:
    lasttable = copy.deepcopy(table)
    nextmove = str(input())
    print(nextmove)
    if nextmove == "j":  # left
        Move_left()
        Move_left()
        Move_left()
        Add_left()
        Move_left()
    elif nextmove == "i":  # up
        Move_up()
        Move_up()
        Move_up()
        Add_up()
        Move_up()
    elif nextmove == "l":  # right
        Move_right()
        Move_right()
        Move_right()
        Add_right()
        Move_right()
    elif nextmove == "k":  # down
        Move_down()
        Move_down()
        Move_down()
        Add_down()
        Move_down()
    if (lasttable == table):
        print("try another key")
    elif not (lasttable == table):
        Generaterand()
        Show_table()
