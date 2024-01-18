"""
5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
należy połączyć w jedną listę odsyłaczową, która jest posortowana
niemalejąco według ostatniej cyfry pola val.
"""




class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def sol(p):
    if p is None:
        return None

    t1 = [Node() for _ in range(10)]
    t2 = [Node() for _ in range(10)]

    while p is not None:
        last_digit = p.val % 10

        if t1[last_digit] is None:
            t1[last_digit] = p
            t2[last_digit] = p
        else:
            t1[last_digit].next = p
            t2[last_digit] = p

        p = p.next

    # we connect the linked lists from 9 to 0
    # because it is easier to append to the start of the list
    # than to the end

    result = Node()

    for i in range(9, -1, -1):
        if t2[i] is not None:
            t2[i].next = result
            result = t1[i]
    
    return result


