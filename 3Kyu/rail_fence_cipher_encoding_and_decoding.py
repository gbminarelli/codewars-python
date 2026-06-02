# https://www.codewars.com/kata/58c5577d61aefcf3ff000081


def encode_rail_fence_cipher(string, n):
    rails, k, i = tuple([] for _ in range(n)), 1, 0
    for c in string:
        rails[i].append(c)
        i += k
        if i == 0 or i == n - 1:
            k *= -1
    return "".join("".join(r) for r in rails)


def decode_rail_fence_cipher(string, n):
    rail_pattern, k, i = [], 1, 0
    for _ in string:
        rail_pattern.append(i)
        i += k
        if i == 0 or i == n - 1:
            k *= -1

    rail_counts = [0] * n
    for r in rail_pattern:
        rail_counts[r] += 1

    rails, j = [], 0
    for c in rail_counts:
        rails.append(list(string[j : j + c]))
        j += c

    rail_result, rail_index = [], [0] * n
    for r in rail_pattern:
        rail_result.append(rails[r][rail_index[r]])
        rail_index[r] += 1
    return "".join(rail_result)
