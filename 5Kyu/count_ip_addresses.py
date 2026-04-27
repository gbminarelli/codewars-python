# https://www.codewars.com/kata/526989a41034285187000de4


def ipv4_to_int(ip):
    a = 0
    for b in ip.split("."):
        a = (a << 8) | int(b)
    return a


def ips_between(start, end):
    return ipv4_to_int(end) - ipv4_to_int(start)
