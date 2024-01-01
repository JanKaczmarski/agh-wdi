# zadanie 3
from random import randint
def create_sample_data(n):
    return [[randint(1,100) for _ in range(n)] for _ in range(n)]


def chess(T, k):
    N = len(T)

    def rek(T, w, p, suma):
        """w: wiersz
           p: pole"""
        if w == N - 1:
            return suma
        # BŁĄD nie rozpatruje wszystkich przypadkow
        # rozlaczne returny i min()
        if p + 1 < N and p - 1 > -1:
            return min(rek(T, w+1, p+1, suma + T[w+1][p+1]),
                       rek(T, w+1, p-1, suma + T[w+1][p-1]),
                       rek(T, w+1, p, suma + T[w+1][p]))
        elif p + 1 < N:
            return min(rek(T, w+1, p+1, suma + T[w+1][p+1]),
                       rek(T, w+1, p, suma + T[w+1][p]))
        elif p - 1 > -1:
            return min(rek(T, w+1, p-1, suma + T[w+1][p-1]),
                       rek(T, w+1, p, suma + T[w+1][p]))

    return rek(T, 0, k, 0)


sample_data = create_sample_data(8)

for line in sample_data:
    print(line)
print(chess(sample_data, 2))