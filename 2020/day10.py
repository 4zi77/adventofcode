import time
import numpy as np
from more_itertools import run_length

# Nombre de permutations équivalentes par occurrences de '1' à la suite
t = {2: 2,
     3: 4,
     4: 7}


def get_data():
    with open("input.txt") as f:
        L = sorted([int(x) for x in f])
    return [0] + L + [max(L) + 3]


if __name__ == '__main__':
    start = time.time()
    numbers = get_data()

    # Calcul de la différence terme à terme entre les éléments
    diffs = np.diff(numbers)

    # Part1 : 1-jolt_diff * 3-jolt_diff
    print((len(diffs[diffs == 1])) * (len(diffs[diffs == 3])))

    # run_length.encode compresse une liste 'abbcccdddd' en [('a', 1), ('b', 2), ('c', 3), ('d', 4)
    # Ou encore [1, 1, 1, 3, 3, 1, 1] en [(1, 3), (3, 2), (1, 2)]
    poss = [t[e] for i, e in run_length.encode(diffs) if i == 1 and e > 1]
    print(np.prod(poss))
    print(time.time() - start)
