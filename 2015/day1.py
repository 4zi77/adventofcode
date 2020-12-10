# Press the green button in the gutter to run the script.
def enter_basement(str_in):
    floor = 0
    for id_i, i in enumerate(str_in):
        if i == '(':
            floor+=1
        else:
            floor-=1
        if floor==-1:
            return id_i+1


def get_floor(str_in):
    return 2*str_in.count("(")-len(str_in)

def get_data(file):
    f = open(file, "r")
    string_p = f.readline()
    return string_p

if __name__ == '__main__':
    input = get_data("in_day1.txt")
    print(enter_basement(input))



