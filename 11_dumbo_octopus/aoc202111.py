import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [[int(num) for num in x] for x in puzzle_input.split("\n")]


def part1(data, steps):
    """ Determine the number of octopus flashes in n steps """
    
    octopuses = grid_to_dict(data)
    flashes = 0
    
    for _ in range(1, steps + 1):
        octopuses, new_flashes = perform_step(octopuses)
        flashes += new_flashes
            
    return flashes

def part2(data):
    """ Determine when the simulation will synchronise (i.e. all octopus will have a value of 0) """
    
    octopuses = grid_to_dict(data)
    synced = False
    step = 0
    
    while not synced:
        octopuses, new_flashes = perform_step(octopuses)
        if new_flashes == len(data) * len(data[0]):
            return step + 1
        step += 1
    
def grid_to_dict(grid): 
    M = {}
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            M[(x, y)] = value
    return M
        
def perform_step(octopuses):
    """Advances the simulation forwards by one step

    Args:
        octopuses (dict): Existing (coord: value) pairs

    Returns:
        dict, int: Updated octopus dict and number of flashes performed that step
    """
    adjacent = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
    to_flash = []
    flashes = 0
    
    # Increment all octopuses by 1 unless already at 9
    for coords, value in octopuses.items():
        octopuses[coords] += 1
        if value == 9:
            to_flash.append(coords)

    while to_flash:
        x, y = to_flash.pop()
        flashes += 1
        for dx, dy in adjacent:
            x2, y2 = x + dx, y + dy
            try:
                octopuses[(x2, y2)] += 1
                if octopuses[(x2, y2)] == 10:
                    to_flash.append((x2, y2))
            except KeyError:
                continue
    
    for coords, value in octopuses.items():
        if value >= 10:
            octopuses[coords] = 0
            
    return octopuses, flashes

def print_board(data, step, board_size):
    values = list(data.values())
    n = board_size
    values_split = [values[i:i + n] for i in range(0, len(values), n)]
    
    print("\n")
    print(f"After step {step}:")
    for row in values_split:
        string = [str(int) for int in row]
        print("".join(string))

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data, 100)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
