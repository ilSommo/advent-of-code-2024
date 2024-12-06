"""Day 6: Guard Gallivant"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools


def main():
    """Solve day 6 stars."""
    with open("data/day_6.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first star."""
    obstructions, guard = load_map(puzzle_input)
    direction = -1 + 0j
    positions = set()

    while 0 <= guard.real < len(puzzle_input) and 0 <= guard.imag < len(
        puzzle_input[0].rstrip()
    ):
        positions.add(guard)

        if guard + direction not in obstructions:
            guard = guard + direction

        else:
            direction *= -1j

    return len(positions)


def star_2(puzzle_input):
    """Solve second star."""
    obstructions, guard = load_map(puzzle_input)
    looping_obstructions = 0

    for i, j in itertools.product(
        range(len(puzzle_input)), range(len(puzzle_input[0].rstrip()))
    ):
        if i + j * 1j not in obstructions and i + j * 1j != guard:
            new_obstructions = obstructions.copy()
            new_obstructions.add(i + j * 1j)
            positions_directions = set()
            new_guard = guard
            direction = -1 + 0j

            while 0 <= new_guard.real < len(
                puzzle_input
            ) and 0 <= new_guard.imag < len(puzzle_input[0].rstrip()):
                if (new_guard, direction) in positions_directions:
                    looping_obstructions += 1
                    break

                positions_directions.add((new_guard, direction))

                if new_guard + direction not in new_obstructions:
                    new_guard = new_guard + direction

                else:
                    direction *= -1j

    return looping_obstructions


def load_map(puzzle_input):
    """Load puzzle map."""
    obstructions = set()
    for i, row in enumerate(puzzle_input):
        for j, position in enumerate(row):
            match position:
                case "#":
                    obstructions.add(i + j * 1j)

                case "^":
                    guard = i + j * 1j

    return obstructions, guard


if __name__ == "__main__":
    main()
