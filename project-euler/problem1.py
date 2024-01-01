# multiples of 3 or 5

def art_seq_sum(a, r, cap=1000):
    i = 1
    last = 0
    while last == 0:
        if (cap - i) % r == 0:
            last = cap - i
        i += 1
    n = last//r
    return int((a + last)/2 * n)


def main():
    print(art_seq_sum(5, 5) + art_seq_sum(3, 3) - art_seq_sum(15, 15))


if __name__ == '__main__':
    main()