# zadanie 6

from random import randint

UNEVEN_NUMS = [i for i in range(1,10,2)]

def create_array(n, t):
    nums = []
    while len(nums) < t:
        drawed_num = randint(1, 1000)
        if drawed_num not in nums:
            nums.append(drawed_num)
    return [nums[randint(0, t-1)] for _ in range(n)]

def has_uneven_digit(array):
    for n in array:
        none_uneven = True
        while n >= 1:
            digit = n % 10
            if digit in UNEVEN_NUMS:
                none_uneven = False
            n //= 10
        if none_uneven:
            return False, array
    return True, array
        
#n, t = int(input()), int(input())

n, t = 20, 20



print(has_uneven_digit(create_array(4, 20)))

