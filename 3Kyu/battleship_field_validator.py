# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7


def valid_corners(i, j, ones):
    return (
        (i + 1, j + 1) not in ones
        and (i + 1, j - 1) not in ones
        and (i - 1, j + 1) not in ones
        and (i - 1, j - 1) not in ones
    )


def valid_edges(i, j, ones):
    return not ((i, j + 1) in ones and (i + 1, j) in ones)


def validate_battlefield(field):
    ones_list = [(i, j) for i, a in enumerate(field) for j, b in enumerate(a) if b]
    if len(ones_list) != 20:
        return False
    ones = set(ones_list)
    ships = [0, 0, 0, 0]
    for i, j in ones_list:
        a = b = 0
        while (i + a, j + b) in ones:
            if not valid_corners(i + a, j + b, ones):
                return False
            if not valid_edges(i + a, j + b, ones):
                return False
            ones.remove((i + a, j + b))
            if (i + a + 1, j) in ones:
                a += 1
            else:
                b += 1
        n = a + b
        if n > 4:
            return False
        if n:
            ships[n - 1] += 1
            if ships[n - 1] + n > 5:
                return False
    return True
