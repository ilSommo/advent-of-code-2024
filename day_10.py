"""Day 10: Hoof It"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from collections import defaultdict

DIRECTIONS = [1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j]


def main():
    """Solve day 10 puzzles."""
    with open("data/day_10.txt", encoding="ascii") as input_file:
        puzzle_input = [line.rstrip() for line in input_file.readlines()]

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    heights = read_map(puzzle_input)

    total = sum(
        len(find_trails(0, trailhead, heights)) for trailhead in heights[0]
    )

    return total


def star_2(puzzle_input):
    """Solve second puzzle."""
    heights = read_map(puzzle_input)

    total = sum(
        count_trails(0, trailhead, heights) for trailhead in heights[0]
    )

    return total


def count_trails(height, position, heights):
    """Count possible trails from given position."""
    if height == 9:
        return 1

    total = 0
    possible_positions = heights[height + 1]

    for direction in DIRECTIONS:
        if position + direction in possible_positions:
            total += count_trails(height + 1, position + direction, heights)

    return total


def find_trails(height, position, heights):
    """Find possible trails from given position."""
    if height == 9:
        return {position}

    trailtails = set()
    possible_positions = heights[height + 1]

    for direction in DIRECTIONS:
        if position + direction in possible_positions:
            trailtails.update(
                find_trails(height + 1, position + direction, heights)
            )

    return trailtails


def read_map(puzzle_input):
    """Read map from puzzle input."""
    heights = defaultdict(set)

    for i, line in enumerate(puzzle_input):
        for j, position in enumerate(line):
            heights[int(position)].add(i + j * 1j)

    return dict(heights)


if __name__ == "__main__":
    main()
