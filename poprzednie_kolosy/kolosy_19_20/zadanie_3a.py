
def poss_kolls(k, n):
    poss_tupple = (k-2, k-1, k, k+1, k+2)
    return [i for i in range(n) if i not in poss_tupple]

def sol(T):
    n = len(T)
    wynik = False


    def rek(w, k, s=0):
        nonlocal wynik
        if w == n and s == 0:
            wynik = True
            return

        for kol in poss_kolls(k, n):
            rek(w + 1, kol, s + T[w][k])

    for i in range(n):
        rek(0, i)

    return wynik
