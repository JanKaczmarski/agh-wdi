

def singleton(T1, T2):
    # zakladam ze tablica T2 jest wyzerowana
    N = len(T1)
    M = len(T2)
    tab = [0 for _ in range(N)]
    k = 0
    indeks = znajdz_indeks(T1, tab)
    mem = T1[indeks][tab[indeks]]
    flaga = True
    for _ in range(M):
        indeks = znajdz_indeks(T1, tab)
        x = T1[indeks][tab[indeks]]
        if x == mem: flaga = False
        
        elif flaga:
            T2[k] = mem
            k += 1
        else: flaga = True
        mem = x    
    # end for
# end def
    
def znajdz_indeks(T1, tab):
    indeks = 0
    N = len(T1)
    for i in range(1, N):
        if tab[i] < len(T1):
            if T1[i][tab[i]] < T1[indeks][tab[indeks]]:
                index = i
    
"""
# szukanie indeksu minimalnego elementu
# t -> tablica 10 elementowa
ind = 0

for i in range(1,10)
    if t[i] < t[ind]:
        ind = i
        

"""
        



        
        