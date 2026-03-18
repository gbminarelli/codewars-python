# https://www.codewars.com/kata/5526fc09a1bbd946250002dc


def find_outlier(n):
    a, b, c = n[0] % 2, n[1] % 2, n[2] % 2
    if a != b:
        if a != c:
            return n[0]
        return n[1]
    if a != c:
        return n[2]
    for m in n[3:]:
        if m % 2 != a:
            return m
