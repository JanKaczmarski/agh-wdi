from math import sqrt


def is_prime(a):
    if a == 2 or a == 3: return True
    if a == 1 or a % 2 == 0 or a % 3 == 0: return False

    i = 6
    while i <= sqrt(a) + 1:
        if a % (i-1) == 0 or a % (i + 1) == 0:
            return False

        i += 6

    return True


def both_primes(a, b):
    # are both numbers prime
    return is_prime(a) and is_prime(b)


def sol():
    init_arr = [1] + [0 for _ in range(8)]

    def rek(arr, length=1):
        if length == 9:
            print(arr)
            return

        nums_left = [i for i in range(2,10) if i not in arr]

        for num in nums_left:
            if not both_primes(arr[length-1], num) and abs(num - arr[length-1]) >= 2:
                arr[length] = num
                rek(arr, length+1)

    rek(init_arr)


if __name__ == '__main__':
    sol()
