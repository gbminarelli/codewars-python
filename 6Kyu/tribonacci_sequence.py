# https://www.codewars.com/kata/556deca17c58da83c00002db


def tribonacci(signature, n):
    s = signature[:n]
    for _ in range(n - 3):
        s.append(s[-1] + s[-2] + s[-3])
    return s
