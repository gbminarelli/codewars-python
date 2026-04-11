# https://www.codewars.com/kata/54a91a4883a7de5d7800009c

import re


def increment_string(string):
    s, n = re.subn(
        r"[0-9]+$",
        lambda m: f"{int(n := m.group()) + 1:0{len(n)}d}",
        string,
    )
    return s if n else s + "1"
