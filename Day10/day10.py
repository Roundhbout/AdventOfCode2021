with open('input.txt', 'r') as f:
    lines = f.read().split()

test_data = ['[({(<(())[]>[[{[]{<()<>>',
            '[(()[<>])]({[<{<<[]>>(',
            '{([(<{}[<>[]}>{[]{[(<()>',
            '(((({<>}<{<{<>}{[]{[]{}',
            '[[<[([]))<([[{}[[()]]]',
            '[{[{({}]{}}([{[{{{}}([]',
            '{<[[]]>}<{[{[{[]{()[[[]',
            '[<(<(<(<{}))><([]([]()',
            '<{([([[(<>()){}]>(<<{{',
            '<{([{{}}[<[[[<>{}]]]>[]]']

PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

ILLEGAL_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

AUTOFILL_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def validate_line(line):
    expected_stack = []
    for char in line:
        # we can always add new open chars, put it at the top of the stack
        if char in PAIRS.keys():
            expected_stack.append(char)
        # close chars can be illegal
        else:
            if char == PAIRS[expected_stack[-1]]:
                expected_stack.pop()
            else:
                return char
    if expected_stack:
        return expected_stack
    else:
        return 'VALID'

def illegal_lines_score(lines):
    score = 0
    for line in lines:
        valid = validate_line(line)
        if valid in PAIRS.values():
            score += ILLEGAL_SCORES[valid]
    return score

def incomplete_lines_scores(lines):
    scores = []
    for line in lines:
        valid = validate_line(line)
        if valid != 'VALID' and valid not in PAIRS.values():
            autofill_score = 0
            while valid:
                char = valid.pop()
                autofill_score *= 5
                autofill_score += AUTOFILL_SCORES[PAIRS[char]]
            scores.append(autofill_score)
    
    return scores

def part1():
    return illegal_lines_score(lines)

def part2():
    scores = sorted(incomplete_lines_scores(lines))
    return scores[len(scores) // 2]

assert illegal_lines_score(test_data) == 26397

print(f'PART 1: {part1()}')

print(f'PART 2: {part2()}')