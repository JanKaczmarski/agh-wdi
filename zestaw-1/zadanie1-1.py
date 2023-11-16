# zadanie 1

def fib_until(n):
    """Fib seq number smaller than n:int"""
    a = 1
    b = 1
    
    while a < n:
        print(a)
        a, b = b, a + b

fib_until(10**6)