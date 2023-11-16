from math import sqrt

N = int(input())
t = [True for _ in range(N)]

t[0] = False
t[1] = False

for i in range(sqrt(N) + 1):
    if t[i]:
        for k in range(i * i, N, i):
            t[k] = False

licznik = 0
for n in t:
    if n:
        licznik += 1
