# zadanie 7

odwazniki = [1, 3, 5, 7, 13, 20]

def waga(T, p):
    n = len(T)

    def rek(T, i, suma):
        if n == i:
            return suma == p

        return rek(T, i + 1, suma + T[i]) or rek(T, i + 1, suma)

    return rek(T, 0, 0)

print(waga([1,3,5,7,13,17,21], 2))



