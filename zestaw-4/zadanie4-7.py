# zadanie 7

def linearize_ascending(T1, T2):
    N = len(T1)
    counter = [0 for _ in range(N)]

    
    for i in range(N*N):
        indeks = find_smallest_id(T1, counter)
        print(indeks)
        T2[i] = T1[indeks][counter[indeks]]
        counter[indeks] += 1
    
    return T2
    
    
def find_smallest_id(T, counter):
    N = len(T)
    indeks = 0
    
    for i in range(1, N - 1):
        if counter[i] < N:
            if T[i][counter[i]] < T[indeks][counter[indeks]]: indeks = i
        
    return indeks

print(linearize_ascending([[1, 2, 3],[1, 4, 5],[7, 8, 9]], [0]*9))