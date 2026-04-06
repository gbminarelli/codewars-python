# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c


def max_sequence(arr):
    a = b = 0
    for c in arr:
        b += c
        if b < 0:
            b = 0
        elif b > a:
            a = b
    return a
