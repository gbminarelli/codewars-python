# https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4

import math


def is_prime_in_gap(a):
    for b in range(3, math.isqrt(a) + 1, 2):
        if a % b == 0:
            return False
    return True


def next_prime_in_gap(a):
    b = a
    while not is_prime_in_gap(b):
        b += 2
    return b


def gap(g, m, n):
    a = next_prime_in_gap(m if m % 2 else m + 1)
    b = next_prime_in_gap(a + 2)
    while b <= n:
        if b - a == g:
            return [a, b]
        a = b
        b = next_prime_in_gap(b + 2)
