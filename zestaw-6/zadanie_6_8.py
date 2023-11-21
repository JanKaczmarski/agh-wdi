# zadanie 8

def sol(T, target):
    n = len(T)

    def rek(i, suma, odwazniki):
        if i == n:
            if suma == target:
                print(odwazniki)
            return suma == target

        return (rek(i + 1, suma, odwazniki) or
                rek(i + 1, suma + T[i], odwazniki + [T[i]]) or
                rek(i + 1, suma - T[i], odwazniki + [-T[i]]))

    return rek(0, 0, [])

print(sol([1,3], 2))