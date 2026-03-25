# https://www.codewars.com/kata/51c8e37cee245da6b40000bd


def strip_comments(strng, markers):
    lines, m, s = strng.split("\n"), set(markers), []
    for line in lines:
        a = []
        for b in line:
            if b in m:
                break
            a.append(b)
        s.append("".join(a).rstrip())
    return "\n".join(s)
