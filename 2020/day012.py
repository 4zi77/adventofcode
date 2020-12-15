# 10e 4n --> 4e 10s [10, 4] --> [4, -10] --> [-10, -4] --> [-4, 10]
facing = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def moving_grid2(instructions, ship_pos, way_pos):
    for line in instructions:
        inst = line[0]
        val = int(line[1:])
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
            if val % 4 == 2:
                way_pos[0], way_pos[1] = -way_pos[0], -way_pos[1]
            elif val % 4 == 1:
                way_pos[0], way_pos[1] = -way_pos[1], way_pos[0]
            elif val % 4 == 3:
                way_pos[0], way_pos[1] = way_pos[1], -way_pos[0]
        elif inst == 'R':
            val = val // 90
            if val % 4 == 2:
                way_pos[0], way_pos[1] = -way_pos[0], -way_pos[1]
            elif val % 4 == 1:
                way_pos[0], way_pos[1] = way_pos[1], -way_pos[0]
            elif val % 4 == 3:
                way_pos[0], way_pos[1] = -way_pos[1], way_pos[0]
        elif inst == 'F':
            ship_pos[0] += val * way_pos[0]
            ship_pos[1] += val * way_pos[1]

    return ship_pos


def moving_grid1(instructions, ship_pos, i_facing):
    pos = ship_pos
    for line in instructions:
        inst = line[0]
        val = int(line[1:])
        if inst == 'N':
            pos[1] += val
        elif inst == 'S':
            pos[1] -= val
        elif inst == 'E':
            pos[0] += val
        elif inst == 'W':
            pos[0] -= val
        elif inst == 'L':
            i_facing = (i_facing - val // 90) % len(facing)
        elif inst == 'R':
            i_facing = (i_facing + val // 90) % len(facing)
        elif inst == 'F':
            pos[0] += val * facing[i_facing][0]
            pos[1] += val * facing[i_facing][1]
    return pos


def get_data():
    with open("input.txt", "r") as f:
        return f.read().split('\n')


if __name__ == '__main__':
    data = get_data()
    pos_ship = [0, 0]  # x, y
    pos_waypoint = [10, 1]
    idx_facing = 0
    coord = moving_grid1(data, pos_ship, idx_facing)
    print(sum(map(abs, coord)))
    coord = moving_grid2(data, pos_ship, pos_waypoint)
    print(sum(map(abs, coord)))
