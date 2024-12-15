"""Day 15: Warehouse Woes"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"


def main():
    """Solve day 15 puzzles."""
    with open("data/day_15.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    robot, boxes, walls, moves = parse_input(puzzle_input)

    for move in moves:
        robot, boxes = move_robot(robot, boxes, walls, move)

    total = int(sum(100 * box.real + box.imag for box in boxes))

    return total


def star_2(puzzle_input):
    """Solve second puzzle."""
    robot, boxes, walls, moves = parse_input(puzzle_input)

    robot = robot.real + robot.imag * 2j

    boxes = {box.real + box.imag * 2j for box in boxes}

    walls = tuple(wall.real + wall.imag * 2j for wall in walls)

    for move in moves:
        robot, boxes = move_robot_double(robot, boxes, walls, move)

    total = int(sum(100 * box.real + box.imag for box in boxes))

    return total


def move_robot(robot, boxes, walls, move):
    """Move robot."""
    new_robot = robot + move

    if new_robot in walls:
        return robot, boxes

    if new_robot in boxes:
        boxes.remove(new_robot)
        box, boxes = move_robot(new_robot, boxes, walls, move)
        boxes.add(box)

        if box != new_robot:
            return new_robot, boxes

        return robot, boxes

    return new_robot, boxes


def move_robot_double(robot, boxes, walls, move):
    """Move robot in double map."""
    boxes = boxes.copy()
    new_robot = robot + move
    new_robot_1 = new_robot - 1j

    if new_robot in walls or new_robot_1 in walls:
        return robot, boxes

    if new_robot in boxes or new_robot_1 in boxes:
        box_robot = new_robot if new_robot in boxes else new_robot_1
        boxes.remove(box_robot)

        box_0, boxes_0 = move_robot_double(box_robot, boxes, walls, move)
        box_1, boxes_1 = move_robot_double(box_robot + 1j, boxes, walls, move)
        box_1 -= 1j

        if box_0 == box_1 != box_robot:
            boxes = (boxes_0 | boxes_1) - boxes | boxes_0 & boxes_1
            boxes.add(box_0)
            return new_robot, boxes

        boxes.add(box_robot)
        return robot, boxes

    return new_robot, boxes


def parse_input(puzzle_input):
    """Parse puzzle input."""
    boxes = set()
    walls = set()
    i = 0

    while len(puzzle_input[i]) >= 1:
        line = puzzle_input[i]

        for j, position in enumerate(line):
            match position:
                case "#":
                    walls.add(i + j * 1j)

                case "O":
                    boxes.add(i + j * 1j)

                case "@":
                    robot = i + j * 1j

        i += 1

    moves = []

    for line in puzzle_input[i + 1 :]:
        for move in line:
            match move:
                case "^":
                    moves.append(-1 + 0j)

                case "v":
                    moves.append(1 + 0j)

                case "<":
                    moves.append(0 - 1j)

                case ">":
                    moves.append(0 + 1j)

    moves = tuple(moves)
    walls = tuple(walls)

    return robot, boxes, walls, moves


if __name__ == "__main__":
    main()
