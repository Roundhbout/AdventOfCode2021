import time
f = open("input.txt", "r")

depths = list(map(int, f.read().split()))

# count times an item in depths is greater than the item before it
def depth_increases(depths):
    return [depths[i] > depths[i - 1] for i in range(1, len(depths))].count(True)

"""since across comparisons there will always be two common values (the middle two)
we can just see if depths[i] is greater than depths[i - 3]
(i.e. the value that changes from AAA to BBB)"""
def sliding_window_depth_increases(depths):
    ans = [depths[i] > depths[i - 3] for i in range(3, len(depths))].count(True)
    return ans


assert(depth_increases([1, 2, 3, 4, 3]) == 3)
assert(sliding_window_depth_increases([1, 2, 3, 4, 5, 0]) == 2)

print(f"PART 1: {depth_increases(depths)}")
print(f"PART 2: {sliding_window_depth_increases(depths)}")