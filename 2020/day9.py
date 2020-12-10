
def get_product_pair_sum(L, val):
    for id_i, i in enumerate(L):
        for j in L[id_i+1:]:
            if (int(i) + int(j)) == val:
                return 1
    return 0

def get_data():
    return open("input.txt", "r").read().split('\n')


if __name__ == '__main__':
    L = get_data()
    start = 0
    end = 25
    value = L[start:end]
    for l in L[25:]:
        if get_product_pair_sum(value, int(l)) == 0:
            val_to_reach = int(l)
            break
        start += 1
        end += 1
        value = L[start:end]

    new_L = L[:end]
    start = 0
    end = 0
    the_sum = int(new_L[0])
    while the_sum != val_to_reach:
        # print(the_sum)
        if the_sum > val_to_reach:
            start += 1
            end = start
            the_sum = int(new_L[start])
        else:
            the_sum += int(new_L[end])
        end += 1
    new_L = [int(i) for i in L[start:end]]
    print(min(new_L)+max(new_L))
