import numpy as np

slope = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def get_data():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        return lines


def solve1(lines):
    pattern_len = len(lines[0])-1
    cpt = 0
    for idx_l, l in enumerate(lines):
        pos = (3 * idx_l) % pattern_len
        if l[pos] == '#':
            cpt += 1
    return cpt


def solve2(lines):
    pattern_len = len(lines[0])-1
    cpt = [0 for _ in range(len(slope))]
    for idx_l, l in enumerate(lines):
        for idx_s, s in enumerate(slope):
            if idx_l % s[1] == 0:
                pos = (s[0] * idx_l) % pattern_len
                if l[pos] == '#':
                    cpt[idx_s] += 1
    cpt_arr = np.array(cpt)
    return np.prod(cpt_arr)


if __name__ == '__main__':
    inpoute = get_data()
    print(solve1(inpoute))
    print(solve2(inpoute))
