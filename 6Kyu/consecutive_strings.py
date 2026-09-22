# https://www.codewars.com/kata/56a5d994ac971f1ac500003e


def longest_consec(strarr, k):
    n = len(strarr)
    if not n or n < k or k <= 0:
        return ""
    sizes = tuple(len(word) for word in strarr)
    current = sum(sizes[:k])
    largest = current
    i = 0
    for j in range(1, n - k + 1):
        current += sizes[j + k - 1] - sizes[j - 1]
        if current > largest:
            largest = current
            i = j
    return "".join(strarr[i : i + k])
