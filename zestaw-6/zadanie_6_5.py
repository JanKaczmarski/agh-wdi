# zadanie 5
from math import sqrt


def list_to_bin(n_list):
    i = 0
    n = 0
    while i < len(n_list):
        n += n_list[i]*2**i
        i += 1
    return n


def bin_to_dec(n):
    solution = 0
    i = 0
    while n > 0:
        solution += (n % 2) * 2 ** i
        n //= 10
        i += 1

    return solution


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n == 1:
        return False

    i = 6
    while i <= sqrt(n) + 1:
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
        i += 6

    return True


def zadanie5(T):
    n = len(T)

    def rek(t, i):
        #if len(t) == 0:
        #    return True
        if i == len(t):
            return is_prime(bin_to_dec(list_to_bin(t)))
        if i == 30:
            return is_prime(bin_to_dec(list_to_bin(t[:i])))

        if is_prime(bin_to_dec(list_to_bin(t[:i]))):
            return rek(t[i:], 2)
        else:
            return rek(t, i + 1)


    return rek(T, 2)


print(zadanie5([1,1,1,0,1,1]))

