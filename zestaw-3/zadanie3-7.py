# zadanie 7
from random import randint


def create_and_fill_arr(n, t):
    if t > 1000:
        return "T musi byc t < 1000"
    nums = [0 for _ in range(t)]

    i = 0
    while 0 in nums:
        drawed_num = randint(1, 1000)
        if drawed_num not in nums:
            nums[i] = drawed_num
            i += 1    
    
    return [nums[randint(0,t-1)] for _ in range(n)]

def all_digits_uneven(n):
    while n > 0:
        if (n % 10) % 2 == 0:
            return False
        n //= 10
    return True

def sol(N, t):
    for num in create_and_fill_arr(N, t):
        if all_digits_uneven(num):
            return True
    return False

print(sol(8, 20))