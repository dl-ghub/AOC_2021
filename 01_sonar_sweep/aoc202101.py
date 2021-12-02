import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]


def part1(data):
    """Count the number of times a number is greater than the previous number"""
    count = sum([1 for i in range(1, len(data)) if data[i] > data[i - 1]])
    return count


def part2(data):
    """Count the number of times a window of 3 data is greater than the previous window"""
    count = sum([1 for i in range(3, len(data)) if data[i] > data[i - 3]])
    return count


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
