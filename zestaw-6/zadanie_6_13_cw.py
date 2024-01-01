# zadanie 13

def rek(num, result="", p=0):
    if num == 0:
        print(result[:-1])
    else:
        # num + 1 zeby doszlo do konca
        # p ustawiamy zeby rozklad byl w kolejnosci nierosnacej
        for i in range(p, num+1):
            rek(num - i, result + str(i) + "+", i)
        