def has_only_uneven_digits(n):
    while n > 0:
        if (n%10)%2 == 0:
            return False
        # end
        n //= 10
    # end
    return True
# end
def uneven_in_tab(T):
    length = len(T)
    for row in range(length):
        has_uneven = False
        for col in range(length):
            if has_only_uneven_digits(T[row][col]):
                has_uneven = True
                continue
            # end
        if has_uneven is False:
            return False
        # end
    # end
    return True
# end


print(uneven_in_tab([[1, 1, 1],[2, 2, 2],[1, 1, 1]]))

