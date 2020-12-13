# 10e 4n --> 4e 10s [10, 4] --> [4, -10] --> [-10, -4] --> [-4, 10]
dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def moving_grid2(L, ship_pos, way_pos):
    for l in L:
        inst = l[0]
        val = int(l[1:])
        if inst == 'N':
            way_pos[1] += val
        elif inst == 'S':
            way_pos[1] -= val
        elif inst == 'E':
            way_pos[0] += val
        elif inst == 'W':
            way_pos[0] -= val
        elif inst == 'L':
            val = val // 90
            if val % 2 == 0:
                if val % 4 == 2:
                    way_pos[0], way_pos[1] = -way_pos[0], -way_pos[1]
            else:
                if val % 4 == 1:
                    way_pos[0], way_pos[1] = -way_pos[1], way_pos[0]
                else:
                    way_pos[0], way_pos[1] = way_pos[1], -way_pos[0]
        elif inst == 'R':
            val = val // 90
            if val % 2 == 0:
                if val % 4 == 2:
                    way_pos[0], way_pos[1] = -way_pos[0], -way_pos[1]
            else:
                if val % 4 == 1:
                    way_pos[0], way_pos[1] = way_pos[1], -way_pos[0]
                else:
                    way_pos[0], way_pos[1] = -way_pos[1], way_pos[0]
        elif inst == 'F':
            ship_pos[0] += val * way_pos[0]
            ship_pos[1] += val * way_pos[1]

    return ship_pos

def moving_grid1(L, ship_pos, i_facing):
    pos = ship_pos
    print(L)
    for l in L:
        inst = l[0]
        val = int(l[1:])
        if inst == 'N':
            pos[1] += val
        elif inst == 'S':
            pos[1] -= val
        elif inst == 'E':
            pos[0] += val
        elif inst == 'W':
            pos[0] -= val
        elif inst == 'L':
            i_facing = (i_facing - val // 90) % len(dir)
        elif inst == 'R':
            i_facing = (i_facing + val // 90) % len(dir)
        elif inst == 'F':
            pos[0] += val * dir[i_facing][0]
            pos[1] += val * dir[i_facing][1]
    return pos

def get_data():
    return open("input.txt", "r").read().split('\n')

if __name__ == '__main__':
    L = get_data()
    pos_ship = [0, 0]  # x, y
    pos_waypoint = [10, 1]
    # i_facing = 0
    # pos = moving_grid1(L, pos_ship, i_facing)
    # print(pos)
    # print(sum(map(abs, pos)))
    pos = moving_grid2(L, pos_ship, pos_waypoint)
    print(pos)
    print(sum(map(abs, pos)))

