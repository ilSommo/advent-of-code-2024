"""Day 12: Garden Groups"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools
from collections import defaultdict
from functools import cache


def main():
    """Solve day 12 puzzles."""
    with open("data/day_12.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    regions = load_regions(puzzle_input)

    total = sum(len(region) * compute_perimeter(region) for region in regions)

    return total


def star_2(puzzle_input):
    """Solve second puzzle."""
    regions = load_regions(puzzle_input)

    total = sum(len(region) * count_sides(region) for region in regions)

    return total


def compute_perimeter(region):
    """Compute the perimeter of a region."""
    perimeter = sum(
        4 - sum(neighbor in region for neighbor in get_neighbors(plant))
        for plant in region
    )

    return perimeter


def count_sides(region):
    """Count the number of sides of a region."""
    sides = 0

    for plant in region:
        neighbors = get_neighbors(plant)

        for i in range(4):
            neighbor_0 = neighbors[i]
            neighbor_1 = neighbors[(i + 1) % 4]

            if neighbor_0 not in region and neighbor_1 not in region:
                sides += 1

            if (
                neighbor_0 in region
                and neighbor_1 in region
                and neighbor_0 + neighbor_1 - plant not in region
            ):
                sides += 1

    return sides


@cache
def get_neighbors(position):
    """Get neighbors of a position."""
    neighbors = tuple(
        position + direction for direction in (1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j)
    )

    return neighbors


@cache
def load_regions(puzzle_input):
    """Load regions from puzzle input."""
    types = load_types(puzzle_input)

    regions = tuple(
        itertools.chain.from_iterable(
            [load_type_regions(plants) for plants in types]
        )
    )

    return regions


def load_type_regions(plants):
    """Load type regions."""
    type_regions = []

    while plants:
        plant = plants.pop()
        plant_regions = []

        for i, region in enumerate(type_regions):
            for plant_ in region:
                if abs(plant - plant_) == 1:
                    plant_regions.append(i)
                    break

        match len(plant_regions):
            case 0:
                type_regions.append([plant])

            case 1:
                type_regions[plant_regions[0]].append(plant)

            case _:
                i = plant_regions[0]
                type_regions[i].append(plant)

                for j in plant_regions[:0:-1]:
                    type_regions[i].extend(type_regions.pop(j))

    return type_regions


def load_types(garden):
    """Load types from garden."""
    types = defaultdict(list)

    for i, line in enumerate(garden):
        for j, plant in enumerate(line):
            types[plant].append(i + j * 1j)

    types_tuple = tuple(types.values())

    return types_tuple


if __name__ == "__main__":
    main()
