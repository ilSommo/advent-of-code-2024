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
    fragmented_files = SortedDict()

    for i, (size, value) in files.items():
        for j in range(size):
            fragmented_files[i + j] = (1, value)

    files = compact_memory(fragmented_files, free_space)

    checksum = compute_checksum(files)

    return checksum


def star_2(puzzle_input):
    """Solve second star."""
    files, free_space = load_disk_map(puzzle_input)
    files = compact_memory(files, free_space)

    checksum = compute_checksum(files)

    return checksum


def compact_memory(files, free_space):
    """Compact files in memory."""
    new_files = SortedDict()

    for _ in range(len(files)):
        i, (size, value) = files.popitem()

        for j, free_size in free_space.items():
            if j >= i:
                break

            if free_size >= size:
                del free_space[j]

                if free_size > size:
                    free_space[i] = size
                    free_space[j + size] = free_size - size

                i = j
                break

        new_files[i] = (size, value)

    return new_files


def compute_checksum(files):
    """Compute checksum of files."""
    checksum = sum(
        int(size * value * (2 * i + size - 1) / 2)
        for i, (size, value) in files.items()
    )

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
