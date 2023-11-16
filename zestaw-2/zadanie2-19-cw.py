# zadanie 19

# 1/2 -> 0.5
# 1/3 -> 0.(3)
# 1/4 -> 0.25
# 1/7 -> 0.(14725)

def il25(n):
    dwojki = 0
    piatki = 0
    while n % 2 == 0:
        dwojki += 1
        n //=2
    while n % 5 == 0:
        piatki += 1
        n //=5
    return max(dwojki, piatki)


def ulamek(l, m):
    print(l // m, end="")
    l %= m
    if l != 0:
        print(".", end="")
        # dzielenie pisemne dopoki nie dojdziemy do okresu
        for i in range(il25(m)):
            l *= 10
            print(l//m, end="")
            l %= m
        if l != 0:
            print("(", end="")
            reszta = l
            while True:
                l *= 10
                print(l//m, end="")
                l %= m
                if reszta == l:
                    break
            print(")")
                