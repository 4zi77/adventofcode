import re

keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
fields = {
    'byr': lambda val: 1920 <= int(val) <= 2002,
    'iyr': lambda val: 2010 <= int(val) <= 2020,
    'eyr': lambda val: 2020 <= int(val) <= 2030,
    'hgt': lambda val: val[-2:] == 'cm' and 150 <= int(val[:-2]) <= 193 \
                       or val[-2:] == 'in' and 59 <= int(val[:-2]) <= 76,
    'hcl': lambda val: bool(re.fullmatch('^#[a-f0-9]{6}$', val)),
    'ecl': lambda val: val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda val: bool(re.fullmatch('^[0-9]{9}$', val))
}


def get_data_re():
    with open("input.txt", "r") as f:
        lines = re.sub(r'\n(\S)', r' \1', f.read())
        lines = lines.splitlines()
        return lines


def get_data():
    with open("input.txt", "r") as f:
        lines = f.read().split('\n\n')
        return lines


if __name__ == '__main__':
    res = get_data()
    cpt = 0
    for line in res:
        if all(key in line for key in keys):
            cpt += 1
    print(cpt)

    res = get_data_re()
    cpt = 0
    for line in res:
        doc = {value.split(':')[0]: value.split(':')[1] for value in line.split()}
        if all([field in doc for field in fields]) and all([k == 'cid' or fields[k](val) for k, val in doc.items()]):
            # Enough field                         and field = cid or field respect fields expression
            cpt += 1

    print(cpt)
