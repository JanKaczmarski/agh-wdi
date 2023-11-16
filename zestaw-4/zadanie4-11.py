
def czy_te_same_cyfry(a, b, c):
    cyfry = [0 for _ in range(10)]
    while a > 0:
        cyfry[a%10] = 1
        a //= 10
    # end
    while b > 0:
        if cyfry[b%10] == 0:
            return False
        else:
            cyfry[b%10] += 1
            b //= 10
        # end
    # end
    while c > 0:
        if cyfry[c%10] == 0 or cyfry[c%10] == 1:
            return False
        else:
            cyfry[c%10] += 1
            c //= 10
        # end
    # end
    for i in range(10):
        if cyfry[i] == 1 or cyfry[1] == 2:
            return False
        # end
    # end
    return True
# end 

# 45, 123, 21113, 1223, 54
# 45, 123, 21113, 1223, 54

def przyjaciele(T):
    n = len(T)
    sol = 0
    for row in range(n):
        for col in range(1,n-1):
            if czy_te_same_cyfry(T[row][col-1], T[row][col], T[row][col+1]):
                sol += 1
            # end
        # end
    # end
        if czy_te_same_cyfry(T[row][0], T[row][1], T[row][1]):
            sol += 1
        # end
        if czy_te_same_cyfry(T[row][-1], T[row][-2], T[row][-2]):
            sol += 1
    
    return sol
    

print(przyjaciele([[1223, 123, 21113],
                   [45, 65, 33],
                   [123, 123, 432]]))

#print(czy_te_same_cyfry(123, 22231, 23111))
