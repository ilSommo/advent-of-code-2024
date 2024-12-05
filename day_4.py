"""Day 4: Ceres Search"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools


def main():
    with open("data/day_4.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    grid = load_grid(puzzle_input)
    total = 0

    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            total += check_coord(grid, i, j)

    return total


def star_2(puzzle_input):
    grid = load_grid(puzzle_input)
    total = 0

    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            total += check_x(grid, i, j)

    return total


def load_grid(puzzle_input):
    grid = []

    for i, line in enumerate(puzzle_input):
        grid.append([])

        for j, letter in enumerate(line.rstrip()):
            grid[i].append(letter)

    return grid


def check_coord(grid, i, j):
    n_rows = len(grid)
    n_cols = len(grid[0])
    total = 0

    if grid[i][j] == "X":
        for ii, jj in itertools.product(range(-1, 2), range(-1, 2)):
            if 0 <= i + 3 * ii < n_rows and 0 <= j + 3 * jj < n_cols:
                if (
                    grid[i + ii][j + jj] == "M"
                    and grid[i + 2 * ii][j + 2 * jj] == "A"
                    and grid[i + 3 * ii][j + 3 * jj] == "S"
                ):
                    total += 1

    return total


def check_x(grid, i, j):
    n_rows = len(grid)
    n_cols = len(grid[0])

    if grid[i][j] == "A" and 1 <= i < n_rows - 1 and 1 <= j < n_cols - 1:
        if (
            grid[i - 1][j - 1] == "M"
            and grid[i + 1][j + 1] == "S"
            or grid[i - 1][j - 1] == "S"
            and grid[i + 1][j + 1] == "M"
        ):
            if (
                grid[i - 1][j + 1] == "M"
                and grid[i + 1][j - 1] == "S"
                or grid[i - 1][j + 1] == "S"
                and grid[i + 1][j - 1] == "M"
            ):
                return 1

    return 0


if __name__ == "__main__":
    main()
