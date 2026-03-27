# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

import collections


def duplicate_encode(word):
    w = word.lower()
    c = collections.Counter(w)
    return "".join("(" if c[k] == 1 else ")" for k in w)
