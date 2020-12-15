def solve1():
    count = 0
    with open("input.txt", "r") as f:
        for group in f.read().split('\n\n'):
            lines = group.split('\n')
            if len(lines) == 1:
                count += len(lines[0])
            else:
                res = lines[0]
                for person in lines:
                    for answer in person:
                        if answer not in res:
                            res += answer
                count += len(res)
        return count


if __name__ == '__main__':
    print(solve1())
    cpt = 0
    with open('input.txt', 'r') as data:
        for group in data.read().split('\n\n'):
            person = group.strip().split('\n')
            cpt += len(set(person[0]).intersection(*[set(a) for a in person[1:]]))
        print(cpt)
