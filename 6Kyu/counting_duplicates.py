# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

import collections


def duplicate_count(text):
    return sum(1 for _, count in collections.Counter(text.lower()).items() if count > 1)
