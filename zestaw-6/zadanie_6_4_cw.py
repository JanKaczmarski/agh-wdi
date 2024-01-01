# zadanie 4


# wypisz uzupelniania tablice
def wypisz(T):
    n = len(T)
    for row in range(n):
        for col in range(n):
            if col != n-1:
                print(T[row][col], end='\t')
            else:
                print(T[row][col])


# funkcje do uzupelnienia
def czy_skok(T, w, k, i):
    n = len(T)
    dx = (1, 2, 2, 1, -1, -2, -2, -1)
    dy = (-2, -1, 1, 2, 2, 1, -1, -2)

    w += dx[i]
    k += dy[i]

    if n > w >= 0 and 0 <= k < n and T[w][k] == 0:
        return w, k
    else:
        return False

def skok(T, w=0, k=0, ind=1):
    global flag
    n = len(T)
    T[w][k] = ind
    if ind == n ** 2:
        wypisz(T)
        exit()
    else:
        for i in range(8):
            if new_pos := czy_skok(T, w, k, i):
                skok(T, new_pos[0], new_pos[1], ind + 1)

    # jesli wykonaly sie i nie ma sukcesu to wstawiam 0 zamiast ind
    T[w][k] = 0

skok([[0 for _ in range(8)] for __ in range(8)])
