# https://www.codewars.com/kata/514b92a657cdc65150000006


def solution(number):
    return sum(e for e in range(number) if e % 3 == 0 or e % 5 == 0)
