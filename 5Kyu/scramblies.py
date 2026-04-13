# https://www.codewars.com/kata/55c04b4cc56a697bb0000048

import collections


def scramble(s1, s2):
    return collections.Counter(s1) >= collections.Counter(s2)
