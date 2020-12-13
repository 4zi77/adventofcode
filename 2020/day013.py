def get_data1():
    with open("input.txt", "r") as f:
        time_dep = int(f.readline())
        buses = [int(bus) for bus in f.readline().split(',') if bus != 'x']
        return time_dep, buses

def get_data2():
    buses = (open("input.txt", "r").readlines()[1]).split(',')
    return [(i, int(bus)) for i, bus in enumerate(buses) if bus != 'x']

def solve_weird_prime_thing(buses):
    time_dep = 0
    common_mult = 1
    for start, divisor in buses:
        while (time_dep + start) % divisor:
            time_dep += common_mult
        common_mult *= divisor
    return time_dep

def early_bus_val(t, buses):
    mini_t, bus = sorted([bus - t % bus, bus] for bus in buses)[0]
    return mini_t * bus

if __name__ == '__main__':
    t, buses = get_data1()
    print(early_bus_val(t, buses))
    buses = get_data2()
    print(buses)
    print(solve_weird_prime_thing(buses))
