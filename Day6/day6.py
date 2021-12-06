from collections import Counter
from collections import deque

with open('input.txt', 'r') as f:
    input_file = list(map(int, f.read().split(',')))

test_data = [3, 4, 3, 1, 2]


def update_fish_count(fish_count):
    """update the fish count after a day progresses
        does this by rotating the ordered Counter down
        (so count[8] becomes count[7] and so on, and count[0] becomes count[8])
        before this, stores 0 because those fish don't disappear (the 0 becoming 8
        is new offspring) and adds it to count[6] since they then reset their cycle

    Args:
        fish_count (Dict of {int: int}): A counter of the number of fish at <key> day
        of their cycle

    Returns:
        Dict of {int: int}: An updated counter based on the rules above
    """
    # store the amount of fish about to give birth
    fish_refresh = fish_count[0]
    # store the counts into a deque
    count_deque = deque(fish_count.values())
    # use the deques rotation function to shift the counts down by one day
    count_deque.rotate(-1)
    # zip up the old keys with the rotated values into a new dict
    new_count = dict(zip(fish_count.keys(), count_deque))
    # add the amount of fish to give birth to day 6 since they reset their cycle
    new_count[6] += fish_refresh
    return new_count


def simulate_lanternfish_2(fish, days):
    """return the number of lanternfish after days number of days

    Args:
        fish (List of Int): the initial fish to start with
        days (Int): the number of days to simulate offspring generation

    Returns:
        Int: the number of lanternfish at the end of days
    """
    # get counts of fish at the beginning
    fish_count = Counter(fish)
    # add any days up to 8 missing
    for i in range(max(fish_count.keys()) + 1, 9):
        fish_count[i] = 0
    # also add day 0
    fish_count[0] = 0
    # sort the dict so that rotating the deque follows proper day changing
    fish_count = dict(sorted(fish_count.items()))
    # for each day
    for day in range(days):
        # update the fish count
        fish_count = update_fish_count(fish_count)
    
    # return the sum of each count
    return sum(fish_count.values())

def solve_part_1():
    return simulate_lanternfish_2(input_file, 80)

def solve_part_2():
    return simulate_lanternfish_2(input_file, 256)

assert simulate_lanternfish_2(test_data, 80) == 5934

assert simulate_lanternfish_2(test_data, 256) == 26984457539

print(f'PART 1: {solve_part_1()}')

print(f'PART 2: {solve_part_2()}')
