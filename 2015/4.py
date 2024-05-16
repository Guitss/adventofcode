"""
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for
 all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five
zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below)
followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest
positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043
 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash
 starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

 --- Part Two ---
Now find one that starts with six zeroes.
"""
import hashlib

from utils import load_input


INPUT = load_input(__file__)



def solve(input: str, mask='00000'):

    secret = '0'
    while True:
        hash_key = hashlib.md5(f'{input}{secret}'.encode()).hexdigest()

        if hash_key.startswith(mask):
            return secret
        else:
            secret = str(int(secret) + 1)


if __name__ == "__main__":

    # Checks
    checks = [
        ('abcdef', '609043'),
        ('pqrstuv', '1048970'),
    ]

    print('checks part 1')
    for input, expected in checks:

        result = solve(input, '00000')
        try:
            assert result == expected
        except AssertionError:
            print(f'X {input} {result} is not {expected}')
            raise
        else:
            print(f'V {input} {expected}')

    print('part 1:', solve(INPUT, '00000'))
    print('part 2:', solve(INPUT, '000000'))
