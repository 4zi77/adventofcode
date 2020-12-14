import numpy as np

def ribbon_length(L):
    res = 0
    for l in L:
        prod = np.prod(l)
        suml = 2*(np.sum(l)-max(l))
        res += prod + suml
    return res

def paper_area(L):
    res = 0
    for l in L:
        A = [2*(a*b) for a,b in zip(l, np.roll(l, 1))]
        res+=sum(A) + min(A) // 2
    return res

def get_data(file):
    f = open(file, "r")
    L = [list(map(int, l[:-1].split('x'))) for l in f]
    return L

if __name__ == '__main__':
    input = get_data("input.txt")
    print(ribbon_length(input))