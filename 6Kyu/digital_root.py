# https://www.codewars.com/kata/541c8630095125aba6000c00


def sum_of_digits(n):
    m, m_sum = n // 10, n % 10
    while m // 10 > 0:
        m_sum += m % 10
        m //= 10
    return m_sum + m


def digital_root(n):
    n_root = n
    while n_root // 10 > 0:
        n_root = sum_of_digits(n_root)
    return n_root
