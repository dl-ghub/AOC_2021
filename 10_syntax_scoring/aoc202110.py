import pathlib
import sys
from statistics import median


left = ["(", "[", "{", "<"]
right = [")", "]", "}", ">"]

symbols = {"(": 1, ")": 1, "[": 2, "]": 2, "{": 3, "}": 3, "<": 4, ">": 4}
left_to_right = {"(": ")", "[": "]", "{": "}", "<": ">"}

values = {")": 3, "]": 57, "}": 1197, ">": 25137}


def parse(puzzle_input):
    """Parse input"""
    return [x for x in puzzle_input.splitlines()]


def part1(data):
    """Find the location of all incomplete brackets (ignoring incomplete lines)"""
    points = 0

    print(data)

    for line in data:
        # print("~~~~~~~~~~~~~~~")
        # print(line)
        line = [char for char in line]

        valid = True
        i = 0
        while valid:
            if len(line) == 0:  # line is complete and valid
                valid = False
                continue

            j = i + 1

            # print(line)
            # print(i, j)

            if j > (len(line) - 1):  # end of line reached
                # print("end of line reached")
                valid = False
                continue

            leftchar = line[i]
            rightchar = line[j]

            # print(leftchar, rightchar)
            # print("~~~~~~~~~~~~~~~~~~~")

            if line[j] in left:
                i += 1
            elif symbols[line[j]] == symbols[line[i]]:  # closing bracket
                del line[i : j + 1]
                i -= 1
            else:  # incorrect closing bracket
                # print(
                #     f"expected {line[i]} at index {i} but got {line[j]} at index {j}"
                # )
                points += values[line[j]]
                valid = False
                continue

        # print(f"points {points}")

    return points


def part2(data):
    """Find the string that correctly closes each incomplete line"""
    points = 0

    valid_strings = []
    corrupt_strings = []
    closing_string_scores = []

    for string in data:
        line = [char for char in string]

        corrupt = True
        i = 0
        while corrupt:
            if len(line) == 0:  # line is complete and valid
                valid_strings.append(string)
                corrupt = False
                continue

            j = i + 1

            if j > (len(line) - 1):  # end of line reached
                # print("end of line reached")
                valid_strings.append(string)
                corrupt = False
                continue

            leftchar = line[i]
            rightchar = line[j]

            if line[j] in left:
                i += 1
            elif symbols[line[j]] == symbols[line[i]]:  # closing bracket
                del line[i : j + 1]
                i -= 1
            else:  # incorrect closing bracket
                points += values[line[j]]
                corrupt = False
                continue

    # print("~~~~~~~~~~~~~~~~~~~~~")
    # print(valid_strings)

    for string in valid_strings:
        closing_string = ""
        total = 0

        for char in reversed(reduce(string)):
            closing_string += left_to_right[char]
            total *= 5
            total += symbols[char]

        closing_string_scores.append(total)

    return median(closing_string_scores)


def reduce(string):
    """Reduce a string to its smallest form"""
    line = [char for char in string]

    corrupt = True
    i = 0
    while corrupt:
        if len(line) == 0:  # line is complete and valid
            corrupt = False
            continue

        j = i + 1

        if j > (len(line) - 1):  # end of line reached
            # print("end of line reached")
            corrupt = False
            continue

        leftchar = line[i]
        rightchar = line[j]

        if line[j] in left:
            i += 1
        elif symbols[line[j]] == symbols[line[i]]:  # closing bracket
            del line[i : j + 1]
            i -= 1
        else:  # incorrect closing bracket
            points += values[line[j]]
            corrupt = False
            continue

    return "".join(line)


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
