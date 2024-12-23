"""Day 22: Monkey Market"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from collections import defaultdict
from functools import cache


def main():
    """Solve day 22 puzzles."""
    with open("data/day_22.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    return sum(
        compute_next_number(int(line), 2000)[0] for line in puzzle_input
    )


def star_2(puzzle_input):
    """Solve second puzzle."""
    totals = defaultdict(int)

    for line in puzzle_input:
        _, prices, changes = compute_next_number(int(line), 2000)
        sequences = set()

        for i, price in enumerate(prices[4:]):
            sequence = tuple(changes[i : i + 4])

            if sequence not in sequences:
                totals[sequence] += price
                sequences.add(sequence)

    return max(totals.values())


@cache
def compute_next_number(number, steps):
    """Compute next number."""
    old_price = number % 10
    prices = [old_price]
    changes = []

    for _ in range(steps):
        number = ((number * 64) ^ number) % 16777216
        number = (int(number / 32) ^ number) % 16777216
        number = ((number * 2048) ^ number) % 16777216

        price = number % 10
        prices.append(price)
        changes.append(price - old_price)
        old_price = price

    return number, prices, changes


if __name__ == "__main__":
    main()
