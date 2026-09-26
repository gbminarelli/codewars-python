# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029


def wave(people):
    chars = list(people)
    result = []
    for i, char in enumerate(people):
        if not char.isspace():
            chars[i] = char.upper()
            result.append("".join(chars))
            chars[i] = char
    return result
