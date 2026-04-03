# https://www.codewars.com/kata/54e6533c92449cc251001667


def unique_in_order(sequence):
    s = [None]
    for e in sequence:
        if e != s[-1]:
            s.append(e)
    return s[1:]
