# https://www.codewars.com/kata/55983863da40caa2c900004e


def digits_to_int(digits):
    result = 0
    for d in digits:
        result = result * 10 + d
    return result


def next_bigger(n):
    d = [int(m) for m in str(n)]
    dr = d[::-1]
    k = -1
    for i, a in enumerate(dr):
        if a < k:
            dri = dr[:i]
            for j, b in enumerate(dri):
                if b > a:
                    return digits_to_int(
                        d[: -i - 1] + [b] + dri[:j] + [a] + dri[j + 1 :]
                    )
            return digits_to_int(d[: -i - 1] + [b] + dri + [a])
        k = a
    return -1
