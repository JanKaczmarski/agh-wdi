# zadanie 13

from math import sqrt

def is_prime(n):
    if n == 2 or n == 3: return True
    if n == 1 or n%2 == 0 or n%3 == 0: return False
    
    i = 6
    while i <= sqrt(n) + 1:
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def is_prime_v3(a):
    if a == 2 or a == 3:
        return True
    if a % 2 == 0 or a % 3 == 0 or a == 1:
        return False
    
    i = 6
    while i <= sqrt(a) + 1:
        if a % (i-1) == 0 or a % (i+1) == 0:
            return False
        i += 6

    return True

print(is_prime_v3(29))