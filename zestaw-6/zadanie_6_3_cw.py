
from random import randint
def create_sample_data(n):
    return [[randint(1,100) for _ in range(n)] for _ in range(n)]


def chess(T, k):
    N = len(T)



    def rek(p, w=0, suma=0):
        nonlocal min_suma
        """w: wiersz
           p: pole"""
        if w == N - 1:
            min_suma = min(suma, min_suma)
        else:
            if p + 1 < N:
                rek(p + 1, w+1, suma+T[w][p])
            if p-1 > -1:
                rek(p - 1, w+1, suma+T[w][p])
            rek(p, w+1, suma+T[w][p])
    min_suma = float('inf')
    rek(k)

    return min_suma + T[0][k]

sample_data = create_sample_data(8)

for line in sample_data:
    print(line)
print(chess(sample_data, 2))


def chess2():
    return None