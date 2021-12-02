import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")


def part1(data):
    """Determine final position of submarine. Return depth * horizontal position"""
    position = 0
    depth = 0
    for i in data:
        match i[0]: 
            case "f":
                position += int(i[-1])
            case "d":
                depth += int(i[-1])
            case "u":
                depth -= int(i[-1])
            case _:
                print("There is an error in the input")
                return

    return position * depth


def part2(data):
    """Determine final position of submarine with new variable aim. Return depth * horizontal position"""
    aim = 0
    position = 0
    depth = 0

    for i in data:
        match i[0]:
            case "f":
                position += int(i[-1])
                depth += aim * int(i[-1])
            case "d":
                aim += int(i[-1])
            case "u":
                aim -= int(i[-1])
            case _:
                print("There is an error in the input")
                return
                
    return position * depth


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
