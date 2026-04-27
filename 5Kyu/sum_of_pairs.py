# https://www.codewars.com/kata/54d81488b981293527000c8f


def sum_pairs(ints, s):
    p = set()
    for a in ints:
        if s - a in p:
            return [s - a, a]
        p.add(a)
