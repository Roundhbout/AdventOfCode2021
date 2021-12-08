from itertools import permutations

with open('input.txt', 'r') as f:
    input_file = f.readlines()

signal_output = [s.split(' | ') for s in input_file]


def easy_output_appearances(sig_out):
    EASY_SEGMENTS = {
        1: 2,
        4: 4,
        7: 3,
        8: 7
    }
    output = [s[1].split() for s in sig_out]

    lens = [[len(outval) for outval in row] for row in output]
    appearances = 0
    for row in lens:
        appearances += sum(1 for l in row if l in EASY_SEGMENTS.values())

    return appearances

# so i had to look up how to do this but i think i can explain it now


def sum_outputs(sig_out):
    # create a dict of known strings that map to digits correctly
    defaults = {
        'acedgfb': 8,
        'cdfbe': 5,
        'gcdfa': 2,
        'fbcad': 3,
        'dab': 7,
        'cefabd': 9,
        'cdfgeb': 6,
        'eafb': 4,
        'cagedb': 0,
        'ab': 1
    }

    """sort those strings to have them be a baseline, we're going to try and map each signal
     character by character to match defaults"""
    defaults = {"".join(sorted(key)): val for key, val in defaults.items()}

    total = 0
    # gotta do this for every line
    for line in sig_out:
        # separate signal and output and split into lists
        signal, output = line
        signal = signal.split()
        output = output.split()
        # get every possible permutation for 'abcdefg' (7! == ~5000)
        for p in permutations('abcdefg'):
            """create a mapping of the permutation to the characters in order
            this will allow us to try changing letter by letter until we find
            a mapping that gets us defaults"""
            pmap = {x: y for x, y in zip(p, 'abcdefg')}
            # create new signals and output strs based on the mapping
            newsig = ["".join(pmap[char] for char in word) for word in signal]
            newout = ["".join(pmap[char] for char in word) for word in output]

            # if every word in the mapped signals is in defaults (what we know)
            if all("".join(sorted(word)) in defaults for word in newsig):
                # then we know that we can use this mapping for outputs too
                newout = ["".join(sorted(word)) for word in newout]
                # every new output will also be in defaults, and we can get the digit from there
                total += int("".join(str(defaults[word]) for word in newout))
                break
    return total


def part1():
    return easy_output_appearances(signal_output)


def part2():
    return sum_outputs(signal_output)


print(f'PART 1: {part1()}')
print(f'PART 2: {part2()}')
