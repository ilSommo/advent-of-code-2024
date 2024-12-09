"""Day 9: Disk Fragmenter"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from sortedcontainers import SortedDict


def main():
    """Solve day 9 stars."""
    with open("data/day_9.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first star."""
    files, free_space = load_disk_map(puzzle_input)

    for _ in range(len(files)):
        i, (size, value) = files.popitem()

        if min(free_space.keys()) >= i:
            files[i] = (size, value)
            break

        while size:
            j, free_size = free_space.popitem(0)

            if j >= i:
                free_space[j] = free_size
                files[i] = (size, value)
                break

            files[j] = (1, value)
            free_space[i] = 1
            size -= 1

            if free_size >= 2:
                free_space[j + 1] = free_size - 1

    memory = sum(int(digit) for digit in puzzle_input) * [0]

    for i, (size, value) in files.items():
        memory[i : i + size] = size * [value]

    checksum = sum(i * id_number for i, id_number in enumerate(memory))

    return checksum


def star_2(puzzle_input):
    """Solve second star."""
    files, free_space = load_disk_map(puzzle_input)
    new_files = SortedDict()

    for _ in range(len(files)):
        i, (size, value) = files.popitem()

        for j, free_size in free_space.items():
            if j >= i:
                break

            if free_size == size:
                free_space.pop(j)
                i = j
                break

            if free_size > size:
                free_space.pop(j)
                free_space[i] = size
                free_space[j + size] = free_size - size
                i = j
                break

        new_files[i] = (size, value)

    memory = sum(int(digit) for digit in puzzle_input) * [0]

    for i, (size, value) in new_files.items():
        memory[i : i + size] = size * [value]

    checksum = sum(i * id_number for i, id_number in enumerate(memory))

    return checksum


def load_disk_map(puzzle_input):
    """Load disk map from puzzle input."""
    files = SortedDict()
    free_space = SortedDict()
    j = 0
    value = 0

    for i, size in enumerate(puzzle_input):
        if int(size) > 0:
            if i % 2 == 0:
                files[j] = (int(size), value)
                value += 1

            else:
                free_space[j] = int(size)

        j += int(size)

    return files, free_space


if __name__ == "__main__":
    main()
