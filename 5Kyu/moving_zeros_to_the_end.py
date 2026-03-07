# https://www.codewars.com/kata/52597aa56021e91c93000cb0


def move_zeros(lst):
    return [a for a in lst if a] + [0] * lst.count(0)
