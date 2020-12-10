def next_house(santa, char):
    if char == '^':
        return (santa[0], santa[1] + 1)
    elif char == '>':
        return (santa[0] + 1, santa[1])
    elif char == '<':
        return (santa[0] - 1, santa[1])
    elif char == 'v':
        return (santa[0], santa[1] - 1)
    else:
        return santa

def get_data(file):
    f = open(file, "r")
    string_p = f.readline()
    return string_p

if __name__ == '__main__':
    inpoute = get_data("input.txt")
    checked_houses = [(0, 0)]
    santa = (0, 0)
    robo_santa = (0,0)
    s = santa
    for idx_c, c in enumerate(inpoute):
        if idx_c%2==0:
            s = santa
        else:
            s=robo_santa
        s = next_house(s, c)
        if s not in checked_houses:
            checked_houses.append(s)
        if idx_c%2==0:
            santa = s
        else:
            robo_santa = s
    print(len(checked_houses))