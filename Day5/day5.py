from collections import Counter
from bresenham import bresenham
import pprint

with open('input.txt', 'r') as f:
    input_file = list(map(lambda s: s.split(' -> '), f.readlines()))

linepoints = [[list(map(int, coord.split(','))) for coord in line] for line in input_file]
MIN_OVERLAPS = 2

test_points = [[[0,9], [5,9]],
                [[8,0], [0,8]],
                [[9,4], [3,4]],
                [[2,2], [2,1]],
                [[7,0], [7,4]],
                [[6,4], [2,0]],
                [[0,9], [2,9]],
                [[3,4], [1,4]],
                [[0,0], [8,8]],
                [[5,5], [8,2]],
            ]

def generate_line(xy1, xy2, diags):
    x1, y1 = xy1
    x2, y2 = xy2
    line = []
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            line.append((x1, y))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            line.append((x, y1))
    elif diags:    
        line = list(bresenham(x1, y1, x2, y2))
    #print('-------------')
    #print(rc1, rc2)
    #pprint.pprint(line)
    return line

def map_points(linepoints, diags):

    lines = [tuple(point) for line in list(map(lambda s: generate_line(s[0], s[1], diags), linepoints)) for point in line]
    #print(lines)
    overlaps = Counter(lines)
    return overlaps

def solve_part_1(linepoints):
    overlaps = map_points(linepoints, False)

    return sum(i >= MIN_OVERLAPS for i in overlaps.values())

def solve_part_2(linepoints):
    overlaps = map_points(linepoints, True)
    return sum(i >= MIN_OVERLAPS for i in overlaps.values())

assert(solve_part_1(test_points) == 5)
assert(solve_part_2(test_points) == 12)

print(f"PART 1: {solve_part_1(linepoints)}")

print(f"PART 2: {solve_part_2(linepoints)}")