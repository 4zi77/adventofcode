import numpy as np


def get_data():
    with open("test.txt") as f:
        square = [line.strip() for line in f.readlines()]
        square = [[1 if c == "#" else 0 for c in line] for line in square]
        square = np.array(square)
        shape = np.expand_dims(square, 0)
        return shape


def check(pt_val, neighbours):

    if pt_val == 1:
        return int(neighbours in [2, 3])
    return int(neighbours == 3)


def count_nearby(pt, cube, part2=False):

    if part2:
        w, z, y, x = pt[0], pt[1], pt[2], pt[3]
        wmin, wmax = max(0, w - 1), min(w + 2, cube.shape[0])
        zmin, zmax = max(0, z - 1), min(z + 2, cube.shape[1])
        ymin, ymax = max(0, y - 1), min(y + 2, cube.shape[2])
        xmin, xmax = max(0, x - 1), min(x + 2, cube.shape[3])

        nearby_points = cube[wmin:wmax, zmin:zmax, ymin:ymax, xmin:xmax]
    else:
        z, y, x = pt[0], pt[1], pt[2]
        zmin, zmax = max(0, z - 1), min(z + 2, cube.shape[0])
        ymin, ymax = max(0, y - 1), min(y + 2, cube.shape[1])
        xmin, xmax = max(0, x - 1), min(x + 2, cube.shape[2])

        nearby_points = cube[zmin:zmax, ymin:ymax, xmin:xmax]
    result = nearby_points.sum() - cube[pt]
    return result


def transform(input_shape, part2=False):

    input_shape = np.pad(input_shape, 1)
    output_shape = np.zeros(input_shape.shape)

    for index, val in np.ndenumerate(input_shape):
        neighbours = count_nearby(index, input_shape, part2)
        output_shape[index] = check(val, neighbours)

    return output_shape


if __name__ == '__main__':
    hypercube = get_data()
    hypercube2 = np.expand_dims(hypercube, 0)
    nb_cycle = 6
    for _ in range(nb_cycle):
        hypercube = transform(hypercube)
        hypercube2 = transform(hypercube2, part2=True)
    print(hypercube.sum(), hypercube2.sum())
