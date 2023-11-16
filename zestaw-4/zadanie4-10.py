
def zadanie_10(T):
    N = len(T)
    sol = [0 for _ in range(N + N)]
    for i in range(N):
        for j in range(N):
            if T[i][j] == 0:
                sol[i], sol[N + j] = 1, 1
            # end
        # end
    # end
    
    for i in range(len(sol)):
        if sol[i] == 0:
            return False
        # end
    # end
    return True
# end def

print(zadanie_10([[0,0,1,1],[0,1,1,0],[1,1,0,1],[0,1,1,1]]))
