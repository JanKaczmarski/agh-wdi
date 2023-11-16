
def sol(T):
    N = len(T)
    for i in range(N - 5):
        seq_len = 2
        while i + seq_len < (N - i) // 2:
            flag = True
            ratio = T[i] / T[i + seq_len + 1]
            for j in range(1, seq_len + 1):
                if T[i + j] / T[i + seq_len + j + 1] != ratio:
                    flag = False
                    break
            if flag:
                return i, i + seq_len
            else:
                seq_len += 1
                
print(sol([2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2]))
