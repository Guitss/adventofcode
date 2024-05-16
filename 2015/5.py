"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

 - It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
 - It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or
aabbccdd (aa, bb, cc, or dd).
 - It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the
other requirements.

For example:

 - ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double
letter (...dd...), and none of the disallowed substrings.
 - aaa is nice because it has at least three vowels and a double letter, even though the
letters used by different rules overlap.
 - jchzalrnumimnmhp is naughty because it has no double letter.
 - haegwjzuvuyypxyu is naughty because it contains the string xy.
 - dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining
whether a string is naughty or nice. None of the old rules apply, as they are all
clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without
overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them,
like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that
repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with
one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single
letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo),
but no pair that appears twice.

How many strings are nice under these new rules?
"""
import re

from utils import load_input


INPUT = load_input(__file__)


VOWELS = "aeiou"
VOWELS_REGEX = re.compile(r'[aeiou]')

FORBIDDEN_MOTIFS = [
    "ab",
    "cd",
    "pq",
    "xy",
]


def solve_part1(input: str):

    nicies_count = 0

    for text in input.split():

        has_forbidden_motif = any([bad_motif in text for bad_motif in FORBIDDEN_MOTIFS])
        if has_forbidden_motif:
            continue

        no_vowels = re.sub(VOWELS_REGEX, '', text)
        if len(no_vowels) > len(text) - 3:
            continue

        sub_string_by_2 = [text[i:i+2] for i in range(len(text))][:-1]
        has_duplicates = any([len(set(dup)) == 1 for dup in sub_string_by_2])
        if not has_duplicates:
            continue

        nicies_count += 1

    return nicies_count


def solve_part2(input: str):

    nicies_count = 0

    for text in input.split():
        sub_string_by_2 = [text[i:i+2] for i in range(len(text))][:-1]
        duplicates = [sub for sub in sub_string_by_2 if text.count(sub) > 1]
        if not duplicates:
            continue

        sub_string_by_3 = [text[i:i+3] for i in range(len(text)) if len(text[i:i+3]) == 3]
        are_palindrom = [triplette == triplette[::-1] for triplette in sub_string_by_3]
        if not any(are_palindrom):
            continue

        nicies_count += 1

    return nicies_count


if __name__ == "__main__":

    # Checks
    checks = [
        ('ugknbfddgicrmopn', 1),
        ('aaa', 1),
        ('jchzalrnumimnmhp', 0),
        ('haegwjzuvuyypxyu', 0),
        ('dvszwmarrgswjxmb', 0),
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
        ('qjhvhtzxzqqjkmpb', 1),
        ('xxyxx', 1),
        ('uurcxstgmygtbstg', 0),
        ('ieodomkazucvgmuy', 0),
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
