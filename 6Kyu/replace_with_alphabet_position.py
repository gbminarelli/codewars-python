# https://www.codewars.com/kata/546f922b54af40e1e90001da


def alphabet_position(text):
    return " ".join(str(b - 96) for a in text.lower() if 96 < (b := ord(a)) < 123)
