"""Day 17: Chronospatial Computer"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from collections import deque


def main():
    """Solve day 17 puzzles."""
    with open("data/day_17.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    a, b, c, instructions = load_program(puzzle_input)
    output = execute_program(a, b, c, instructions)

    return output


def star_2(puzzle_input):
    """Solve second puzzle."""
    _, b, c, instructions = load_program(puzzle_input)
    goal = puzzle_input[-1].split()[1]
    branches = deque()

    while True:
        factors = branches.popleft() if branches else []

        start = sum(8 ** (i + 1) * factors[i] for i in range(len(factors)))

        for a in range(start, start + 8):
            output = execute_program(a, b, c, instructions)

            if output == goal:
                return a

            if output == goal[-2 * len(factors) - 1 :]:
                branches.append([a % 8] + factors)


def execute_instruction(a, b, c, i, instructions):
    """Execute instruction."""
    instruction = instructions[i]
    i += 1
    output = []

    match instruction[1]:
        case 0 | 1 | 2 | 3:
            operand = instruction[1]

        case 4:
            operand = a

        case 5:
            operand = b

        case 6:
            operand = c

    match instruction[0]:
        case 0:
            a //= 2**operand

        case 1:
            b ^= instruction[1]

        case 2:
            b = operand % 8

        case 3:
            if a != 0:
                i = instruction[1] // 2

        case 4:
            b ^= c

        case 5:
            output = [str(operand % 8)]

        case 6:
            b = a // 2**operand

        case 7:
            c = a // 2**operand

    return a, b, c, i, output


def execute_program(a, b, c, instructions):
    """Execute program."""
    i = 0
    output = []

    while i < len(instructions):
        a, b, c, i, new_output = execute_instruction(a, b, c, i, instructions)
        output += new_output

    return ",".join(output)


def load_program(puzzle_input):
    """Load program from input."""
    a = int(puzzle_input[0].split()[-1])
    b = int(puzzle_input[1].split()[-1])
    c = int(puzzle_input[2].split()[-1])

    instructions_list = puzzle_input[4].split()[1].split(",")
    instructions = tuple(
        (int(instructions_list[i]), int(instructions_list[i + 1]))
        for i in range(0, len(instructions_list), 2)
    )

    return a, b, c, instructions


if __name__ == "__main__":
    main()
