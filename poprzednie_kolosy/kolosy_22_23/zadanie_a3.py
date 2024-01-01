

def king(N, L):
    sol = 0
    moves = ((0, 1), (1, 0), (-1, 0))

    def rek(w, k, prev, cnt):
        print(w,k)
        nonlocal sol

        if w == N-1 and k == N-1:
            if cnt > sol:
                sol = cnt
                return
        elif (w, k) in L:
            return

        for move in moves:
            print(move)
            if move != prev:
                rek(w + move[0], k + move[1], move, cnt + 1)

    rek(0, 0, (-1, 0), 0)

    if sol != 0:
        return sol

    return None


print(king(3,
           [
             ]))
