from support import get_cycle


def first_dig(n):
    while n > 9:
        n //= 10
    return n


def sol(p, n):
    head = p

    while True:
        if p.val % 10 == first_dig(n):
            cnt = 0
            first = p
            while p.next != first:
                if first_dig(p.next.val) == n % 10 and cnt > 2:
                    return cnt - 1
                p = p.next
                cnt += 1
        p = p.next
        if p == head:
            break

    return 0


# 2023 31 17 703 37 707 72 29 902

a = get_cycle()

print(sol(a, 303))
