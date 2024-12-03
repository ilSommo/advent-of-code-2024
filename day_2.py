"""Day 2: Red-Nosed Reports"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"


def main():
    with open("data/day_2.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    star_1(puzzle_input)
    star_2(puzzle_input)


def star_1(puzzle_input):
    safe_reports = 0

    for line in puzzle_input:
        report = line.split()
        safe_reports += check_safety_1(report)

    print(safe_reports)


def star_2(puzzle_input):
    safe_reports = 0

    for line in puzzle_input:
        report = line.split()
        safe_reports += check_safety_2(report)

    print(safe_reports)


def check_safety_1(report):
    last_difference = 0

    for i, _ in enumerate(report[:-1]):
        difference = int(report[i + 1]) - int(report[i])

        if not (
            difference * last_difference >= 0 and 1 <= abs(difference) <= 3
        ):
            return 0

        last_difference = difference

    return 1


def check_safety_2(report):
    last_difference = 0

    for i, _ in enumerate(report[:-1]):
        difference = int(report[i + 1]) - int(report[i])

        if not (
            difference * last_difference >= 0 and 1 <= abs(difference) <= 3
        ):
            for j in range(i - 1, i + 2):
                report_copy = report.copy()
                report_copy.pop(j)

                if check_safety_1(report_copy):
                    return 1

            return 0

        last_difference = difference

    return 1


if __name__ == "__main__":
    main()
