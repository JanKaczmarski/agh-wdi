class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
       

def member(zb, n):
    while zb != None:
        if zb.val == n: return True
        zb = zb.next
    return False

# usage:
# zb = insert(zb, 12)
def insert(zb, el):
    if zb == None:
        zb == Node(el)
        return zb


