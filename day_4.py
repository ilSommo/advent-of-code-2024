"""Day 4: Ceres Search"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools


def main():
    """Solve day 4 stars."""
    with open("data/day_4.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first star."""
    grid = load_grid(puzzle_input)
    total = 0

    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            total += check_coord(grid, i, j)

    return total


def star_2(puzzle_input):
    """Solve second star."""
    grid = load_grid(puzzle_input)
    total = 0

    for i, row in enumerate(grid[1:-1]):
        for j, _ in enumerate(row[1:-1]):
            total += check_x(grid, i + 1, j + 1)

    return total


def check_coord(grid, i, j):
    """Check if XMAS starts at given coordinates."""
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
    """Check if an X-MAS is present at given coordinates."""
    if grid[i][j] == "A":
        for a, b in itertools.product([-1, 1], [-1, 1]):
            if (
                grid[i + a][j + a] == grid[i + b][j - b] == "M"
                and grid[i - a][j - a] == grid[i - b][j + b] == "S"
            ):
                return 1

    return 0


def load_grid(puzzle_input):
    """Load grid from puzzle input."""
    grid = []

    for i, line in enumerate(puzzle_input):
        grid.append([])

        for letter in line.rstrip():
            grid[i].append(letter)

    return grid


if __name__ == "__main__":
    main()
