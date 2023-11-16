# zadanie 3

def has_even_digit(n):
    while n > 0:
        if (n % 10) % 2 == 0:
            return True
        # end
        n //= 10
    # end
    return False
# end

def tab_has_even_digits(T):
    length = len(T)
    for row in range(length):
        sol = True
        for col in range(length):
            if has_even_digit(T[row][col]) is False:
                sol = False
                continue
        if sol:
            return True
    return False

