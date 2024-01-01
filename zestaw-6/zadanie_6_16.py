# zadanie 16

"""
Zadanie 16. Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę sa-
mogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład′′ula′′ →117, 108, 97

oraz ′′exe′′ →101, 120, 101. Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe zbudowa-
nie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna wypisać
znaleziony wyraz.
"""

SAMOGLOSKI = ['a', 'e', 'i', 'o', 'u', 'y']


def samogloski_eq(s1, s2):
    suma_s1 = 0
    suma_s2 = 0
    for i in s1:
        if i in SAMOGLOSKI:
            suma_s1 += 1
    for i in s2:
        if i in SAMOGLOSKI:
            suma_s2 += 1

    return suma_s2 == suma_s1

def suma_ascii_eq(s1, s2):
    suma_s1 = 0
    suma_s2 = 0

    for i in s1:
        suma_s1 += ord(i)
    for i in s2:
        suma_s2 += ord(i)

    return suma_s2 == suma_s1


def prettify(s):
    return s

def wyraz(s1, s2):
    storage = ['' for _ in range(len(s2))]
    def rek(s_current, i):
        nonlocal storage
        if i == len(s2):
            if suma_ascii_eq(s1, s_current) and samogloski_eq(s1, s_current):
                storage.append(s_current)
        else:
            rek(s_current + s2[i], i + 1)
            rek(s_current, i + 1)

    rek('', 0)
    return prettify(storage)


print(wyraz('ula', 'exe'))

