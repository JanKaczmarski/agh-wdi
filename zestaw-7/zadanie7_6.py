from support import get_ll



def insert(p, value):
    
    if p is None:
        return None
    
    while p is not None:
        p = p.next
    
    p.val = value
    
p = get_ll()


    

    