
def check_array(t):
    # ...

    return True


def cut_rows(t, r, cols, length):
    return [[t[row][i] for i in range(length) if i not in cols] for row in range(length) if row != r]


def sol(t):
    n = len(t)

    for row in range(n):
        for col1 in range(n - 1):
            for col2 in range(col1 + 1, n):
                if check_array(cut_rows(t, row, (col1, col2), n)):
                    return True

    return False

