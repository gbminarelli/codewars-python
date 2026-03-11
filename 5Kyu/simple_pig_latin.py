# https://www.codewars.com/kata/520b9d2ad5c005041100000f


def pig_word(word):
    return word[1:] + word[0] + "ay"


def pig_it(text):
    return " ".join(pig_word(word) if word.isalpha() else word for word in text.split())
