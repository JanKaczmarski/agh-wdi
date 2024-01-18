from support import Node, print_list, get_ll


def empty_arr(z1, z2, z3):
    cnt = 0
    while z1 != None:
        cnt += 1
        z1 = z1.next

    while z2 != None:
        cnt += 1
        z2 = z2.next

    while z3 != None:
        cnt += 1
        z3 = z3.next

    return [0 for _ in range(cnt)]


def iloczyn(z1: Node, z2: Node, z3: Node) -> Node:
    elements = empty_arr(z1, z2, z3)

    # z1
    i = 0
    while z1 is not None:
        elements[i] = z1.val
        z1 = z1.next
        i += 1

    # z2
    while z2 is not None:
        elements[i] = z2.val
        z2 = z2.next
        i += 1

    # z3
    while z3 is not None:
        elements[i] = z3.val
        z3 = z3.next
        i += 1

    new_list_el = [i for i in elements if elements.count(i) == 3]
    already_used = [0 for _ in range(len(new_list_el))]

    p = Node()  # guardian
    start = p
    i = 0

    for el in new_list_el:
        if el not in already_used:
            new = Node(el)
            p.next = new
            p = p.next
            already_used[i] = el
            i += 1

    return start


l1, l2, l3 = get_ll(1, 2, 3, 4, 5, 6), get_ll(
    2, 3, 4, 8, 16, 64), get_ll(2, 3, 9, 18, 27, 81)

print_list(iloczyn(l1, l2, l3), guardian=True)
