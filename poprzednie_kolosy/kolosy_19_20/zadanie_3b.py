def sol(T):
    n = len(T)
    wynik = False

    def rek(w, k, s):
        nonlocal wynik

        if w == n and s == 0:
            wynik = True
            return
        for kol_id in available_kols(k, n):
            rek(w +1, kol_id, s + T[w][k])
    # end def

    for i in range(n):
        rek(0, i, 0)

    return wynik
# end def


def available_kols(k, n):
    return [i for i in range(n) if i not in (k-1, k, k+1)]


