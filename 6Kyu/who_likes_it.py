# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python


def likes(names):
    likes_count = len(names)
    if likes_count > 3:
        return f"{names[0]}, {names[1]} and {likes_count - 2} others like this"
    elif likes_count == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif likes_count == 2:
        return f"{names[0]} and {names[1]} like this"
    elif likes_count == 1:
        return f"{names[0]} likes this"
    else:
        return "no one likes this"
