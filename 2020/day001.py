
def get_product_triplet_sum_2020(lines):
    for id_i, i in enumerate(lines):
        for id_j, j in enumerate(lines[id_i + 1:]):
            if i+j < 2020:
                for k in lines[id_j + 1:]:
                    if (i + j + k) == 2020:
                        return i*j*k
    return 0


def get_product_pair_sum_2020(lines):
    for id_i, i in enumerate(lines):
        for j in lines[id_i + 1:]:
            if (i + j) == 2020:
                return i*j
    return 0


def get_data():
    with open("input.txt", "r") as f:
        lines = [int(line[:-1]) for line in f]
        return lines


if __name__ == '__main__':
    inpoute = get_data()
    print(get_product_pair_sum_2020(inpoute))
    print(get_product_triplet_sum_2020(inpoute))
