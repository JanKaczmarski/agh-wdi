# zadanie 10
# napisac program wyszukujacy liczby doskonale mniejsze od miliona
from math import sqrt


def is_perfect(n):
    suma = 1
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            if i != n//i:
                suma += i + n//i
            else:
                suma += i

        i += 1
    return n - suma == 0


for n in range(10 ** 6):
    if is_perfect(n):
        print(n)
