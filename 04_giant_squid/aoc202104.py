import pathlib
import sys
import numpy as np

BOARD_SIZE = 5


def parse(puzzle_input):
    """Parse input"""
    data = puzzle_input.split("\n\n")

    draws = [int(x) for x in data[0].split(",")]
    boards = [parse_board(board) for board in data[1:]]

    # print(boards)
    return draws, boards


def parse_board(raw_board):
    """Formats raw board into a nested array"""
    board = []
    for row in raw_board.splitlines():
        board.append([int(x) for x in row.split()])
    return board


def part1(draws, boards):
    """Using draws, identify which board wins bingo first"""

    winning_number, drawn_nums, winning_board = draw(draws, boards, 0)
    
    winning_board_sum = sum([x for x in flatten(winning_board[0]) if x not in drawn_nums])
    
    return winning_number * winning_board_sum


def flatten(l):
    """Flatten a nested list"""
    return [item for sublist in l for item in sublist]


def draw(draws, boards, gamemode=0):
    """Returns winning draw number and winning board with unmarked numbers only.
    Gamemode=0: Returns winning draw number and winning board.
    Gamemode=1: Returns last board to win and draw number"""

    winning_boards = []
    drawn_nums = []
    board_dicts = [[[0, 0, 0, 0, 0,], [0, 0, 0, 0, 0]] for board in boards]

    for draw in draws:  # Iterate through draws
        drawn_nums.append(draw)
        for board_index, board in enumerate(boards):
            if board in winning_boards:
                continue
            for i, x in enumerate(board):
                for y in range(len(x)):
                    if x[y] == draw:
                        board_dicts[board_index][0][i] += 1
                        board_dicts[board_index][1][y] += 1

            if (5 in board_dicts[board_index][0]) or (5 in board_dicts[board_index][1]):  # Board has won
                winning_boards.append(board)
                if gamemode == 0:
                    return draw, drawn_nums, winning_boards
                elif len(winning_boards) == len(boards):
                    return draw, drawn_nums, winning_boards
                else:
                    continue

def part2(draws, boards):
    """Find the final board to win."""

    winning_number, drawn_nums, winning_boards = draw(draws, boards, 1)
    
    final_board = winning_boards[-1]
    final_board_sum = sum([x for x in flatten(final_board) if x not in drawn_nums])

    return winning_number * final_board_sum


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    draws, boards = parse(puzzle_input)
    solution1 = part1(draws, boards)
    solution2 = part2(draws, boards)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
