"""Day 24: Crossed Wires"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from collections import deque


def main():
    """Solve day 24 puzzles."""
    with open("data/day_24.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    wires, gates = load_input(puzzle_input)

    wires = apply_gates(wires, gates)

    z_binary = []

    for k, v in sorted(wires.items()):
        if k[0] == "z":
            z_binary.append(v)

    return sum(2**i * digit for i, digit in enumerate(z_binary))


def star_2(puzzle_input):
    """Solve second puzzle."""
    wires, gates = load_input(puzzle_input)
    bits = len(wires) // 2

    wrong_wires = set()

    for (input_0, operator, input_1), output in gates:
        if operator != "XOR" and output[0] == "z" and int(output[1:]) != bits:
            wrong_wires.add(output)

        elif (
            operator == "XOR"
            and input_0[0] not in ("x", "y", "z")
            and input_1[0] not in ("x", "y", "z")
            and output[0] not in ("x", "y", "z")
        ):
            wrong_wires.add(output)

        elif operator == "AND" and "x00" not in (input_0, input_1):
            for (input_0_, operator_, input_1_), _ in gates:
                if output in (input_0_, input_1_) and operator_ != "OR":
                    wrong_wires.add(output)

        elif operator == "XOR":
            for (input_0_, operator_, input_1_), _ in gates:
                if output in (input_0_, input_1_) and operator_ == "OR":
                    wrong_wires.add(output)

    return ",".join(sorted(wrong_wires))


def apply_gate(input_0, operator, input_1):
    """Apply gate to inputs."""
    match operator:
        case "AND":
            return input_0 & input_1

        case "OR":
            return input_0 | input_1

        case "XOR":
            return input_0 ^ input_1


def apply_gates(wires, gates):
    """Apply gates to wires."""
    gates = gates.copy()

    for _ in range(len(gates) ** 2):
        inputs, output = gates.popleft()

        try:
            wires[output] = apply_gate(
                wires[inputs[0]], inputs[1], wires[inputs[2]]
            )
        except KeyError:
            gates.append([inputs, output])

        if not gates:
            return wires

    return wires


def load_input(puzzle_input):
    """Load wires and gates."""
    lines = deque(puzzle_input)
    wires = {}

    line = lines.popleft()

    while line:
        wire, value = line.split(": ")
        wires[wire] = int(value)
        line = lines.popleft()

    gates = deque()

    for line in lines:
        inputs, output = line.split(" -> ")
        gates.append([tuple(inputs.split()), output])

    return wires, gates


if __name__ == "__main__":
    main()
