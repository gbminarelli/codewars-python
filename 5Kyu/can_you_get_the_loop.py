# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863


def loop_size(node):
    i = node._Node__id
    n = node.next
    while (j := n._Node__id) > i:
        i = j
        n = n.next
    return i - j + 1
