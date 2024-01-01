from math import sqrt

# Program nie dziala Program nie dziala Program nie dziala Program nie dziala
# Program nie dziala Program nie dziala Program nie dziala Program nie dziala
# Program nie dziala Program nie dziala Program nie dziala Program nie dziala

def nww(a, b):
    c = min(a, b)

    for i in range(2, int(sqrt(c)) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


def sol_nww(t):
    if nww(t[0], t[1])and nww(t[0], t[2])and nww(t[1], t[2]):
        return True


def trojki(T):
    n = len(T)
    cnt = 0

    def rek(t, current, i=0, can_pause=True):
        """
        t: trojka,
        current: ile elementow w trojce
        """
        nonlocal cnt
        print(current)
        if current == 3:
            if sol_nww(t):
                cnt += 1
            t = [0, 0, 0]

        elif i == n:
            return

        else:
            if can_pause:
                rek(t, current, i + 1, False)
            t[current] = T[i]
            rek(t, current + 1, i + 1, True)

    rek([0,0,0], 0 )

    return cnt

print(trojki([2,4,6,7,8,10,12]))

