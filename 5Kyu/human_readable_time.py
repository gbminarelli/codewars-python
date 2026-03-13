# https://www.codewars.com/kata/52685f7382004e774f0001f7


def make_readable(seconds):
    h, s = seconds // 3600, seconds % 3600
    m, s = s // 60, s % 60
    return f"{h:02d}:{m:02d}:{s:02d}"
