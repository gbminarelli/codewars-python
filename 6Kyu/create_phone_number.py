# https://www.codewars.com/kata/525f50e3b73515a6db000b83


def list_to_string(m):
    return "".join(str(e) for e in m)


def create_phone_number(n):
    return f"({list_to_string(n[:3])}) {list_to_string(n[3:6])}-{list_to_string(n[6:])}"
