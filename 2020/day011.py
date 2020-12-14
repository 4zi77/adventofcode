import time

start = time.time()
lines = open("input.txt").readlines()
seats = [list(line[:-1]) for line in lines]

rows, cols = len(seats), len(seats[0])
dij = [(i, j) for i in range(-1,2) for j in range(-1,2) if (i or j)]

def count_adjacent2(seats, i, j):
    cpt = 0
    for di, dj in dij:
        vi, vj = i+di, j+dj
        while 0<=vi<rows and 0<=vj<cols:
            cur_seat = seats[vi][vj]
            if cur_seat == '#':
                cpt+=1
                break
            elif cur_seat == 'L':
                break
            vi += di
            vj += dj
    return cpt

def count_adjacent(seats, i, j):
    cpt = 0
    for di, dj in dij:
        vi, vj = i+di, j+dj
        if 0<=vi<rows and 0<=vj<cols and seats[vi][vj]=='#':
            cpt+=1
    return cpt

def update_single_seat(seats, row, col):
    cur_seat = seats[row][col]
    if cur_seat == '.':
        return cur_seat
    cpt_adj = count_adjacent2(seats, row, col)
    if cur_seat == 'L' and cpt_adj == 0:
        return '#'
    elif cur_seat == '#' and cpt_adj >= 5:
        return 'L'
    else:
        return cur_seat


def update_seats(seats):
    return [[update_single_seat(seats, i, j) for j in range(len(seats[i]))] for i in range(len(seats))]


def print_seats(seats):
    for row in seats:
        print(row)
    print('\n')

if __name__ == '__main__':
    next_seats = update_seats(seats)
    while next_seats != seats:
        seats = next_seats
        next_seats = update_seats(seats)
    # print_seats(next_seats)
    print(sum(seat == '#' for line in seats for seat in line))
    print(time.time()-start)