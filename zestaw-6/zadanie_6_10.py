# zadanie 10 -> wyznacznik macierzy NxN

def wykresl(t, col):
    new = [t[i][:col] + t[i][col + 1:] for i in range(1, len(t))]
    return new


def sol(T):
    n = len(T)

    # t -> tablica, s -> skalar, z -> znak : -1 || 1
    def rek(t):
        length = len(t)
        wyznacznik = 0
        if len(t) == 2:
            return t[0][0] * t[1][1] - t[0][1] * t[1][0]

        for i in range(length):
            wyznacznik += t[0][i] * ((-1) ** i * rek(wykresl(t, i)))

        return wyznacznik

    return rek(T)


# 1 0 0
# 0 1 0
# 0 0 1

print(sol(  [ [1, -1, 2, 4], [0,1,0,3], [5,7,-2,0], [2,0,-1,4] ]  ))
