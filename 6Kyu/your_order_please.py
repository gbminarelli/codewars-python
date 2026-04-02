# https://www.codewars.com/kata/55c45be3b2079eccff00010f


def order(sentence):
    ss = sentence.split()
    so = ["" for _ in ss]
    for w in ss:
        for c in w:
            if c.isdigit():
                so[int(c) - 1] = w
                break
    return " ".join(so)
