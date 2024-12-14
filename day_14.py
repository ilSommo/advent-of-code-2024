"""Day 14: Restroom Redoubt"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from functools import cache
import math

HEIGHT = 103
WIDTH = 101


def main():
    """Solve day 14 puzzles."""
    with open("data/day_14.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    robots = get_robots(puzzle_input)

    robots = move_robots(robots, 100)

    quadrants = count_quadrants(robots)
    total = math.prod(quadrants)

    return total


def star_2(puzzle_input):
    """Solve second puzzle."""
    robots = get_robots(puzzle_input)
    previous_positions = []
    position = tuple(robot[0] for robot in robots)
    step = 0

    while position not in previous_positions:
        previous_positions.append(position)
        counter = 0

        for robot in position:
            if (
                sum(neighbor in position for neighbor in get_neighbors(robot))
                == 4
            ):
                counter += 1
                if counter >= 100:
                    return step

        robots = move_robots(robots, 1)
        position = tuple(robot[0] for robot in robots)
        step += 1

    return 0


def count_quadrants(robots):
    """Count robots in each quadrant."""
    quadrants = [0, 0, 0, 0]

    for p, _ in robots:
        i, j = p.real, p.imag

        if i < WIDTH // 2 and j < HEIGHT // 2:
            quadrants[0] += 1

        elif i > WIDTH // 2 and j < HEIGHT // 2:
            quadrants[1] += 1

        elif i < WIDTH // 2 and j > HEIGHT // 2:
            quadrants[2] += 1

        elif i > WIDTH // 2 and j > HEIGHT // 2:
            quadrants[3] += 1

    return quadrants


@cache
def get_neighbors(position):
    """Get neighbors of a position."""
    neighbors = tuple(
        position + direction for direction in (1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j)
    )

    return neighbors


@cache
def get_robots(puzzle_input):
    """Get robots from input."""
    robots = []

    for line in puzzle_input:
        p, v = line.split()
        p = p[2:].split(",")
        v = v[2:].split(",")
        p = int(p[0]) + int(p[1]) * 1j
        v = int(v[0]) + int(v[1]) * 1j
        robots.append((p, v))

    return robots


def move_robots(robots, steps):
    """Move robots for a number of steps."""
    robots = [(p + steps * v, v) for p, v in robots]
    robots = [(p.real % WIDTH + p.imag % HEIGHT * 1j, v) for p, v in robots]
    return robots


if __name__ == "__main__":
    main()
