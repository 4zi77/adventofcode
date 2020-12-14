
voyels = 'aeiou'
naughty = ['ab', 'cd', 'pq', 'xy']

def is_str_correct2(s):
    has_pair = False
    has_mirror = False
    for idx_c, c in enumerate(s):
        if idx_c < len(s) - 1:
            c_next = s[idx_c + 1]
            pair = c+c_next
            if not(has_pair):
                if (s[idx_c+2:]).count(pair)>0:
                    true_pair = pair
                    has_pair = True
            if not(has_mirror) and idx_c<len(s)-2:
                if c == s[idx_c+2]:
                    true_mirror = pair+s[idx_c+2]
                    has_mirror = True
    if has_pair and has_mirror:
        print(s, true_pair, true_mirror)
        return 1
    return 0

def is_str_correct(s):
    cpt_voy = 0
    red = False
    for idx_c, c in enumerate(s):
        for v in voyels:
            if cpt_voy<3 and v == c:
                cpt_voy += 1
        if idx_c<len(s)-1:
            c_next = s[idx_c+1]
            if not red:
                if c == c_next:
                    red = True
            for n in naughty:
                if n[0] == c and n[1] == c_next:
                    # print(s, c, c_next)
                    return 0
    # print(s, cpt_voy >= 3, red)
    if cpt_voy >= 3 and red:
        return 1
    return 0

def get_data(file):
    f = open(file, "r")
    string_p = f.readlines()
    return string_p

if __name__ == '__main__':
    inpoute = get_data("input.txt")
    cpt = 0
    for s in inpoute:
        cpt += is_str_correct2(s)
    print(cpt)