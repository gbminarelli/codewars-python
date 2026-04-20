# https://www.codewars.com/kata/55aa075506463dac6600010d

import collections
import math


def prime_factors(n):
    m = n
    i = 3
    f = collections.defaultdict(int)
    while m % 2 == 0:
        f[2] += 1
        m //= 2
    while m >= i * i:
        if m % i:
            i += 2
        else:
            m //= i
            f[i] += 1
    if m > 1:
        f[m] += 1
    return f


def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n


def geometric_sum(a, r, n):
    return a * (r**n - 1) // (r - 1)


def sum_of_squared_divisors(n):
    return math.prod(geometric_sum(1, a**2, b + 1) for a, b in prime_factors(n).items())


def list_squared(m, n):
    return [
        [a, b]
        for a in range(m, n + 1)
        if is_perfect_square(b := sum_of_squared_divisors(a))
    ]
