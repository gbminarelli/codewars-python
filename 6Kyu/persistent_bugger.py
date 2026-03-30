# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

import math


def persistence(n):
    m = n
    mp = 0
    while m // 10:
        m = math.prod((int(d) for d in str(m)))
        mp += 1
    return mp
