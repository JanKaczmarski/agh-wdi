# zadanie 3

from math import log10

# 123 -> 321  False
# 121 -> 121  True
# 2332 -> 2332 True
# Wniosek


def is_palindrome_int(n):
    # how many digits number has 
    n_len = int(log10(n)) + 1
    # number second part
    n_sp = 0
    # number first part
    n_fp = 0
    
    pom = n
    for i in range(n_len, (n_len-1)//2 , -1):
        indeks = n_len-i
        n_sp += (pom%10)*10**indeks
        pom //= 10
    
    pom = n
    for i in range(0, n_len//2):
        n_fp += (pom%10)*10**i
        pom //= 10
    return n_fp, n_sp




print(is_palindrome_int(101101))

# 101101
# 101101