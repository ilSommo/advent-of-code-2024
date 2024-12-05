"""Day 1: Historian Hysteria"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"


def main():
    """Solve day 1 stars."""
    with open("data/day_1.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first star."""
    list_0, list_1 = create_lists(puzzle_input)

    list_0.sort()
    list_1.sort()

    total_distance = compute_sum(list_0, list_1)

    return total_distance


def star_2(puzzle_input):
    """Solve second star."""
    list_0, list_1 = create_lists(puzzle_input)

    total_distance = compute_similarity(list_0, list_1)

    return total_distance


def create_lists(lines):
    """Create lists from input."""
    list_0 = []
    list_1 = []

    for line in lines:
        numbers = line.split()
        list_0.append(int(numbers[0]))
        list_1.append(int(numbers[1]))

    return list_0, list_1


def compute_sum(list_0, list_1):
    """Compute total distance."""
    total = 0

    for number_0, number_1 in zip(list_0, list_1):
        total += abs(number_1 - number_0)

    return total


def compute_similarity(list_0, list_1):
    """Compute similarity."""
    total = 0

    for number_0 in list_0:
        total += number_0 * list_1.count(number_0)

    return total


if __name__ == "__main__":
    main()
