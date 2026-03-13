# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1


def snail(snail_map):
    snail_r, snail_list = snail_map, []
    while len(snail_r):
        snail_r, snail_list = (
            [list(row) for row in zip(*snail_r[1:])][::-1],
            snail_list + snail_r[0],
        )
    return snail_list
