# https://www.codewars.com/kata/54d512e62a5e54c96200019e

import collections


def format_prime_factors(f):
    return "".join(f"({k}{f'**{v}' if v > 1 else ''})" for k, v in f.items())


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
    return format_prime_factors(f)
