from support import get_ll, print_list

def count_octal(num):
    cnt_5 = 0
    while num > 0:
        if num % 8 == 5:
            cnt_5 += 1
        num //= 8
    return cnt_5
    
    
def sol(p):
    head = p
    
    if p is None:
        return p
    
    while p.next is not None and p.next.next is not None:
        cnt = count_octal(p.next.val)
        if cnt % 2 == 0:
            p.next.next, p.next, head = head, p.next.next, p.next
        else:
            p = p.next
            
    cnt = count_octal(p.next.val)
    if cnt % 2 == 0:
        p.next.next, head, p.next = head, p.next, None
    
    return head


p = get_ll()

            
print_list(sol(p))