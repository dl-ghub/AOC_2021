import pathlib
import sys
from collections import Counter, defaultdict


def parse(puzzle_input):
    """Parse input"""

    return [int(x) for x in puzzle_input.split(",")]


def part1(data, days):
    """Given a list of integers representing time to new fish, calculate number of fish after x days"""
    NUM_DAYS = days

    counts = Counter(data)

    total_fish = 0

    for _ in range(NUM_DAYS):
        updated_counts = Counter()

        # print(f"After {day + 1} days: {counts}")
        for days_left, fish_count in counts.items():
            if days_left == 0:
                updated_counts[6] += fish_count
                updated_counts[8] += fish_count
            else:
                updated_counts[days_left - 1] += fish_count

        counts = updated_counts

        total_fish = sum(counts.values())

    return total_fish


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data, 80)
    solution2 = part1(data, 256)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
