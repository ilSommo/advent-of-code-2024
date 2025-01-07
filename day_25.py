"""Day 25: Code Chronicle"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import itertools
import operator


def main():
    """Solve day 25 puzzles."""
    with open("data/day_25.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    locks, keys = load_locks_keys(puzzle_input)
    fits = set()

    for lock, key in itertools.product(locks, keys):
        fit = list(map(operator.add, lock, key))

        if max(fit) < 6:
            fits.add((lock, key))

    return len(fits)


def load_locks_keys(puzzle_input):
    """Load loack and keys from input."""
    locks = []
    keys = []
    row = 0

    while row < len(puzzle_input):
        if puzzle_input[row][0] == "#":
            lock = [0, 0, 0, 0, 0]

            for line in puzzle_input[row + 1 : row + 6]:
                for i, elem in enumerate(line):
                    if elem == "#":
                        lock[i] += 1

            locks.append(tuple(lock))
            row += 8

        elif puzzle_input[row][0] == ".":
            key = [5, 5, 5, 5, 5]

            for line in puzzle_input[row + 1 : row + 6]:
                for i, elem in enumerate(line):
                    if elem == ".":
                        key[i] -= 1

            keys.append(tuple(key))
            row += 8

    return tuple(locks), tuple(keys)


if __name__ == "__main__":
    main()
