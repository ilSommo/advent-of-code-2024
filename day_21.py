"""Day 21: Keypad Conundrum"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from functools import cache

DIRECTIONAL_KEYPAD = {
    "^": 0 + 1j,
    "A": 0 + 2j,
    "<": 1 + 0j,
    "v": 1 + 1j,
    ">": 1 + 2j,
}
NUMERIC_KEYPAD = {
    "7": 0 + 0j,
    "8": 0 + 1j,
    "9": 0 + 2j,
    "4": 1 + 0j,
    "5": 1 + 1j,
    "6": 1 + 2j,
    "1": 2 + 0j,
    "2": 2 + 1j,
    "3": 2 + 2j,
    "0": 3 + 1j,
    "A": 3 + 2j,
}


def main():
    """Solve day 21 puzzles."""
    with open("data/day_21.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    complexities = [compute_complexity(code, 2) for code in puzzle_input]

    return sum(complexities)


def star_2(puzzle_input):
    """Solve second puzzle."""
    complexities = [compute_complexity(code, 25) for code in puzzle_input]

    return sum(complexities)


def compute_complexity(line, layers):
    """Compute complexity of line."""
    length = compute_length(line, "numeric", layers)

    return int(line[:3]) * length


@cache
def compute_length(code, keypad, layers):
    """Compute code length."""
    code = "A" + code
    length = 0

    for i, _ in enumerate(code[:-1]):
        start = code[i]
        end = code[i + 1]
        paths = compute_paths(start, end, keypad)

        if layers == 0:
            length += min(len(path) for path in paths)

        else:
            length += min(
                compute_length(path, "directional", layers - 1)
                for path in paths
            )

    return length


@cache
def compute_paths(start, end, keypad):
    """Compute possible paths."""
    keypad = NUMERIC_KEYPAD if keypad == "numeric" else DIRECTIONAL_KEYPAD

    start = keypad[start]
    end = keypad[end]

    paths = [(start, [])]
    full_paths = []

    while paths:
        position, path = paths.pop()

        if position not in keypad.values():
            continue

        if position == end:
            full_paths.append("".join(path + ["A"]))
            continue

        movement = end - position
        row_movement = movement.real
        col_movement = movement.imag

        if col_movement < 0:
            paths.append((position - 1j, path + ["<"]))

        if row_movement < 0:
            paths.append((position - 1, path + ["^"]))

        if col_movement > 0:
            paths.append((position + 1j, path + [">"]))

        if row_movement > 0:
            paths.append((position + 1, path + ["v"]))

    return full_paths


if __name__ == "__main__":
    main()
