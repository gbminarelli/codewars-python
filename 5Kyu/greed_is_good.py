# https://www.codewars.com/kata/5270d0d18625160ada0000e4

import collections


def score(dice):
    return sum(
        b // 3 * (a * 100 if a != 1 else 1000)
        + b % 3 * (100 if a == 1 else 50 if a == 5 else 0)
        for a, b in collections.Counter(dice).items()
    )
