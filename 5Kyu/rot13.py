# https://www.codewars.com/kata/530e15517bc88ac656000716


def rot13(message):
    return "".join(
        c
        if not c.isalpha()
        else chr(c13)
        if (c13 := ord(c) + 13) < (123 if c.islower() else 91)
        else chr(ord(c) - 13)
        for c in message
    )
