# zadanie 1

# 1 1 2 3 5 8 13 21 34 55 89


def czy_iloczyn(n):
    # przez ile pomnozyc wyraz zeby dostac n
    # [n, n//2, n//3, n//5, n//8, n//13 ...]
    # 1 -> n
    # 2 -> n // 2
    # 3 -> n // 3
    # 5 -> n // 5
    
    dopelnienia = []

    a = 1
    b = 1

    while b <= n:
        if b in dopelnienia:
            return True
        dopelnienia.append(n/b)
        a, b = b, a+b
    return False


print(czy_iloczyn(13))