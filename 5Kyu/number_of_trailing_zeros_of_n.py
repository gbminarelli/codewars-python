# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34


def zeros(n):
    m = n
    s = 0
    while m := m // 5:
        s += m
    return s
