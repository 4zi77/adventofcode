import itertools
import numpy as np

def initialize_ferry_dockingV2(L):
    mem = {}
    for l in L:
        if l[0] == "mask":
            mask = np.array(list(l[1]))
            number_X = np.count_nonzero(mask == 'X')
            permutations = [np.array(list("".join(seq))) for seq in itertools.product("01", repeat=number_X)]
        else:
            mem_add = np.array(list(f"{int(l[0][4:-1]):036b}"))
            val = int(l[1])
            mem_add[np.where(mask == '1')] = '1'
            mem_add[np.where(mask == 'X')] = 'X'
            for perm in permutations:
                new_mem_add = np.copy(mem_add)
                new_mem_add[np.where(new_mem_add == 'X')] = perm
                mem[''.join(list(new_mem_add))] = val
    return sum(mem.values())

def initialize_ferry_docking(L):
    mem = {}
    for l in L:
        if l[0] == "mask":
            mask = l[1]
            len_mask = len(mask)
        else:
            mem_id = int(l[0][4:-1])
            val = f"{int(l[1]):036b}"
            mem_val = 0
            for i, bit in enumerate(mask):
                if bit == 'X':
                    mem_val += int(val[i]) * 2 ** (len_mask - i - 1)
                else:
                    mem_val += int(bit) * 2 ** (len_mask - i - 1)
            mem[mem_id] = mem_val
    return sum(mem.values())


def get_data():
    L=[]
    for l in open("input.txt", "r").readlines():
        L.append(l[:-1].split(" = "))
    return L

if __name__ == '__main__':
    L = get_data()
    # print(initialize_ferry_docking(L))
    print(initialize_ferry_dockingV2(L))