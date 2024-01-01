# zadanie 13


def sol(n):
    suma = 0

    def rek(n, k):
        if k > n:
            return 0
        if k == 0 and n == 0:
            return 1
        if k == 0:
            return 0
        if n == k:
            return 0

        return rek(n-1, k-1) + k * rek(n-1, k)

    for k in range(2, n + 1):
        suma += rek(n, k)

    return suma


print(sol(4))
