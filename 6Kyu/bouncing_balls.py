# https://www.codewars.com/kata/5544c7a5cb454edb3c000047

from math import ceil, log


def bouncing_ball(h, bounce, window):
    return (
        1 + 2 * (ceil(log(window / h, bounce)) - 1)
        if h > 0 and 0 < bounce < 1 and window < h
        else -1
    )
