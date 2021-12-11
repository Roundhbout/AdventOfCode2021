import pprint
with open('input.txt', 'r') as f:
    octopi = f.read().split()

octopi = [[int(o) for o in row] for row in octopi]

def flash_neighbors(octopi, row, col):
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
            flashed_neighbors.append((row + rowdiff, col +coldiff))
    return flashed_neighbors

def simulate_octopi(octopi):
    flashes = 0
    
    for i in range(100):
        octopi = [list(map(lambda o : o + 1, r)) for r in octopi]

        flash_list = []
        
        #while there are flashes to occur
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
                        neighbors = flash_neighbors(octopi, ridx, cidx)
                        for nrow, ncol in neighbors:
                            octopi[nrow][ncol] += 1
            if len(flash_list) == prev_list_len:
                break
        flashes += len(flash_list)
        for frow, fcol in flash_list:
            octopi[frow][fcol] = 0
    return flashes

def find_first_all_flash(octopi):

    i = 1
    while True:
        octopi = [list(map(lambda o : o + 1, r)) for r in octopi]

        flash_list = []
        
        #while there are flashes to occur
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
                        neighbors = flash_neighbors(octopi, ridx, cidx)
                        for nrow, ncol in neighbors:
                            octopi[nrow][ncol] += 1
            if len(flash_list) == prev_list_len:
                break
        for frow, fcol in flash_list:
            octopi[frow][fcol] = 0
        if len(flash_list) == 100:
            return i 
    
        i += 1

def part1():
    return simulate_octopi(octopi)

def part2():
    return find_first_all_flash(octopi)

print(f'PART 1: {part1()}')

print(f'PART 2: {part2()}')