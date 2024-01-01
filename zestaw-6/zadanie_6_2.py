def waga(n):
    cnt = 0

    i = 2
    while n > 1:
        if n % i == 0:
            cnt += 1
        while n % i == 0:
            n //= i
        i += 1

    return cnt


def podzial(T):
    n = len(T)
    # tablica wag elementow z T
    T2 = [waga(T[i]) for i in range(n)]
    # Nie ma sensu liczyc bo nie da sie rozdzielic na 3 rowne zbiory
    if sum(T2) % 3 != 0:
        return False

    def rek(i, a, b, c):
        if i == n:
            return a == b == c

        return (rek(i + 1, a + T2[i], b, c) or
                rek(i + 1, a, b + T2[i], c) or
                rek(i + 1, a, b, c + T2[i]))

    return rek(0, 0, 0, 0)
