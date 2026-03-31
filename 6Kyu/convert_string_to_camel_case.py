# https://www.codewars.com/kata/517abf86da9663f1d2000003


def to_camel_case(text):
    words = text.replace("_", "-").split("-")
    return words[0] + "".join(w.capitalize() for w in words[1:] if w)
