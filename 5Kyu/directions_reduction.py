# https://www.codewars.com/kata/550f22f4d758534c1100025a


def dir_reduc(arr):
    a, b = [], {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    for dir in arr:
        if len(a) and a[-1] == b[dir]:
            a.pop()
        else:
            a.append(dir)
    return a
