"""Day 16: Reindeer Maze"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from collections import defaultdict
from functools import cache


def main():
    """Solve day 16 puzzles."""
    with open("data/day_16.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    start, end, walls = load_maze(puzzle_input)
    direction = 0 + 1j

    end_cost, _ = solve_maze(start, end, walls, direction)

    return end_cost


def star_2(puzzle_input):
    """Solve second puzzle."""
    start, end, walls = load_maze(puzzle_input)
    direction = 0 + 1j

    _, end_paths = solve_maze(start, end, walls, direction)

    tiles = set()

    for path in end_paths:
        for tile, _ in path:
            tiles.add(tile)

    n_tiles = len(tiles)

    return n_tiles


def load_maze(puzzle_input):
    """Load maze from puzzle input."""
    walls = []

    for i, line in enumerate(puzzle_input):
        for j, elem in enumerate(line):
            match elem:
                case "#":
                    walls.append(i + j * 1j)

                case "S":
                    start = i + j * 1j

                case "E":
                    end = i + j * 1j

    walls = tuple(walls)

    return start, end, walls


@cache
def solve_maze(start, end, walls, direction):
    """Solve maze."""
    maze = end, walls
    costs = defaultdict(lambda: float("inf"))

    costs[(start, direction)] = 0
    paths = {((start, direction),): 0}
    end_cost = float("inf")
    end_paths = []

    while paths:
        paths, costs, end_cost, end_paths = step(
            paths, costs, end_cost, end_paths, maze
        )

    return end_cost, end_paths


def step(paths, costs, end_cost, end_paths, maze):
    """Perform one step."""
    new_paths = {}

    for steps, cost in paths.items():
        position, direction = steps[-1]
        path_0 = tuple(list(steps) + [(position + direction, direction)])
        path_1 = tuple(list(steps) + [(position, direction * 1j)])
        path_2 = tuple(list(steps) + [(position, -direction * 1j)])

        if position + direction not in maze[1]:
            new_paths[path_0] = cost + 1

        new_paths[path_1] = cost + 1000
        new_paths[path_2] = cost + 1000

    paths = {}

    for path, cost in new_paths.items():
        if path[-1][0] == maze[0]:
            if cost < end_cost:
                end_cost = cost
                end_paths = [path]

            elif cost == end_cost:
                end_paths.append(path)

        elif cost <= costs[path[-1]] and cost < end_cost:
            costs[path[-1]] = cost
            paths[path] = cost

    return paths, costs, end_cost, end_paths


if __name__ == "__main__":
    main()
