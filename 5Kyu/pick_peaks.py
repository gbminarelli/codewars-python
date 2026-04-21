# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7


def pick_peaks(arr):
    p = {"pos": [], "peaks": []}
    n = len(arr)
    if n < 3:
        return p
    a = arr[0]
    p_index = None
    for i in range(1, n):
        b = arr[i]
        if a < b:
            p_index = i
        elif a > b and p_index is not None:
            p["pos"].append(p_index)
            p["peaks"].append(a)
            p_index = None
        a = b
    return p
