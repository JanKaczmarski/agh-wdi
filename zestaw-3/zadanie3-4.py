# zadanie 4

def factorial(n):
    if n == 0:
        return 1
    sol = 1
    for i in range(2, n + 1):
        sol *= i
    return sol


def euler(N):
    e = 0
    for i in range(N + 1):
        e += 1/factorial(i)
    return e


n = int(input())

print(euler(n))
