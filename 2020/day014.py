import itertools
import numpy as np


def initialize_ferry_dockingV2(instruction_list):
    mem, mask, permutations = {}, [], []
    for inst in instruction_list:
        if inst[0] == "mask":
            mask = np.array(list(inst[1]))
            number_x = np.count_nonzero(mask == 'X')
            permutations = [np.array(list("".join(seq))) for seq in itertools.product("01", repeat=number_x)]
        else:
            mem_add = np.array(list(f"{int(inst[0][4:-1]):036b}"))
            val = int(inst[1])
            mem_add[np.where(mask == '1')] = '1'
            mem_add[np.where(mask == 'X')] = 'X'
            for perm in permutations:
                new_mem_add = np.copy(mem_add)
                new_mem_add[np.where(new_mem_add == 'X')] = perm
                mem[''.join(list(new_mem_add))] = val
    return sum(mem.values())


def initialize_ferry_docking(instruction_list):
    mem, mask, len_mask = {}, [], 0
    for inst in instruction_list:
        if inst[0] == "mask":
            mask = inst[1]
            len_mask = len(mask)
        else:
            mem_id = int(inst[0][4:-1])
            val = f"{int(inst[1]):036b}"
            mem_val = 0
            for i, bit in enumerate(mask):
                if bit == 'X':
                    mem_val += int(val[i]) * 2 ** (len_mask - i - 1)
                else:
                    mem_val += int(bit) * 2 ** (len_mask - i - 1)
            mem[mem_id] = mem_val
    return sum(mem.values())


def get_data():
    inst = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            inst.append(line[:-1].split(" = "))
        return inst


if __name__ == '__main__':
    instructions = get_data()
    # print(initialize_ferry_docking(L))
    print(initialize_ferry_dockingV2(instructions))
