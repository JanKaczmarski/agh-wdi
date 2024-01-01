"""
Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza czy jest możliwe
pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawałków też była
liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Na przykład: divide(2347)=True, podział na
23 i 47, natomiast divide(2255)=False.
"""
from math import log10, sqrt


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


def first_n_dig(num, i):
    length = 0
    p = num
    while p > 0:
        length += 1
        p //= 10

    return num // 10 ** (length - i)


def divide(N):
    # n: rozpatrywana liczba, i: gdzie tniemy, n_s: aktualna liczba cięć
    def rek(n, i, n_s):
        length = int(log10(n))
        if i == length:
            return is_prime(n_s + 1) and is_prime(n)

        return (rek(n, i + 1, n_s) or rek(n % (10 ** (i + 1)), 1, n_s + 1)) if is_prime(first_n_dig(n, i))\
            else rek(n, i + 1, n_s)

    return rek(N, 1, 0)


