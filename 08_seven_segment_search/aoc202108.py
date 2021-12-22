import pathlib
import sys
from collections import defaultdict


def parse(puzzle_input):
    """Parse input"""
    lines = [x for x in puzzle_input.split("\n")]
    data = []
    for line in lines:
        line = line.split(" | ")
        data.append((line[0], line[1]))

    return data


def part1(data):
    """Find all instances of digits 1, 4, 7 or 8 in output values"""
    count = 0
    for input_, output_ in data:
        for val in output_.split(" "):
            if len(val) in [2, 3, 4, 7]:
                count += 1
    return count


def part2(data):
    """Decode all of the scrambled mappings"""
    final_numbers = []

    for line in data:
        mapping = decode(line[0])
        translated_output = translate(line[1], mapping)
        final_numbers.append(int(translated_output))

    return sum(final_numbers)


def decode(input):
    """Decodes an input string"""
    # print("decoding: ", input.split(" "))
    number_mappings = {}
    # letter_mappings = {}

    tokens = input.split(" ")
    for token in tokens:
        if len(token) == 2:
            number_mappings[1] = set(token)
        elif len(token) == 3:
            number_mappings[7] = set(token)
        elif len(token) == 4:
            number_mappings[4] = set(token)
        elif len(token) == 7:
            number_mappings[8] = set(token)

    a = number_mappings[7] - number_mappings[1]

    five_segment_numbers = [x for x in tokens if len(x) == 5]  # 2, 3, 5
    six_segment_numbers = [x for x in tokens if len(x) == 6]  # 0, 6, 9

    number_mappings[6] = [
        set(x)
        for x in six_segment_numbers
        if (list(set("abcdefg") - set(x)))[0] in number_mappings[1]
    ][0]

    c = number_mappings[1] - number_mappings[6]
    f = number_mappings[1].intersection(number_mappings[6])

    b = number_mappings[4] - number_mappings[1]
    d = number_mappings[4] - number_mappings[1]

    number_mappings[0] = [
        set(x)
        for x in six_segment_numbers
        if (list(set("abcdefg") - set(x)))[0] in b
    ]

    d = set("abcdefg") - number_mappings[0][0]
    b = b - d

    e = set("abcdefg") - a - b - c - d - f
    g = e

    number_mappings[9] = [
        set(x)
        for x in six_segment_numbers
        if (list(set("abcdefg") - set(x)))[0] in e
    ]

    e = set("abcdefg") - number_mappings[9][0]
    g = g - e

    # print(number_mappings)
    mapping = [a, b, c, d, e, f, g]
    letters = ["a", "b", "c", "d", "e", "f", "g"]

    # for letter, code in zip(letters, mapping):
    #     print(letter, ":", code)

    # print(list(zip(letters, mapping)))

    return list(zip(letters, mapping))


def translate(input, mapping):
    """Translates an input string using a custom mapping, returns the translated input as an int"""
    traditional_mapping = {
        frozenset("abcefg"): 0,
        frozenset("cf"): 1,
        frozenset("acdeg"): 2,
        frozenset("acdfg"): 3,
        frozenset("bcdf"): 4,
        frozenset("abdfg"): 5,
        frozenset("abdefg"): 6,
        frozenset("acf"): 7,
        frozenset("abcdefg"): 8,
        frozenset("abcdfg"): 9,
    }

    new_mapping = [(list(y)[0], x) for (x, y) in mapping]

    input = input.split(" ")

    final_number = ""

    for token in input:
        translation = ""
        for char in token:
            translation += [x[1] for x in new_mapping if x[0] == char][0]
        translation_number = [
            x[1]
            for x in traditional_mapping.items()
            if x[0] == frozenset(translation)
        ][0]
        final_number += str(translation_number)

    return final_number


part2(
    [
        (
            "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab",
            "cdfeb fcadb cdfeb cdbaf",
        )
    ]
)


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
