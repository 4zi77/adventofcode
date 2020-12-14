import numpy as np


def get_instruction(l):
    l = l.split(" ")
    if l[0]=="turn":
        l[0] += l.pop(1)
        if l[0]=="turnon":
            command=1
        else:
            command=0
    else:
        command=2  # Toggle
    [x0, y0] = l[1].split(',')
    [x1, y1] = l[3].split(',')
    return command, int(x0), int(y0), int(x1), int(y1)


def get_data(file):
    f = open(file, "r")
    string_p = f.readlines()
    return string_p

if __name__ == '__main__':
    inpoute = get_data("input.txt")
    grid = [[0 for i in range(1000)] for j in range(1000)]
    for l in inpoute:
        com, x0, y0, x1, y1 = get_instruction(l)
        for i in range(x0, x1+1):
            for j in range(y0, y1+1):
                if com == 0:
                    grid[i][j] -= max(0,grid[i][j]-1)
                else:
                    grid[i][j] += com
    g = np.array(grid)
    print(np.sum(g))
