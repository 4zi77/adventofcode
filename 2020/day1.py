
def get_product_triplet_sum_2020(L):
    for id_i, i in enumerate(L):
        for id_j, j in enumerate(L[id_i + 1:]):
            if i+j < 2020:
                for k in L[id_j + 1:]:
                    if (i + j + k) == 2020:
                        return i*j*k
    return 0


def get_product_pair_sum_2020(L):
    for id_i, i in enumerate(L):
        for j in L[id_i+1:]:
            if (i + j) == 2020:
                return i*j
    return 0


def get_data(file):
    f = open(file, "r")
    L = [int(line[:-1]) for line in f]
    return L


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inpoute = get_data("in_day1_1.txt")
    print(get_product_triplet_sum_2020(inpoute))




