from support import DoubleNode, print_list

def count_binary(num):
    cnt = {i:0 for i in range(2)}
    
    while num > 0:
        cnt[num%2] += 1
        num //= 2
    return cnt


def sol(p):
    start = p
    
    if p is None:
        return p
    
    while p is not None:
        # cnt = <number of 'ones' in binary representation>
        cnt = count_binary(p.val)[1]
        if cnt % 2 == 1:
            p.last.next = p.next
        p = p.next
            
    return start

p = DoubleNode(0)
a = DoubleNode(1)
b = DoubleNode(45)
c = DoubleNode(3)
d = DoubleNode(7)
e = DoubleNode(5)
f = DoubleNode(12)
p.next = a

a.next = b
a.last = p

b.next = c
b.last = a

c.next = d
c.last = b

d.next = e
d.last = c

e.next = f
e.last = d

#print_list(sol(p))
