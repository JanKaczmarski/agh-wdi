# zadanie 7

def czy_iloczyn_sasiednich(n):
    a = 1
    b = 1

    while b < n:
        if a * b == n:
            return True
        a, b = b, a+b
        
    return False

