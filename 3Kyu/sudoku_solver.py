# https://www.codewars.com/kata/5296bc77afba8baa690002d7


def subsquare(i, j):
    if 0 <= i < 3:
        if 0 <= j < 3:
            return 0
        if 3 <= j < 6:
            return 1
        if 6 <= j < 9:
            return 2
    if 3 <= i < 6:
        if 0 <= j < 3:
            return 3
        if 3 <= j < 6:
            return 4
        if 6 <= j < 9:
            return 5
    if 6 <= i < 9:
        if 0 <= j < 3:
            return 6
        if 3 <= j < 6:
            return 7
        if 6 <= j < 9:
            return 8


def sudoku(puzzle):
    r, c, s, zero_indexes = [], [], [], []
    puzzle_solved = [e[:] for e in puzzle]
    for _ in range(9):
        r.append(set(range(1, 10)))
        c.append(set(range(1, 10)))
        s.append(set(range(1, 10)))
    for i, row in enumerate(puzzle_solved):
        for j, e in enumerate(row):
            if e:
                r[i].remove(e)
                c[j].remove(e)
                s[subsquare(i, j)].remove(e)
            else:
                zero_indexes.append((i, j))
    while len(zero_indexes):
        for i, row in enumerate(puzzle_solved):
            for j, e in enumerate(row):
                if not e:
                    rcs = r[i] & c[j] & s[subsquare(i, j)]
                    if len(rcs) == 1:
                        new_e = rcs.pop()
                        r[i].remove(new_e)
                        c[j].remove(new_e)
                        s[subsquare(i, j)].remove(new_e)
                        zero_indexes.remove((i, j))
                        puzzle_solved[i][j] = new_e
    return puzzle_solved
