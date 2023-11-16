# iteracyjnie

from math import log2


def bin(n):
    t = [0 for _ in range(int(log2(n)) + 1)]

    i = -1

    while n > 0:
        t[i] = n%2
        n //= 2
        i -= 1
    # end while

    for i in t:
        print(i, end="")
    print()
# end def


n = 76
bin(n)

