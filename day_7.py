"""Day 7: Bridge Repair"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"


def main():
    """Solve day 7 stars."""
    with open("data/day_7.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first star."""
    equations = load_equations(puzzle_input)
    operations = (
        lambda operand_0, operand_1: operand_0 + operand_1,
        lambda operand_0, operand_1: operand_0 * operand_1,
    )

    total = sum(
        test_equation(test_value, operands, operations)
        for test_value, operands in equations
    )

    return total


def star_2(puzzle_input):
    """Solve second star."""
    equations = load_equations(puzzle_input)
    operations = (
        lambda operand_0, operand_1: operand_0 + operand_1,
        lambda operand_0, operand_1: operand_0 * operand_1,
        lambda operand_0, operand_1: int(f"{operand_0}{operand_1}"),
    )

    total = sum(
        test_equation(test_value, operands, operations)
        for test_value, operands in equations
    )

    return total


def load_equations(puzzle_input):
    """Load equations from puzzle input."""
    equations = []

    for line in puzzle_input:
        test_value, operands = line.split(": ")
        equations.append(
            (
                int(test_value),
                [int(operand) for operand in operands.split()],
            )
        )

    return equations


def test_equation(test_value, operands, operations):
    """Test if equation is possbile."""
    partials = []

    for operation in operations:
        partial = operation(operands[0], operands[1])
        if partial <= test_value:
            partials.append(partial)

    if len(operands) == 2:
        return test_value if test_value in partials else 0

    for partial in partials:
        if test_equation(test_value, [partial] + operands[2:], operations):
            return test_value

    return 0


if __name__ == "__main__":
    main()
