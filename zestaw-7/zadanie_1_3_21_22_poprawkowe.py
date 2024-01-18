from support import Node, print_list, get_ll


def create_list(p):
    cnt = 0
    while p.next is not None:
        cnt += 1
        p = p.next

    return [0 for _ in range(cnt)]


def sol(p):
    head = Node()
    head.next = p
    l = create_list(head)

    eq_2 = Node()
    rest = Node()

    # count_ocurences
    i = 0
    while p is not None:
        l[i] = p.val
        p = p.next
        i += 1

    return eq_2, rest
