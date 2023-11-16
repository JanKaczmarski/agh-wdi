# zadanie 8
# Program sprawdzajacy czy zadana liczba jest pierwsza

from math import sqrt

# X X X X 5 X 7 X X X 11 X 13 X X X 17 X 19


def czy_pierwsza(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n == 1:
        return False

    i = 6
    while i <= sqrt(n):
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False

        i += 6

    return True

print(czy_pierwsza(37))
