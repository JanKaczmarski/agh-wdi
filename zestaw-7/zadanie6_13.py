from support import get_ll, print_list


def sol(p):
    start = p
    if p is None:
        return p

    while p.next is not None:
        if p.next.val < p.val:
            # delete all nodes that values are lower than p.val
            copy = p.next
            max_val = p.val
            while copy.next is not None:
                if copy.next.val >= max_val:
                    p.next = copy.next
                    break
                else:
                    copy = copy.next
        p = p.next
    
    return start

p = get_ll()

print_list(sol(p))
                    