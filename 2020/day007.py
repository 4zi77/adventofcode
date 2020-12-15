import time

bags = {}
contain_shiny = []


def get_data():
    with open("input.txt", "r") as f:
        for line in f.readlines():
            l2 = line.split(' contain ')
            bags.update({l2[0][:-5]: l2[1].split(", ")})


def add_bags(bag_color, cpt, multiplicator):
    for bag in bags.items():
        if bag[0] == bag_color:
            print(bag)
            for contained in bag[1]:
                if contained[:2] != 'no':  # Bag contains other bags
                    nb_bags = int(contained[0])
                    cpt += multiplicator * nb_bags
                    color_to_check = contained.split(' bag')[0][2:]
                    cpt = add_bags(color_to_check, cpt, multiplicator*nb_bags)
            return cpt


def add_container_bag(bag_color):
    for bag in bags.items():
        for contained in bag[1]:
            if (bag_color in contained) and (bag[0] not in contain_shiny):
                contain_shiny.append(bag[0])
                add_container_bag(bag[0])


if __name__ == '__main__':
    start = time.time()
    get_data()
    name = 'shiny gold'
    add_container_bag(name)
    print(len(contain_shiny))
    count = add_bags(name, 0, 1)
    print(count)
    print(time.time() - start)
