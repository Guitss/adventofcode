"""
--- Day 1: Not Quite Lisp ---
Santa was hoping for a white Christmas, but his weather machine's "snow" function is
powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty
stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each
day in the Advent calendar; the second puzzle is unlocked when you complete the first.
 Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the
right floor - the directions he got are a little confusing. He starts on the ground
floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ),
 means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find
the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?

--- Part Two ---
Now, given the same instructions, find the position of the first character that causes
him to enter the basement (floor -1). The first character in the instructions has
position 1, the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character that causes Santa to first enter the basement?
"""
from utils import load_input


INPUT = load_input(__file__)
print(INPUT)


def solve_part1(input: str) -> int:

    floor = 0

    for character in input:
        if character == '(':
            floor += 1
        elif character == ')':
            floor -= 1

    return floor


def solve_part2(input: str) -> int:

    floor = 0

    for c_index, character in enumerate(input):
        if character == '(':
            floor += 1
        elif character == ')':
            floor -= 1

        if floor == -1:
            return c_index + 1

    return -1


if __name__ == "__main__":

    # Checks
    checks = [
        ('(())', 0),
        ('()()', 0),

        ('(((', 3),
        ('(()(()(', 3),

        ('())', -1),
        ('))(', -1),

        (')))', -3),
        (')())())', -3),
    ]

    print('checks part 1')
    for input, expected in checks:

        result = solve_part1(input)
        try:
            assert result == expected
        except AssertionError:
            print(f'X {input} {result} is not {expected}')
        else:
            print(f'V {input} {expected}')

    print('part 1:', solve_part1(INPUT))

    # Checks
    checks = [
        (')', 1),
        ('()())', 5),
    ]

    print('checks part 2')
    for input, expected in checks:

        result = solve_part2(input)
        try:
            assert result == expected
        except AssertionError:
            print(f'X {input} {result} is not {expected}')
        else:
            print(f'V {input} {expected}')

    print('part 2:', solve_part2(INPUT))
