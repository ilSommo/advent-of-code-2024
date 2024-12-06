"""Day 6: Guard Gallivant"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"


def main():
    """Solve day 6 stars."""
    with open("data/day_6.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first star."""
    n_rows = len(puzzle_input)
    n_cols = len(puzzle_input[0].rstrip())
    obstructions, guard = load_map(puzzle_input)

    positions = get_path(obstructions, guard, (n_rows, n_cols))

    return len(positions)


def star_2(puzzle_input):
    """Solve second star."""
    n_rows = len(puzzle_input)
    n_cols = len(puzzle_input[0].rstrip())
    obstructions, guard = load_map(puzzle_input)

    positions = get_path(obstructions, guard, (n_rows, n_cols)) - {guard}

    looping_obstructions = sum(
        is_loop(obstructions | {position}, guard, (n_rows, n_cols))
        for position in positions
    )

    return looping_obstructions


def get_path(obstructions, guard, dims):
    """Get path of the guard."""
    positions = set()
    direction = -1 + 0j

    while 0 <= guard.real < dims[0] and 0 <= guard.imag < dims[1]:
        positions.add(guard)

        if guard + direction not in obstructions:
            guard = guard + direction

        else:
            direction *= -1j

    return positions


def is_loop(obstructions, guard, dims):
    """Check if there is a loop."""
    positions_directions = set()
    direction = -1 + 0j

    while 0 <= guard.real < dims[0] and 0 <= guard.imag < dims[1]:
        if (guard, direction) in positions_directions:
            return 1

        positions_directions.add((guard, direction))

        if guard + direction not in obstructions:
            guard += direction

        else:
            direction *= -1j

    return 0


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
