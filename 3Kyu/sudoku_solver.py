# https://www.codewars.com/kata/5296bc77afba8baa690002d7

def sudoku(puzzle):
    puzzle_solved = [e[:] for e in puzzle]
    r = [set(range(1, 10)) for _ in range(9)]
    c = [set(range(1, 10)) for _ in range(9)]
    s = [[set(range(1, 10)) for _ in range(3)] for _ in range(3)]
    # zeros = sum(1 for row in puzzle for e in row if not e)
    zeros = 0
    for i, row in enumerate(puzzle):
        for j, e in enumerate(row):
            if e:
                r[i].remove(e)
                c[j].remove(e)
                s[i // 3][j // 3].remove(e)
            else:
                zeros += 1
    while zeros:
        for i, row in enumerate(puzzle_solved):
            for j, e in enumerate(row):
                if not e:
                    rcs = r[i] & c[j] & s[i // 3][j // 3]
                    if len(rcs) == 1:
                        new_e = rcs.pop()
                        r[i].remove(new_e)
                        c[j].remove(new_e)
                        s[i // 3][j // 3].remove(new_e)
                        zeros -= 1
                        puzzle_solved[i][j] = new_e
    return puzzle_solved


puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

print(sudoku(puzzle))

# print(sum(1 for e in [[1, 2, 0, 3, 0, 3], [1, 2, 0]] for a in e if not a))
