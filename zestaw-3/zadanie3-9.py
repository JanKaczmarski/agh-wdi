# zadanie 9

def sol(T):
    N = len(T)
    i = 1
    longest = 1
    current_len = 1
    while i < N:
        if T[i] - T[i-1] > 0:
            current_len += 1
        else:
            if current_len > longest:
                longest = current_len
            current_len = 1
        i += 1
        
    longest = max(current_len, longest)
    return longest

print(sol([1,2,3,4,2,3,5,6,7]))


