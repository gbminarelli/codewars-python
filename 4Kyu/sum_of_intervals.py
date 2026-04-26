# https://www.codewars.com/kata/52b7ed099cdc285c300001cd


def sum_of_intervals(intervals):
    s = 0
    top = float("-inf")
    for a, b in sorted(intervals):
        if top < b:
            s += b - max(a, top)
            top = b
    return s
