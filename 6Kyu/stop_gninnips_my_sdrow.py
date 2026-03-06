# https://www.codewars.com/kata/5264d2b162488dc400000001

import re


def spin_words(sentence):
    return re.sub(r"([a-zA-Z]{5,})", lambda m: m.group(1)[::-1], sentence)
