import pprint
with open('input.txt', 'r') as f:
    octopi = f.read().split()

octopi = [[int(o) for o in row] for row in octopi]


def get_neighbors(octopi, row, col):
    flashed_neighbors = []
    neighbor_list = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]
    for rowdiff, coldiff in neighbor_list:
        if 0 <= row + rowdiff < len(octopi) and 0 <= col + coldiff < len(octopi[0]):
            flashed_neighbors.append((row + rowdiff, col + coldiff))
    return flashed_neighbors


def simulate_octopi(octopi):
    flashes = 0
    for i in range(100):
        # increment each octopus energy by 1
        octopi = [list(map(lambda o: o + 1, r)) for r in octopi]
        flash_list = []
        # while there are flashes to occur
        while any(i >= 10 for i in [o for row in octopi for o in row]):
            prev_list_len = len(flash_list)
            # loop through all the values to find new flashes
            for ridx, row in enumerate(octopi):
                for cidx, o in enumerate(row):
                    # see if it's to flash and hasn't already flashed
                    if o > 9 and (ridx, cidx) not in flash_list:
                        # add this to the flash list
                        flash_list.append((ridx, cidx))
                        # get neighbors and increment them by one
                        neighbors = get_neighbors(octopi, ridx, cidx)
                        for nrow, ncol in neighbors:
                            octopi[nrow][ncol] += 1
            # if no new flashes added we can go to the next turn
            if len(flash_list) == prev_list_len:
                break
        # increment flashes
        flashes += len(flash_list)
        # reset each flashed octopus to 0
        for frow, fcol in flash_list:
            octopi[frow][fcol] = 0
    return flashes


def find_first_all_flash(octopi):
    # start at turn one
    i = 1
    # we know this will eventually terminate so we can do this
    while True:
        # increment all octopus energies by 1
        octopi = [list(map(lambda o: o + 1, r)) for r in octopi]
        flash_list = []
        # while there are flashes to occur
        while any(i >= 10 for i in [o for row in octopi for o in row]):
            # store the previous amount of flashes to 
            prev_list_len = len(flash_list)
            # loop through all the values to find new flashes
            for ridx, row in enumerate(octopi):
                for cidx, o in enumerate(row):
                    # see if it's to flash and hasn't already flashed
                    if o > 9 and (ridx, cidx) not in flash_list:
                        # add this to the flash list
                        flash_list.append((ridx, cidx))
                        # get neighbors and increment them by one
                        neighbors = get_neighbors(octopi, ridx, cidx)
                        for nrow, ncol in neighbors:
                            octopi[nrow][ncol] += 1
            # if no changes in the amount of flashes, we can go onto the next step
            if len(flash_list) == prev_list_len:
                break
        # reset all flashed octopi to 0
        for frow, fcol in flash_list:
            octopi[frow][fcol] = 0
        # if every octopi flashed this turn, return the current turn
        if len(flash_list) == 100:
            return i
        # incrememnt the turn by 1
        i += 1


def part1():
    return simulate_octopi(octopi)


def part2():
    return find_first_all_flash(octopi)


print(f'PART 1: {part1()}')

print(f'PART 2: {part2()}')
