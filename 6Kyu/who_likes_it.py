# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/python


def likes(names):
    likes_count = len(names)
    if likes_count > 3:
        return f"{names[0]}, {names[1]} and {likes_count - 2} others like this"
    if likes_count == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    if likes_count == 2:
        return f"{names[0]} and {names[1]} like this"
    if likes_count == 1:
        return f"{names[0]} likes this"
    return "no one likes this"
