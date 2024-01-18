"""
1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
struktury listy odsyłaczowej.
- czy element należy do zbioru
- wstawienie elementu do zbioru
- usunięcie elementu ze zbioru
"""


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.guardian = Node()
        self.length = 0

    def print(self):
        el = self.guardian.next
        print('Guardian', end=" ")
        while el is not None:
            print('---->', el.val, end=" ")
            el = el.next

        print()

    def add(self, a):
        n = self.guardian
        while n.next is not None:
            n = n.next
        new_node = Node(val=a)
        n.next = new_node

    def belongs(self, a):
        n = self.guardian.next
        while n is not None:
            if n.val == a:
                return True
            n = n.next
        return False


args = (1,2,3)

ll = LinkedList()
for arg in args:
    ll.add(arg)

ll.print()
print(ll.belongs(2))
ll.add(4)
ll.print()