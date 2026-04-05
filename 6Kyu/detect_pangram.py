# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string


def is_pangram(st):
    return set(string.ascii_lowercase).issubset(st.lower())
