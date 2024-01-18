from support import print_list, get_ll


def count_trinary(num):
    cnt_1 = 0
    cnt_2 = 0
    while num > 0:
        rest = num % 3
        if rest == 2:
            cnt_2 += 1
        elif rest == 1:
            cnt_1 += 1
        num //= 3
    return {'1': cnt_1, '2': cnt_2}


def sol(p):
    start = p

    if p is None:
        return p

    while p.next is not None and p.next.next is not None:
        # cnt is a dict
        # get all 'ones' and 'twos' in trinary representaion of a 
        # num
        cnt = count_trinary(p.next.val)
        # if conditions met delete element from list
        if cnt['1'] > cnt['2']:
            p.next = p.next.next
        else:
            # if not else
            # then we will skip values in list
            p = p.next

    cnt = count_trinary(p.next.val)
    if cnt['1'] > cnt['2']:
        p.next = None

    return start


p = get_ll()

print_list(sol(p))
