# zadanie 6

def sol(T):
    n = len(T)

    def rek(T, suma_id, suma_val, i):
        if i == n:
            if suma_val == suma_id:
                return suma_val
            else:
                return 0

        return max(rek(T, suma_id + i, suma_val + T[i], i + 1),
                   rek(T, suma_id, suma_val, i + 1))

    return rek(T, 0, 0, 0)

print(sol([ 1,7,3,5,11,2 ]))



