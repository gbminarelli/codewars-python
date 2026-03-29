# https://www.codewars.com/kata/55983863da40caa2c900004e


def digits_to_int(d):
    a = 0
    for b in d:
        a = a * 10 + b
    return a


def next_bigger(n):
    d = [int(e) for e in str(n)]
    m = len(d)
    if m < 2:
        return -1
    i = m - 2
    while i >= 0:
        if d[i] < d[i + 1]:
            break
        i -= 1
        if i < 0:
            return -1
    j = m - 1
    while j > i:
        if d[j] > d[i]:
            return digits_to_int(
                d[:i] + [d[j]] + (d[i + 1 : j] + [d[i]] + d[j + 1 :])[::-1]
            )
        j -= 1
