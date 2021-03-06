with open('input.txt', 'r') as f:
    heightmap = [[int(p) for p in row if p != '\n'] for row in f.readlines()]


def get_neighbors(heightmap, row, col):
    maxrow = len(heightmap)
    maxcol = len(heightmap[0])
    neighborcoords = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    valid_neighbors = []
    for n in neighborcoords:
        rowdiff, coldiff = n
        if (0 <= row + rowdiff < maxrow) and (0 <= col + coldiff < maxcol):
            valid_neighbors.append((row + rowdiff, col + coldiff))
    
    return valid_neighbors

def find_low_points(heightmap):
    low_points = []
    for row, l in enumerate(heightmap):
        for col, point in enumerate(l):
            pneighbors = get_neighbors(heightmap, row, col)
            if all(point < heightmap[r][c] for r, c in pneighbors):
                low_points.append((row, col))
    return low_points

def create_basin(heightmap, lowpoint):
    frontier = [lowpoint]
    explored = []
    while frontier:
        curpoint = frontier.pop(0)
        explored.append(curpoint)
        currow, curcol = curpoint
        curneighbors = get_neighbors(heightmap, currow, curcol)
        for n in curneighbors:
            if n not in frontier and n not in explored:
                nrow, ncol = n
                if heightmap[nrow][ncol] < 9:
                    frontier.append(n)
    return explored

""" Current Idea:
    given that we can get low points with find_low_points,
    recursively run get_neighbors() on that point and it's neighbor until
    no non-9 can be found (on the origin point then it's immediate neighbors)
    and return a list of that"""
def find_basins(heightmap):
    low_points = find_low_points(heightmap)
    basins = []
    for lp in low_points:
        basins.append(create_basin(heightmap, lp))
    
    return basins

def part1():
    low_points = find_low_points(heightmap)
    return sum(heightmap[r][c] + 1 for r,c in low_points)
def part2():
    basins = sorted(find_basins(heightmap), key=lambda b: len(b), reverse=True)
    product = 1
    for i in range(3):
        product *= len(basins.pop(0))
    return product

print(f'PART 1: {part1()}')
print(f'PART 2: {part2()}')
