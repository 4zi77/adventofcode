
def get_data():
    with open("input.txt", "r") as f:
        return f.read().split('\n')


def solve1(values):
    start, end, val_to_reach = 0, 25, 0
    curr_values = values[start:end]
    for val in values[25:]:
        if get_product_pair_sum(curr_values, int(val)) == 0:
            val_to_reach = int(val)
            break
        start += 1
        end += 1
        curr_values = values[start:end]
    return val_to_reach, end


def solve2(values, val_to_reach, new_end):
    new_values = values[:new_end]
    start = 0
    end = 0
    the_sum = int(new_values[0])
    while the_sum != val_to_reach:
        if the_sum > val_to_reach:
            start += 1
            end = start
            the_sum = int(new_values[start])
        else:
            the_sum += int(new_values[end])
        end += 1
    new_values = [int(i) for i in values[start:end]]
    print(min(new_values) + max(new_values))


def get_product_pair_sum(L, val):
    for id_i, i in enumerate(L):
        for j in L[id_i+1:]:
            if (int(i) + int(j)) == val:
                return 1
    return 0


if __name__ == '__main__':
    values = get_data()
    end_val, idx_end = solve1(values)
    print(end_val)
    print(solve2(values, end_val, idx_end))
