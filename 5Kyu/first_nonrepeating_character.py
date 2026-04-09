# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

import collections


def first_non_repeating_letter(s):
    c = collections.Counter(s)
    for a, b in c.items():
        if b == 1 and (
            not a.isalpha()
            or (a.islower() and not c[a.upper()])
            or (a.isupper() and not c[a.lower()])
        ):
            return a
    return ""
