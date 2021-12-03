f = open("input.txt", "r")

input_file = f.read().split()

binaries = [[int(bit) for bit in row] for row in input_file]
# print(binaries)


def gamma_rate(bins):
    most_common_bit = []

    columns = list(zip(*bins))
    for c in columns:
        if c.count(1) > c.count(0):
            most_common_bit.append("1")
        else:
            most_common_bit.append("0")
    return "".join(most_common_bit)


def most_common_bit(bins, idx):
    columns = list(zip(*bins[::-1]))
    c = columns[idx]
    ones = c.count(1)
    zeroes = c.count(0)
    if ones > zeroes:
        return "1"
    elif zeroes > ones:
        return "0"
    else:
        return "X"


def least_common_bit(bins, idx):
    columns = list(zip(*bins[::-1]))
    c = columns[idx]
    ones = c.count(1)
    zeroes = c.count(0)
    if ones < zeroes:
        return "1"
    elif zeroes < ones:
        return "0"
    else:
        return "X"


def invert_binary(b):
    res = []
    for bit in b:
        if bit == "1":
            res.append("0")
        else:
            res.append("1")
    return "".join(res)


test_data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]

test_binaries = [[int(bit) for bit in row] for row in test_data]


assert(gamma_rate(test_binaries) == '10110')
part_1_gamma = gamma_rate(binaries)

part_1_epsilon = invert_binary(part_1_gamma)

part_1_gamma_val = int(part_1_gamma, 2)

part_1_epsilon_val = int(part_1_epsilon, 2)

print(f"PART 1: {part_1_gamma_val * part_1_epsilon_val}")


def find_oxy_rating(bins):
    l = len(bins[0])
    for idx in range(l):
        bit = most_common_bit(bins, idx)
        if bit == 'X':
            bit = "1"
        bins = [b for b in bins if b[idx] == int(bit)]

        if len(bins) == 1:
            return "".join(map(str, bins[0]))


def find_co2_rating(bins):
    l = len(bins[0])
    for idx in range(l):
        bit = least_common_bit(bins, idx)
        if bit == 'X':
            bit = "0"
        bins = [b for b in bins if b[idx] == int(bit)]
        if len(bins) == 1:
            return "".join(map(str, bins[0]))


assert(find_oxy_rating(test_binaries) == "10111")
assert(find_co2_rating(test_binaries) == "01010")

part_2_oxygen = find_oxy_rating(binaries)
part_2_co2 = find_co2_rating(binaries)
part_2_oxygen_val = int(part_2_oxygen, 2)
part_2_co2_val = int(part_2_co2, 2)

print(f"PART 2: {part_2_co2_val * part_2_oxygen_val}")
