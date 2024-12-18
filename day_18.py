"""Day 18: RAM Run"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from collections import defaultdict, deque

DIMENSION = 70
DIRECTIONS = (1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j)


def main():
    """Solve day 18 puzzles."""
    with open("data/day_18.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    walls = load_bytes(puzzle_input)[:1024] + get_walls(DIMENSION)
    start = 0 + 0j
    goal = DIMENSION * (1 + 1j)

    return len(compute_path(start, goal, walls))


def star_2(puzzle_input):
    """Solve second puzzle."""
    walls = get_walls(DIMENSION)
    start = 0 + 0j
    goal = DIMENSION * (1 + 1j)

    bytes_ = load_bytes(puzzle_input)
    last_path = compute_path(start, goal, walls + bytes_[:1024])

    for i in range(1024, len(bytes_)):
        if bytes_[i] in last_path:
            path = compute_path(start, goal, walls + bytes_[: i + 1])

            if path:
                last_path = path

            else:
                return f"{int(bytes_[i].real)},{int(bytes_[i].imag)}"

    return None


def compute_path(start, goal, walls):
    """Compute path from start to goal."""
    costs = defaultdict(lambda: float("inf"))
    branches = deque()
    branches.append([start])

    while branches:
        path = branches.popleft()

        for direction in DIRECTIONS:
            position = path[-1] + direction

            if position == goal:
                return path

            if position not in walls and len(path) < costs[position]:
                branches.append(path + [position])
                costs[position] = len(path)

    return []


def get_walls(dimension):
    """Get walls of memory."""
    dimension += 1

    walls = tuple()
    walls += tuple(-1 + j * 1j for j in range(dimension))
    walls += tuple(i - 1j for i in range(dimension))
    walls += tuple(dimension + j * 1j for j in range(dimension))
    walls += tuple(i + dimension * 1j for i in range(dimension))

    return walls


def load_bytes(puzzle_input):
    """Load bytes from input."""
    bytes_ = []

    for line in puzzle_input:
        x, y = line.split(",")
        bytes_.append(int(x) + int(y) * 1j)

    return tuple(bytes_)


if __name__ == "__main__":
    main()
