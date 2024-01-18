from support import Node, print_list, get_ll

def sol(p, key):
    start = p
    if p is None:
        return Node(key)
    if p.val == key:
        return p.next
    
    while p.next is not None:
        if p.next.val == key:
            p.next = p.next.next
            return start
        p = p.next
    p.next = Node(key)
    return start


p = get_ll()

p = sol(p, 0)
print_list(p)