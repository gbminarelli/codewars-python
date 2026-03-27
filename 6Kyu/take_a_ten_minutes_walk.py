# https://www.codewars.com/kata/54da539698b8a2ad76000228

import collections


def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    d = collections.Counter(walk)
    return d["n"] == d["s"] and d["e"] == d["w"]
