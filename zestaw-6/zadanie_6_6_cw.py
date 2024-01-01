
def sol(T):
    n = len(T)
    g_l = n
    g_sum = 0
    def rek(suma_id=0, suma_val=0, i=0, l=0):
        nonlocal g_l, g_sum
        if i == n:
            if suma_val == suma_id:
                if l < g_l:
                    g_l = l
                    g_sum = suma_id
        rek(suma_id + i, suma_val + T[i], i + 1, l + 1)
        rek(suma_id, suma_val, i + 1, l)

    return g_sum

print(sol([ 1,7,3,5,11,2 ]))

