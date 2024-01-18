from support import Node, print_list, get_ll

def read_and_append(p):
    num = 0
    while p is not None:
        num = num * 10 + p.val
        p = p.next
    
    return num + 1
    
def num_len(num):
    length = 0
    while num > 0:
        length += 1
        num //= 10
    return length


def create_ll_from_num(num):
    """Each digit in num represent single Node ex. for 123 we get
        1 -> 2 -> 3
    """
    length = num_len(num)
    num_digits = [0 for _ in range(length)]
    
    i = -1
    while num > 0:
        num_digits[i] = num % 10
        num //= 10
        i -= 1

    p = Node(num_digits[0])
    start = p

    for i in range(1, length):
        new = Node(num_digits[i])
        p.next = new
        p = p.next
    
    return start


def sol(p):
    num = read_and_append(p)
    
    p = create_ll_from_num(num)
    return p


if __name__ == '__main__':
    a = get_ll()
    
    a = sol(a)
    print_list(a)