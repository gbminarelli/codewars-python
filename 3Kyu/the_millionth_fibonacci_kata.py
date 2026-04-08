# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26


def fast_doubling(n):
    if n == 0:
        return (0, 1)
    a, b = fast_doubling(n // 2)
    c = a * (2 * b - a)
    d = a * a + b * b
    if n % 2:
        return (d, c + d)
    return (c, d)


def fib(n):
    return fast_doubling(abs(n))[0] * (1 if n > 0 or n % 2 else -1)
