
f = open("input.txt", "r")
input_file = list(map(lambda s: s.split(), f.readlines()))


def move_sub(directions):
    """Move a sub based on directions

    Args:
        directions (ListOf([Str, Str])): a list of commands, representing
        the direction of the sub and the value of that direction

        eg. ['forward', '4'] moves the sub forward by 4 units. (second string must pass .isdigit()) 

    Returns:
        (): [description]
    """
    vertical_map = {
        "down": 1,
        "up": -1
    }

    horiz_pos = 0
    depth = 0
    for dir, val in directions:
        if dir == 'forward':
            horiz_pos += int(val)
        else:
            depth += int(val) * vertical_map[dir]

    return (horiz_pos, depth)


def aim_sub(directions):

    vertical_map = {
        "down": 1,
        "up": -1
    }

    horiz_pos = 0
    depth = 0
    aim = 0

    for dir, val in directions:
        if dir == 'forward':
            horiz_pos += int(val)
            depth += (aim * int(val))
        else:
            aim += (int(val) * vertical_map[dir])

    return (horiz_pos, depth)


test_list = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2'
]

test_cmds = list(map(lambda s: s.split(), test_list))

assert(move_sub(test_cmds) == (15, 10))
assert(aim_sub(test_cmds) == (15, 60))


part_1_h, part_1_d = move_sub(input_file)

part_1_ans = part_1_h * part_1_d

print(f"PART 1: {part_1_ans}")

part_2_h, part_2_d = aim_sub(input_file)

part_2_ans = part_2_h * part_2_d

print(f"PART 2: {part_2_ans}")
