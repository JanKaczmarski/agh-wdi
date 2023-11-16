# zadanie 5

# 12345670

def get_sub_seqs(seq):
    seqs = []
    for i in range(len(seq)):
        w = 1
        while i + w <= len(seq):
            seqs.append(int(seq[i:i+w]))
            w += 1
    seqs.sort()
    return seqs[-10]

a = input()

print(get_sub_seqs(a[:-1]))