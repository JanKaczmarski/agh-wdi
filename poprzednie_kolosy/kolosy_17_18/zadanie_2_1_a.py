

def suma_pol(T, rows, cols):
    suma = 0
    n = len(T)
    for row in range(n):
        for col in range(n):
            if row in rows and col not in cols:
                suma += T[row][col]
            elif row not in rows and col in cols:
                suma += T[row][col]

    return suma


def possible_moves(n, w1, w2):
    # vertical w1, horizontal w1, vertical w2, horizontal w2
    return ([(i, w1[1]) for i in range(n) if i != w1[0]],
            [(w1[0], i) for i in range(n) if i != w1[1]],
            [(i, w2[1]) for i in range(n) if i != w2[0]],
            [(w2[0], i) for i in range(n) if i != w2[1]]
            )


def sol(T, w1, w2):
    n = len(T)
    target = suma_pol(T, (w1[0], w2[0]), (w1[1], w2[1]))

    for i, set_of_moves in enumerate(possible_moves(n, w1, w2)):
        if i < 2:
            for move in set_of_moves:
                if suma_pol(T, (move[0], w2[0]), (move[1], w2[1])) > target:
                    return True

        else:
            for move in set_of_moves:
                if suma_pol(T, (w1[0], move[0]), (w1[1], move[1])) > target:
                    return True

    return False



