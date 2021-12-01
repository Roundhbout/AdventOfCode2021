f = open("input.txt", "r")

depths = list(map(int, f.read().split()))

def depth_increases(depths):
    return [depths[i] > depths[i - 1] for i in range(1, len(depths))].count(True)

def sliding_window_depth_increases(depths):
    
    windows = [sum(depths[i - 3 : i]) for i in range(3, len(depths) + 1)]
    #print(windows)
    return [windows[i] > windows[i - 1] for i in range(1, len(windows))].count(True)

print(f"PART 1: {depth_increases(depths)}")
print(f"PART 2: {sliding_window_depth_increases(depths)}")