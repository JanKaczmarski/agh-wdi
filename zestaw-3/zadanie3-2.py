# zadanie 2

def cyfry(n):
    sol = ""
    n = str(n)
    
    for digit in n:
        if digit not in sol:
            sol += digit
    
    sol = list(sol)
    sol.sort()
    return sol

a = int(input())
b = int(input())

if cyfry(a) == cyfry(b):
    print("tak")
else:
    print("nie")
