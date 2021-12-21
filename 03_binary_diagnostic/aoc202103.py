import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")


def part1(data):
    """ """
    gamma = ""
    epsilon = ""

    for i in range(len(str(data[0]))):
        count = 0
        for j in range(len(data)):
            if data[j][i] == "1":
                count += 1
            else:
                count -= 1
        if count > 0:
            gamma += "1"
        else:
            gamma += "0"

    epsilon = "".join("1" if x == "0" else "0" for x in gamma)

    return int(gamma, 2) * int(epsilon, 2)


def part2(data):
    """ """

    oxygen_array = data.copy()
    scrubber_array = data.copy()

    oxygen = ""
    scrubber = ""
    for i in range(len(str(oxygen_array[0]))):
        count = 0
        most = ""
        for j in range(len(oxygen_array)):
            if oxygen_array[j][i] == "1":
                count += 1
            else:
                count -= 1
        if count >= 0:
            most = "1"
        else:
            most = "0"

        oxygen += most

        oxygen_array = [x for x in oxygen_array if x[i] == most]

    for i in range(len(str(scrubber_array[0]))):
        count = 0
        least = ""
        for j in range(len(scrubber_array)):
            if scrubber_array[j][i] == "1":
                count += 1
            else:
                count -= 1
        if count >= 0:
            least = "0"
        else:
            least = "1"

        scrubber += least

        if len(scrubber_array) == 1:
            scrubber = scrubber_array[0]
            break
        else:
            scrubber_array = [x for x in scrubber_array if x[i] == least]

        # print(scrubber_array)

    return int(oxygen, 2) * int(scrubber, 2)


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


test = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

# part2(test)
