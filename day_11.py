"""Day 11: Plutonian Pebbles"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from collections import defaultdict
from functools import cache


def main():
    """Solve day 11 puzzles."""
    with open("data/day_11.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    stones = load_stones(puzzle_input)

    for _ in range(25):
        stones = blink(stones)

    n_stones = sum(stones.values())

    return n_stones


def star_2(puzzle_input):
    """Solve second puzzle."""
    stones = load_stones(puzzle_input)

    for _ in range(75):
        stones = blink(stones)

    n_stones = sum(stones.values())

    return n_stones


def blink(stones):
    """Process stones after one blink."""
    new_stones = defaultdict(int)

    for k, v in stones.items():
        for new_stone in process_stone(k):
            new_stones[new_stone] += v

    return new_stones


def load_stones(puzzle_input):
    """Load list of stone from puzzle input."""
    stones = defaultdict(int)

    for stone in puzzle_input.split():
        stones[stone.strip("0")] += 1

    return stones


@cache
def process_stone(stone):
    """Apply rules to stone."""
    if stone == "":
        return ("1",)

    if len(stone) % 2 == 0:
        digits = (
            stone[: len(stone) // 2],
            stone[len(stone) // 2 :].lstrip("0"),
        )

        return digits

    return (str(2024 * int(stone)),)


if __name__ == "__main__":
    main()
