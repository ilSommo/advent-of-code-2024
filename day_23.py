"""Day 23: LAN Party"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools
from collections import defaultdict


def main():
    """Solve day 23 puzzles."""
    with open("data/day_23.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    computers = load_computers(puzzle_input)
    sets_of_three = set()

    for computer_0, connected in sorted(computers.items()):
        for computer_1, computer_2 in itertools.combinations(
            sorted(connected), 2
        ):
            if computer_2 in computers[computer_1] and (
                computer_0[0] == "t"
                or computer_1[0] == "t"
                or computer_2[0] == "t"
            ):
                sets_of_three.add(
                    tuple(sorted((computer_0, computer_1, computer_2)))
                )

    return len(sets_of_three)


def star_2(puzzle_input):
    """Solve second puzzle."""
    computers = load_computers(puzzle_input)

    cliques = sorted(
        list(get_cliques(set(), set(computers.keys()), set(), computers)),
        key=len,
    )

    return ",".join(sorted(cliques[-1]))


def get_cliques(r, p, x, graph):
    """Get all cliques."""
    if not p and not x:
        yield r

    while p:
        v = p.pop()
        yield from get_cliques(r | {v}, p & graph[v], x & graph[v], graph)
        x.add(v)


def load_computers(puzzle_input):
    """Load computers from input."""
    computers = defaultdict(set)

    for line in puzzle_input:
        computer_0, computer_1 = sorted(line.split("-"))
        computers[computer_0].add(computer_1)
        computers[computer_1].add(computer_0)

    return computers


if __name__ == "__main__":
    main()
