import pathlib
import sys
from statistics import median


def parse(puzzle_input):
    return [int(x) for x in puzzle_input.split(",")]


def part1(data):
    """Given a set of x coordinates, calculate the centroid, and then find the total distance between each point and the centroid"""
    centroid = median(data)

    return sum([abs(x - centroid) for x in data])


def part2(data):

    """Same as part one, except fuel increases linearly with distance from the centroid"""
    centroid = int(sum(data) / len(data))

    sum_ = 0

    for x in data:
        distance = abs(x - centroid)
        sum_ += (distance * (distance + 1)) / 2

    return sum_


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
