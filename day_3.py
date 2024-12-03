"""Day 3: Mull It Over"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import re


def main():
    with open("data/day_3.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read()

    star_1(puzzle_input)
    star_2(puzzle_input)


def star_1(puzzle_input):
    pairs = get_pairs(puzzle_input)
    total = compute_total(pairs)

    print(total)


def star_2(puzzle_input):
    pairs = get_pairs_2(puzzle_input)
    total = compute_total(pairs)

    print(total)


def get_pairs(string):
    raw_pairs = re.findall(r"(?<=mul\()[0-9]{1,3},[0-9]{1,3}(?=\))", string)
    pairs = []

    for raw_pair in raw_pairs:
        raw_numbers = raw_pair.split(",")
        pairs.append((int(raw_numbers[0]), int(raw_numbers[1])))

    return pairs


def compute_total(pairs):
    total = sum([pair[0] * pair[1] for pair in pairs])

    return total


def get_pairs_2(string):
    raw_pairs = re.findall(
        r"do\(\)|don't\(\)|(?<=mul\()[0-9]{1,3},[0-9]{1,3}(?=\))", string
    )
    pairs = []
    enabled = True

    for raw_pair in raw_pairs:
        match raw_pair:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _:
                if enabled:
                    raw_numbers = raw_pair.split(",")
                    pairs.append((int(raw_numbers[0]), int(raw_numbers[1])))

    return pairs


if __name__ == "__main__":
    main()
