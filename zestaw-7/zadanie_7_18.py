from support import print_list, get_ll


def not_unique(p):
    cnt = {}
    
    while p is not None:
        keys = cnt.keys()
        if p.val not in keys:
            cnt[p.val] = 1
        else:
            cnt[p.val] += 1
        
        p = p.next
    
    return [key for key in cnt.keys() if cnt[key] > 1]

    
def sol(p):
    start = p
    to_delete = not_unique(p)
    
    # 
    if p is None:
        return p
    
    
    while p.next is not None and p.next.next is not None:
        if p.next.val in to_delete:
            p.next = p.next.next
        else:
            p = p.next
            
    # if p.next.next is None and p.next != None        
    if p.next.val in to_delete:
        p.next = None
    
    # if first elemnt is in to_delete
    if start.val in to_delete:
        start = start.next
    
    return start

p = get_ll()

#print_list(sol(p))
