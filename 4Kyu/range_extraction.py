# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f


def args_range_next(a, b):
    d = b - a
    if d > 1:
        return (f"{a}-{b}",)
    elif d:
        return (str(a), str(b))
    return (str(a),)


def solution(args):
    args_range = []
    a = b = args[0]
    for c in args[1:]:
        if c - b > 1:
            args_range.extend(args_range_next(a, b))
            a = c
        b = c
    args_range.extend(args_range_next(a, b))
    return ",".join(args_range)
