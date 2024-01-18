class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def print_tree(p):
    if p is not None:
        print(p.val)
        print_tree(p.left)
        print_tree(p.right)


def size_tree(p):
    if p is None:
        return 0

    return size_tree(p.right) + size_tree(p.left) + 1


def height_tree(p):
    if p is None:
        return 0

    return max(height_tree(p.left), height_tree(p.right)) + 1


def count_leafs(p):
    if p is None:
        return 0

    if p.left is None and p.right is None:
        return 1

    return count_leafs(p.left) + count_leafs(p.right)


def n_tree(p, n):
    if p is None:
        return 0

    if n == 0:
        return 1

    return n_tree(p.left, n - 1) + n_tree(p.right, n - 1)
