
# 1 1 1 1
# 1 2 1 1
# 1 2 2 1
# 1 1 1 3

def sol(t):
    n = len(t)
    for i in range(n-2):
        for j in range(n-2):
            flag = True
            k = 1
            length = 1
            while flag and i + k < n:
                if t[i + k + 1] == t[i + k - 1][j]