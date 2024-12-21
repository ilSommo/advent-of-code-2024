"""Day 20: Race Condition"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

DIRECTIONS = {1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j}


def main():
    """Solve day 20 puzzles."""
    with open("data/day_20.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    start, end, walls = load_racetrack(puzzle_input)
    base_path = compute_base_path(start, end, walls)

    return count_cheats(base_path, 2, 100)


def star_2(puzzle_input):
    """Solve second puzzle."""
    start, end, walls = load_racetrack(puzzle_input)
    base_path = compute_base_path(start, end, walls)

    return count_cheats(base_path, 20, 100)


def compute_base_path(start, end, walls):
    """Compute base path."""
    path = [start]
    last_direction = set()

    while path[-1] != end:
        for direction in DIRECTIONS - last_direction:
            new_position = path[-1] + direction

            if new_position not in set(path) | walls:
                path.append(new_position)
                last_direction = {-direction}
                break

    return tuple(path)


def count_cheats(base_path, cheat_length, save):
    """Count how many cheats save at least save picoseconds."""
    indexes = {element: i for i, element in enumerate(base_path)}
    set_path = set(base_path)
    cheat_length += 1
    cheats = 0

    for start_i, start in enumerate(base_path):
        for i in range(cheat_length):
            for j in range(cheat_length - i):
                if i == j == 0:
                    continue

                for difference in tuple(
                    {
                        i + j * 1j,
                        -i + j * 1j,
                        -i - j * 1j,
                        i - j * 1j,
                    }
                ):
                    end = start + difference

                    if (
                        end in set_path
                        and indexes[end] - start_i - i - j >= save
                    ):
                        cheats += 1

    return cheats


def load_racetrack(puzzle_input):
    """Load start, end, and walls from puzzle input."""
    walls = set()

    for i, line in enumerate(puzzle_input):
        for j, elem in enumerate(line):
            match elem:
                case "S":
                    start = i + j * 1j

                case "E":
                    end = i + j * 1j

                case "#":
                    walls.add(i + j * 1j)

    return start, end, walls


if __name__ == "__main__":
    main()
