from support import Node, print_list, get_ll


def remove_element(p, to_delete):
    start = p

    while p.next != None:
        if p.next.val == to_delete:
            p.next = p.next.next
            return start
        p = p.next


def delete_last(p):
    start = p

    if p is None:
        return start

    elif p.next is None:
        return Node()

    while p.next is not None and p.next.next is not None:
        p = p.next
    p.next = None

    return start


p = get_ll()

p = delete_last(p)
print_list(p)
