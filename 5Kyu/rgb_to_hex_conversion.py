# https://www.codewars.com/kata/513e08acc600c94f01000001


def rgb_clamp(n):
    return 0 if n < 0 else 255 if n > 255 else n


def rgb(r, g, b):
    return f"{rgb_clamp(r):02X}{rgb_clamp(g):02X}{rgb_clamp(b):02X}"
