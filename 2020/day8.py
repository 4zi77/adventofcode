import time

def get_data():
    return open("input.txt", "r").read().split('\n')

if __name__ == '__main__':

    # accu = 0
    L = get_data()
    # line = 0
    # lines = []
    # while True:
    #     l = L[line]
    #     if line in lines:
    #         break
    #     else:
    #         lines.append(line)
    #     if l[:3] == 'acc':
    #         accu += int(l[4:])
    #         line += 1
    #     elif l[:3] == 'jmp':
    #         line += int(l[4:])
    #     else:
    #         line += 1
    # print(accu)

    for idx_m, m in enumerate(L):
        line = 0
        accu = 0
        bugged = 1
        lines = []
        if m[:3] == 'jmp':
            L[idx_m] = m.replace("jmp", "nop")
            while line<len(L):
                l = L[line]
                if line in lines:
                    break
                else:
                    lines.append(line)
                if l[:3] == 'acc':
                    accu += int(l[4:])
                    line += 1
                elif l[:3] == 'jmp':
                    line += int(l[4:])
                else:
                    line += 1
            if line >= len(L):
                bugged = 0
            L[idx_m] = m
        elif m[:3] == 'nop':
            L[idx_m] = m.replace("nop", "jmp")
            while line<len(L):
                l = L[line]
                if line in lines:
                    break
                else:
                    lines.append(line)
                if l[:3] == 'acc':
                    accu += int(l[4:])
                    line += 1
                elif l[:3] == 'jmp':
                    line += int(l[4:])
                else:
                    line += 1
            if line >= len(L):
                bugged = 0
            L[idx_m] = m
        if bugged == 0:
            print(accu, m, idx_m)