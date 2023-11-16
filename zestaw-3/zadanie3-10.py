# zadanie 10

def sol(T):
    N = len(T)
    longest = 2
    i = 2
    current_len = 2
    current_diff = T[1] - T[0]
    while i < N:
        if T[i] - T[i - 1] == current_diff:
            current_len += 1
        else:
            longest = max(longest, current_len)
            current_len = 2
            current_diff = T[i] - T[i - 1]
        i += 1

    return max(longest, current_len)

print(sol([1,2,3,14,5,2,3]))

