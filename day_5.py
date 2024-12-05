"""Day 5: Print Queue"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from collections import defaultdict


def main():
    with open("data/day_5.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    rules, updates = parse_input(puzzle_input)
    total = 0

    for update in updates:
        total += check_update(update, rules)

    return total


def star_2(puzzle_input):
    rules, updates = parse_input(puzzle_input)
    total = 0

    for update in updates:
        total += check_update_2(update, rules)

    return total


def parse_input(puzzle_input):
    rules = defaultdict(list)
    updates = []

    for line in puzzle_input:
        if "|" in line:
            v, k = line.split("|")
            rules[int(k)].append(int(v))

        elif "," in line:
            updates.append([int(page) for page in line.split(",")])

    return rules, updates


def check_update(update, rules):
    forbidden = set()

    for page in update:
        if page in forbidden:
            return 0

        else:
            forbidden.update(set(rules[page]))

    return update[len(update) // 2]


def check_update_2(update, rules):
    forbidden = set()

    for page in update:
        if page in forbidden:
            ordered_update = reorder_update(update, rules)

            return ordered_update[len(update) // 2]

        else:
            forbidden.update(set(rules[page]))

    return 0


def reorder_update(update, rules):
    forbidden = {}

    for page in update:
        forbidden[page] = set(rules[page]) & set(update)

    ordered_update = []

    for k in sorted(forbidden, key=lambda k: len(forbidden[k])):
        ordered_update.append(k)

    return ordered_update


if __name__ == "__main__":
    main()
