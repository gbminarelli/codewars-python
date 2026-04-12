# https://www.codewars.com/kata/55c6126177c9441a570000cc


def order_weight(strng):
    return " ".join(sorted(strng.split(), key=lambda a: (sum(int(b) for b in a), a)))
