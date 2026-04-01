# https://www.codewars.com/kata/5287e858c6b5a9678200083c


def narcissistic(value):
    n = len(s := str(value))
    return sum(int(d) ** n for d in s) == value
