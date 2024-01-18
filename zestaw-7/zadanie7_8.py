from support import get_ll, print_list
        
def delete_even(p):
    start = p

    while p.next is not None:
        p.next = p.next.next
        p = p.next
    
    return start


p = get_ll()


#p = delete_even(p)
#print_list(p)
