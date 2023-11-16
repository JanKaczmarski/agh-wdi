# Program wyznaczajacy NWD 3 zadanych liczb

a = int(input())
b = int(input())
c = int(input())


def nwd(a, b):
    while b != 0:
        pom = b
        b = a % b
        a = pom
    return a


print(nwd(nwd(a, b), c))
