"""Day 13: Claw Contraption"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from functools import cache


def main():
    """Solve day 13 puzzles."""
    with open("data/day_13.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    machines = load_machines(puzzle_input)

    total = sum(compute_cost(machine) for machine in machines)

    return total


def star_2(puzzle_input):
    """Solve second puzzle."""
    machines = load_machines(puzzle_input)

    machines = tuple(
        (a, b, prize + 10000000000000 * (1 + 1j)) for a, b, prize in machines
    )

    total = sum(compute_cost(machine) for machine in machines)

    return total


def compute_cost(machine):
    """Compute the cost of a machine."""
    a, b, p = machine

    i = int(
        (b.imag * p.real - b.real * p.imag)
        / (a.real * b.imag - a.imag * b.real)
    )
    j = int(
        (a.imag * p.real - a.real * p.imag)
        / (a.imag * b.real - a.real * b.imag)
    )

    if i * a + j * b == p:
        cost = 3 * i + j

        return cost

    return 0


@cache
def load_machines(puzzle_input):
    """Load machines from input."""
    machines = []

    for i, line in enumerate(puzzle_input):
        tokens = line.split()

        match i % 4:
            case 0:
                machines.append(
                    [int(tokens[2][2:-1]) + int(tokens[3][2:]) * 1j]
                )

            case 1:
                machines[-1].append(
                    int(tokens[2][2:-1]) + int(tokens[3][2:]) * 1j
                )

            case 2:
                machines[-1].append(
                    int(tokens[1][2:-1]) + int(tokens[2][2:]) * 1j
                )

    machines = tuple(tuple(machine) for machine in machines)

    return machines


if __name__ == "__main__":
    main()
