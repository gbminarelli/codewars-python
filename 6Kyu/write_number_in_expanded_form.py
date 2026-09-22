# https://www.codewars.com/kata/5842df8ccbd22792a4000245


def expanded_form(num):
    digits = str(num)
    n = len(digits)
    return " + ".join(
        digit + "0" * (n - i - 1) for i, digit in enumerate(digits) if digit != "0"
    )
