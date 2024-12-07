"""Day 7: Bridge Repair"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools


def main():
    """Solve day 7 stars."""
    with open("data/day_7.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first star."""
    equations = load_equations(puzzle_input)

    total = sum(test_equation_1(equation) for equation in equations)

    return total


def star_2(puzzle_input):
    """Solve second star."""
    equations = load_equations(puzzle_input)

    total = sum(test_equation_2(equation) for equation in equations)

    return total


def load_equations(puzzle_input):
    """Load equations from puzzle input."""
    equations = []

    for line in puzzle_input:
        test_value, operands = line.split(": ")
        equations.append(
            (
                int(test_value),
                tuple(int(operand) for operand in operands.split()),
            )
        )

    return equations


def test_equation_1(equation):
    """Test if equation is possbile."""
    test_value, operands = equation

    for operators in itertools.product(["+", "*"], repeat=len(operands) - 1):
        total = operands[0]

        for i, operator in enumerate(operators):
            match operator:
                case "+":
                    total += operands[i + 1]

                case "*":
                    total *= operands[i + 1]

        if total == test_value:
            return total

    return 0


def test_equation_2(equation):
    """Test if equation is possbile."""
    test_value, operands = equation

    for operators in itertools.product(
        ["+", "*", "||"], repeat=len(operands) - 1
    ):
        total = operands[0]

        for i, operator in enumerate(operators):
            match operator:
                case "+":
                    total += operands[i + 1]

                case "*":
                    total *= operands[i + 1]

                case "||":
                    total = int(f"{total}{operands[i + 1]}")

        if total == test_value:
            return total

    return 0


if __name__ == "__main__":
    main()
