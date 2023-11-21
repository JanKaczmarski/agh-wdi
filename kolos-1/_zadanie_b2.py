from math import sqrt

def o_two_factors(n):
    b = 2
    cnt = 0
    while b <= sqrt(n):
        if n % b == 0 and cnt == 0:
            cnt += 2
            n //= b
        elif n%b == 0 and cnt != 0:
            return False
        b += 1
    return cnt == 2

def square(t):
    n = len(t)
    for i in range(n-1):
        for j in range(n-1):
            m = 1
            while i + m < n - 1 and j + m < n - 1:
                res = t[i][j] * t[i+m][j] * t[i+m][j + m] * t[i][j+m]
                if o_two_factors(res):
                    return m + 1
                m += 1
    return 0


print(square([[1,1,1],[2,1,1],[1,17,1]]))
