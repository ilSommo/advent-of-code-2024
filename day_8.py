"""Day 8: Resonant Collinearity"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from collections import defaultdict
import itertools
import math


def main():
    """Solve day 8 stars."""
    with open("data/day_8.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first star."""
    antinodes = set()
    n_rows = len(puzzle_input)
    n_cols = len(puzzle_input[0].rstrip())
    antennas = load_antennas(puzzle_input)

    for nodes in antennas.values():
        antinodes.update(compute_antinodes_1(nodes, (n_rows, n_cols)))

    return len(antinodes)


def star_2(puzzle_input):
    """Solve second star."""
    antinodes = set()
    n_rows = len(puzzle_input)
    n_cols = len(puzzle_input[0].rstrip())
    antennas = load_antennas(puzzle_input)

    for nodes in antennas.values():
        antinodes.update(compute_antinodes_2(nodes, (n_rows, n_cols)))

    return len(antinodes)


def compute_antinodes_1(nodes, dims):
    """Compute the antinodes of a given frequency."""
    antinodes = set()

    for node_0, node_1 in itertools.permutations(nodes, 2):
        antinode = 2 * node_1 - node_0

        if 0 <= antinode.real < dims[0] and 0 <= antinode.imag < dims[1]:
            antinodes.add(antinode)

    return antinodes


def compute_antinodes_2(nodes, dims):
    """Compute the antinodes of a given frequency."""
    antinodes = set()

    for node_0, node_1 in itertools.permutations(nodes, 2):
        difference = node_1 - node_0
        difference = difference / math.gcd(
            int(difference.real), int(difference.imag)
        )

        antinode = node_1
        while 0 <= antinode.real < dims[0] and 0 <= antinode.imag < dims[1]:
            antinodes.add(antinode)
            antinode += difference

        antinode = node_1 - difference
        while 0 <= antinode.real < dims[0] and 0 <= antinode.imag < dims[1]:
            antinodes.add(antinode)
            antinode -= difference

    return antinodes


def load_antennas(puzzle_input):
    """Load antenna map from puzzle input."""
    antennas = defaultdict(list)

    for i, line in enumerate(puzzle_input):
        for j, location in enumerate(line.rstrip()):
            if location != ".":
                antennas[location].append(i + j * 1j)

    return dict(antennas)


if __name__ == "__main__":
    main()
