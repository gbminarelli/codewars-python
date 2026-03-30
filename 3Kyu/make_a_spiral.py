# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6


def spiralize(size):
    n = range(size)
    m = [[0 for _ in n] for _ in n]
    m[0] = [1 for _ in n]
    lines = [[], [], [], []]  # Spiral Path
    for a in n[:-1]:
        b = a % 4
        c = 2 * len(lines[b])
        lines[b].append(
            [0 if i < c else 1 if i < c + size - a // 2 * 2 else 0 for i in n]
        )
    for type, line in enumerate(lines):
        if type == 0:  # Vertical Top-Bottom
            for i, a in enumerate(line):
                j = -1 - (2 * i)
                for k, row in enumerate(m):
                    row[j] = a[k] if a[k] else row[j]
        elif type == 1:  # Horizontal Right-Left
            for i, a in enumerate(line):
                j = -1 - (2 * i)
                m[j] = [a[k] if a[k] else m[j][k] for k in n]
        elif type == 2:  # Vertical Bottom-Top
            for i, a in enumerate(line):
                j = 2 * i
                for k, row in enumerate(m[::-1]):
                    row[j] = a[k] if a[k] else row[j]
        elif type == 3:  # Horizontal Left-Right
            for i, a in enumerate(line):
                j = 2 * i + 2
                m[j] = [a[k] if a[k] else m[j][k] for k in n]
    return m
