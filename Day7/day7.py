from collections import Counter
import time

with open('input.txt', 'r') as f:
    input_file = list(map(int, f.read().split(',')))

test_data = [16,1,2,0,4,2,7,1,2,14]

# this is a dumb implementation but it works
def cheapest_align_point(points):
    start = time.time()
    low = min(points)
    high = max(points)
    pointfreqs = Counter(points)
    
    min_cost = float('inf')
    for m in range(low, high):
        min_cost = min(sum(map(lambda p: abs(m - p), points)), min_cost)
    
    print(f'RUNTIME: {time.time() - start}')
    return min_cost

def cheapest_align_point_2(points):
    start = time.time()
    low = min(points)
    high = max(points)
    pointfreqs = Counter(points)
    
    min_cost = float('inf')
    for m in range(low, high):
        min_cost = min(sum(map(lambda p:\
             (abs(m - p) * (abs(m - p) + 1)) // 2, points)), min_cost)
    
    print(f'RUNTIME: {time.time() - start}')
    return min_cost


assert (cheapest_align_point(test_data) == 37)

assert cheapest_align_point_2(test_data) == 168

def part1():
    return cheapest_align_point(input_file)

def part2():
    return cheapest_align_point_2(input_file)

print(f"PART 1: {part1()}")

print(f"PART 2: {part2()}")