from support import get_cycle, Node, print_cycle

def sol(p):
    odd = Node()
    even = Node()
    even_flag = True
    odd_flag = True
    start = p
    
    cnt = 0
    cnt_valid = 0
    while True:
        if p.val > 0 and p.val % 2 == 0:
            cnt_valid += 1
            tmp = Node(p.val)
            if even_flag:
               first_even = tmp
               even = tmp
               even_flag = False
            else:
                even.next = tmp
                even = even.next
        elif p.val < 0 and abs(p.val) % 2 != 0:
            cnt_valid += 1
            tmp = Node(p.val)
            if odd_flag:
                first_odd = tmp
                odd = tmp
                odd_flag = False
            else:
                odd.next = tmp
                odd = odd.next
        
        p = p.next
        cnt += 1
        if p == start:
            break
        
    if not even_flag:
        even.next = first_even
    if not odd_flag:
        odd.next = first_odd
    
    return even, odd, cnt - cnt_valid


p = get_cycle(2, 4, -3, 1, 3, -1)

l1, l2, n = sol(p)
#print_cycle(l1)
#print('******')
#print_cycle(l2)
#print('******')
#print(n)