import pathlib
import sys
from math import prod


def parse(puzzle_input):
    """Parse input"""
    return [[int(num) for num in x] for x in puzzle_input.split("\n")]


def part1(data):
    """Find all points that are lower than all of their orthogonal points"""
    M = grid_to_dict(data)
    low_points = find_low_points(M)

    risk_sum = sum([low_point[1] + 1 for low_point in low_points])

    return risk_sum


def grid_to_dict(data):
    M = {}
    for x, row in enumerate(data):
        for y, value in enumerate(row):
            M[(x, y)] = value

    return M


def part2(data):
    """Find all basins (i.e. grid segments surrounded by 9s) and return product of sizes of 3 largest basins"""
    M = grid_to_dict(data)
    low_points = find_low_points(M)
    basin_sizes = []

    for point, _ in low_points:
        basin_sizes.append(find_basin(M, point))

    basin_sizes.sort()

    return prod(basin_sizes[-3:])


def find_low_points(M):
    adjacent = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    low_points = []

    for coord, value in M.items():
        lowest = True
        for dx, dy in adjacent:
            try:
                if (
                    M[(coord[0] + dx, coord[1] + dy)] <= value
                ):  # Not a low point
                    lowest = False
                    break
            except KeyError:
                continue
        if lowest:
            low_points.append((coord, value))

    return low_points


def find_basin(M, low_point):
    adjacent = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    to_search = [low_point]
    basin = [low_point]

    while to_search:
        x, y = to_search.pop()
        for (dx, dy) in adjacent:
            neighbour = ((x + dx), (y + dy))
            try:
                if 9 > M[neighbour] >= M[(x, y)]:
                    if (neighbour) not in basin:
                        basin.append(neighbour)
                        to_search.append(neighbour)
            except KeyError:
                continue

    return len(basin)


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
