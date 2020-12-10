def check_password2(l):
    mini, maxi, letter, password = get_values(l)
    if (password[mini-1]==letter) != (password[maxi-1]==letter):
        return 1
    return 0

def check_password(l):
    mini, maxi, letter, password = get_values(l)
    val = password.count(letter)
    if val>=mini and val<=maxi:
        return 1
    return 0

def get_values(l):

    interval = l[0].split("-")
    mini, maxi = int(interval[0]), int(interval[1])
    return mini, maxi, l[1][0], l[2]


def get_data(file):
    f = open(file, "r")
    L = [(line[:-1]).split(" ") for line in f]
    return L


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inpoute = get_data("in_day2.txt")
    cpt = 0
    for L in inpoute:
        cpt += check_password2(L)
    print(cpt)