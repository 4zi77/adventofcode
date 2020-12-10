import numpy as np

slope = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def get_data(file):
    L = f.readlines()
    return L


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inpoute = get_data("in_day3.txt")
    pattern_len = len(inpoute[0])-1
    # print(pattern_len)
    # Solution 1
    # cpt = 0
    # for idx_l, l in enumerate(inpoute):
    #     pos = (3*idx_l)%pattern_len
    #     if l[pos] == '#':
    #         # print(l, pos)
    #         cpt += 1
    # print(cpt)

    # Solution 2
    cpt = [0 for i in range(len(slope))]
    for idx_l, l in enumerate(inpoute):
        for idx_s, s in enumerate(slope):
            if idx_l%s[1]==0:
                pos = (s[0]*idx_l)%pattern_len
                if l[pos] == '#':
                    cpt[idx_s] += 1
    print(cpt)
    cpt_arr = np.array(cpt)
    print(np.prod(cpt_arr))