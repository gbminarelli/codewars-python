# https://www.codewars.com/kata/54da5a58ea159efa38000836

import collections


def find_it(seq):
    for a, b in collections.Counter(seq).items():
        if b % 2:
            return a
