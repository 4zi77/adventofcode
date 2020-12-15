def check_password2(li):
    mini, maxi, letter, password = get_values(li)
    if (password[mini-1] == letter) != (password[maxi-1] == letter):
        return 1
    return 0


def check_password(li):
    mini, maxi, letter, password = get_values(li)
    val = password.count(letter)
    if mini <= val <= maxi:
        return 1
    return 0


def get_values(line):

    interval = line[0].split("-")
    mini, maxi = int(interval[0]), int(interval[1])
    return mini, maxi, line[1][0], line[2]


def get_data():
    with open("input.txt", "r") as f:
        lines = [(line[:-1]).split(" ") for line in f]
        return lines


if __name__ == '__main__':
    inpoute = get_data()
    cpt1, cpt2 = 0, 0
    for line in inpoute:
        cpt1 += check_password(line)
        cpt2 += check_password2(line)
    print(cpt1, cpt2)
