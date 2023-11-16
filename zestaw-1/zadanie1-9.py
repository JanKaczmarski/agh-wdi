# zadanie 9
# Napisac program wypisujacy podzielniki liczby

from math import sqrt


def divisors(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            print(i, n//i)
        i += 1

divisors(64)
