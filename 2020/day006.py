def get_data():
    L = open("input.txt", "r").read().split('\n\n')
    return L

if __name__ == '__main__':
    # L = get_data()
    # cpt = 0
    # for l in L:
    #     s = l.split('\n')
    #     if len(s)==1:
    #         cpt+=len(s[0])
    #     else:
    #         res = s[0]
    #         for p in s:
    #             for c in p:
    #                 if c not in res:
    #                     res+=c
    #         cpt+=len(res)
    # print(cpt)
    cpt = 0
    with open('input.txt', 'r') as data:
        for group in data.read().split('\n\n'):
            person = group.strip().split('\n')
            cpt += len(set(person[0]).intersection(*[set(a) for a in person[1:]]))
        print(cpt)