
class Node:
    def __init__(self):
        self.val = None
        self.next = None


"""
first = None

for i in range(4):
    s = int(input('>>'))
    p = Node()
    p.val = s
    p.next = first
    first = p
"""


def wypisz1(p):
    while p is not None:
        print(p.val)
        p = p.next


def wypisz2(p):
    if p is not None:
        print(p.val)
        wypisz2(p.next)


def wypisz3(p):
    """Wypisz od końca"""
    if p is not None:
        wypisz3(p.next)
        print(p.val)


class LL:
    def __init__(self):
        self.first = None
        self.last = None


def add_head(l, n):
    p = Node()
    p.val = n
    p.next = l.first
    l.first = p
    if l.last is None:
        l.last = p


def add_tail(l, n):
    p = Node()
    p.val = n
    if l.last is not None:
        l.last.next = p
        l.last = p
    else:
        add_head(l, n)


linked = LL()

add_tail(linked, 7)
print(linked.first.val)

