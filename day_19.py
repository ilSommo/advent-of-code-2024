"""Day 19: Linen Layout"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from collections import defaultdict


def main():
    """Solve day 19 puzzles."""
    with open("data/day_19.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    patterns, designs = load_towels(puzzle_input)

    return sum(is_possible(patterns, design) for design in designs)


def star_2(puzzle_input):
    """Solve second puzzle."""
    patterns, designs = load_towels(puzzle_input)

    return sum(count_ways(patterns, design) for design in designs)


def count_ways(patterns, design):
    """Count how many ways to create design."""
    designs = {design}
    ways = defaultdict(int)
    ways[design] = 1
    correct_ways = 0

    while designs:
        design = sorted(designs, key=len)[-1]
        designs.remove(design)
        current_ways = ways[design]

        for pattern in patterns:
            if design == pattern:
                correct_ways += current_ways

            elif design.startswith(pattern):
                i = len(pattern)
                ways[design[i:]] = ways[design[i:]] + current_ways
                designs.add(design[i:])

    return correct_ways


def is_possible(patterns, design):
    """Check if design is possible."""
    designs = {design}

    while designs:
        design = designs.pop()

        for pattern in patterns:
            if design == pattern:
                return True

            if design.startswith(pattern):
                designs.add(design[len(pattern) :])

    return False


def load_towels(puzzle_input):
    """Load patterns and designs."""
    patterns = tuple(puzzle_input[0].split(", "))
    designs = tuple(puzzle_input[2:])

    return patterns, designs


if __name__ == "__main__":
    main()
