"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""
from utils import load_input


INPUT = load_input(__file__)


def update_location(start: tuple[int, int], move: str) -> tuple[int, int]:

    if move == '>':
        return start[0]+1, start[1]
    elif move == '<':
        return start[0]-1, start[1]
    elif move == '^':
        return start[0], start[1]+1
    elif move == 'v':
        return start[0], start[1]-1



def solve_part1(input: str) -> int:

    current_location = (0,0)
    house_listing = {current_location}

    for direction in input:

        next_house = update_location(start=current_location, move=direction)
        house_listing.add(next_house)

        current_location = next_house

    return len(house_listing)


def solve_part2(input: str) -> int:

    start_location = (0,0)
    house_listing = {start_location}

    # Santa and robo-santa had their own moving plan
    santa_road = input[::2]
    robo_santa_road = input[1::2]

    # They each move from houses to house
    for journey in [santa_road, robo_santa_road]:

        # Begin at start_location
        current_location = start_location

        # and going their own plan
        for direction in journey:

            next_house = update_location(start=current_location, move=direction)
            house_listing.add(next_house)

            current_location = next_house

    return len(house_listing)


if __name__ == "__main__":

    # Checks
    checks = [
        ('>', 2),
        ('^>v<', 4),
        ('^v^v^v^v^v', 2),
    ]

    print('checks part 1')
    for input, expected in checks:

        result = solve_part1(input)
        try:
            assert result == expected
        except AssertionError:
            print(f'X {input} {result} is not {expected}')
            raise
        else:
            print(f'V {input} {expected}')

    print('part 1:', solve_part1(INPUT))

    # Checks
    checks = [
        ('^v', 3),
        ('^>v<', 3),
        ('^v^v^v^v^v', 11),
    ]

    print('checks part 2')
    for input, expected in checks:

        result = solve_part2(input)
        try:
            assert result == expected
        except AssertionError:
            print(f'X {input} {result} is not {expected}')
            raise
        else:
            print(f'V {input} {expected}')

    print('part 2:', solve_part2(INPUT))
