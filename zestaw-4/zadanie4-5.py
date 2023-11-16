# zadanie 5

def sum_row(T):
    suma = 0
    length = len(T)
    for i in range(length):
        suma += T[i]
    return suma

def sum_col(T, col):
    suma = 0
    length = len(T)
    for i in range(length):
        suma += T[i][col]
    return suma


def biggest_row_col_ratio(T):
    length = len(T)
    sol = [[0, -1, -1] for _ in range(length**2)]
    for i in range(length):
        summed_row = sum_row(T[i])
        if summed_row != 0:
            for j in range(length):
                sol[length * i + j][0] = sum_col(T, j) / summed_row
                sol[length * i + j][1] = i
                sol[length * i + j][2] = j

    biggest = [0, -1, -1]
    for i in range(length**2):
        if sol[i][0] > biggest[0]:
            biggest = sol[i]
    return biggest[1], biggest[2]

print(biggest_row_col_ratio([[0,0,0],[1,1,1],[-2,-2,-2]]))