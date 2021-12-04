import pprint

with open('input.txt', 'r') as f:
    input_file = f.readlines()

called_numbers = list(map(int, input_file.pop(0).split(',')))

rows = [[int(num) for num in row.split()] for row in input_file if row != '\n']

boards = []
while rows:
    board = []
    for i in range(5):
        board.append(rows.pop(0))
    boards.append(board)

def mark_spot(board, num):
    """Looks for num on board and makes it negative if found
        This is considered marking that spot and can be identified
        in case of a match

    Args:
        board (List of List of Int): A 5x5 2D array representing a bingo board
        num (Int): The number called in the game that is to be looked for on the board and marked if found
    """
    for row in board:
        if num in row:
            row[row.index(num)] *= -1

def check_bingo(board):
    """Checks if bingo is found on a board vertically or horizontally

    Args:
        board (List of List of Int): A 5x5 2D array representing a bingo board

    Returns:
        boolean: Returns true if bingo is found vertically or horizontally
    """
    row_check = any([all([num < 0 for num in row]) for row in board])
    # zip(*board) is a quick trick to rotate a 2D array, which is useful since it gets each column into a list
    col_check = any([all([num < 0 for num in col]) for col in zip(*board)])
    return row_check or col_check

def play_bingo(boards, called_nums):
    """Plays bingo on all the boards until a winner is found

    Args:
        boards (List of List of List of Int): List of 5x5 2D arrays representing bingo boards to be played with
        called_nums (List of Int): List of numbers that represent the bingo calls (which numbers to mark each round)

    Returns:
        Dict: A dict containing:
            board : the winning board in its final state
            last_num : the winning number that allowed board to achieve victory
            board_idx : the index of board in boards (used for lose_bingo)
    """
    for num in called_nums:
        # mark each board if num is found on it
        for board in boards:
            mark_spot(board, num)
        # check each board if bingo is achieved, return it and the current number calledd if found
        for idx, board in enumerate(boards):
            if check_bingo(board):
                return {'board' : board, 'last_num' : num, 'board_idx' : idx}

def get_answer(winner_board, last_num):
    
    return (sum([sum([num for num in row if num > 0]) for row in winner_board])) * last_num
        
part_1_bingo = play_bingo(boards, called_numbers)

p1ans = get_answer(part_1_bingo['board'], part_1_bingo['last_num'])

print(f"PART 1: {p1ans}")

#-----------------------------------Part 2---------------------------------------------------------

def lose_bingo(boards, called_nums):
    """Find the last board to win in boards

    Args:
        boards (List of List of Int): List of 5x5 2D arrays representing Bingo Boards to be played with
        called_nums (List of Int): List of numbers that represent the bingo calls (which numbers to mark each round)

    Returns:
        Dict: Returns the result of play_bingo on the last winning board
    """
    # keep playing bingo with all the boards until only one board hasn't won
    while len(boards) > 1:
        cur_winner = play_bingo(boards, called_nums)
        # remove the winner from the list of boards in play (we don't want to beat the octupus after all!)
        boards.pop(cur_winner['board_idx'])
    # once we know there's only one board left, play again to get it to it's final marked state and get the winning number for it
    return play_bingo(boards, called_nums)

part_2_bingo = lose_bingo(boards, called_numbers)

p2ans = get_answer(part_2_bingo['board'], part_2_bingo['last_num'])

print(f"PART 2: {p2ans}")