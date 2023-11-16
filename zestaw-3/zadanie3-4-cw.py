# zadanie 4

"""
def e():
    suma = 0
    skladnik = 1
    licznik = 0
    while skladnik > 0:
        licznik += 1
        suma += skladnik
        skladnik /= licznik
    return suma

print(e())
"""

n = int(input())
suma = [0 for _ in range(n + 1)]
skladnik = [0 for _ in range(n+1)]
skladnik[0] = 1

# Dokonczyc 
licznik = 0
while licznik < 1000:
    licznik += 1
    # dodawanie pisemne
    p = 0
    for k in range(n,-1,-1):
        tmp = suma[k] + skladnik[k] + p
        suma[k] = tmp%10
        p = tmp//10

print(suma)