import time
f = open("input.txt", "r")

depths = list(map(int, f.read().split()))

def depth_increases(depths):
    return [depths[i] > depths[i - 1] for i in range(1, len(depths))].count(True)

def sliding_window_depth_increases(depths):
    start = time.time()
    windows = [sum(depths[i - 3 : i]) for i in range(3, len(depths) + 1)]
    ans = [windows[i] > windows[i - 1] for i in range(1, len(windows))].count(True)
    return ans


assert(depth_increases([1, 2, 3, 4, 3]) == 3)
assert(sliding_window_depth_increases([1, 2, 3, 4, 5, 0]) == 2)

print(f"PART 1: {depth_increases(depths)}")
print(f"PART 2: {sliding_window_depth_increases(depths)}")