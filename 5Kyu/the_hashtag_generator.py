# https://www.codewars.com/kata/52449b062fb80683ec000024


def generate_hashtag(s):
    return (
        "#" + h
        if 0 < len(h := "".join(w.capitalize() for w in s.split() if w)) < 140
        else False
    )
