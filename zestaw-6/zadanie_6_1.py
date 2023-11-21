# zadanie 1
from math import sqrt


def log10(n):
    cnt = 0
    while n > 0:
        n //= 10
        cnt += 1
    return cnt


def is_prime(n):
    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0 or n == 1:
        return False

    i = 6
    while i <= sqrt(n) + 1:
        if n % (i-1) == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def list_to_n(n_list):
    length = len(n_list)
    n = 0
    for i in range(length):
        n += n_list[-(i + 1)] * 10 ** i
    return n

def sol(n):
    # log(n) >= 3
    length = log10(n)
    n_list = [0 for _ in range(length)]
    for i in range(1, length+1):
        n_list[-i] = n % 10
        n //= 10


    def rek(n_list, i, flag):
        if i == length//2:
            return None

        if flag:
            n_list




print(sol(123))
