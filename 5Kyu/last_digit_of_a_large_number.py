# https://www.codewars.com/kata/5511b2f550906349a70004e1


CYCLES = {
    0: (0,),
    1: (1,),
    2: (6, 2, 4, 8),
    3: (1, 3, 9, 7),
    4: (6, 4),
    5: (5,),
    6: (6,),
    7: (1, 7, 9, 3),
    8: (6, 8, 4, 2),
    9: (1, 9),
}


def last_digit(n1, n2):
    if n2 == 0:
        return 1
    a = CYCLES[n1 % 10]
    b = n2 % len(a)
    return a[b]
