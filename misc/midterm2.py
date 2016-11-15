from rec_linked_list import LinkedListRec
from tree import Tree
from week9 import BinarySearchTree

def filter_pos_rec(lst):
    """
    Return a new LinkedListRec whose items are
    the ones in lst that have value > 0.
    The items must appear in the * same order *
    they do in lst.

    @type lst: LinkedListRec | int
    @rtype: LinkedListRec | int

    >>> lst = LinkedListRec ([3 , -10 , 4 , 0, 5]) # [3 -> -10 -> 4 -> 0 -> 5]
    >>> pos = filter_pos_rec(lst) # pos is [3 -> 4 -> 5]
    >>> pos.__str__()
    '3 -> 4 -> 5'
    """
    if isinstance(lst, int):
        if lst > 0:
            return lst
    elif lst.is_empty():
        pass
    else:
        r = []
        if filter_pos_rec(lst._first) is not None:
            r += [lst._first]
        if filter_pos_rec(lst._rest) is not None:
            r += filter_pos_rec(lst._rest)
        return LinkedListRec(r)


def count_depth(tree, d):
    """
    Return the number of nodes in tree at depth d .
    You may assume that d >= 1.
    @type tree: Tree
    @type d: int
    @rtype: int
    >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
    >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
    >>> t = Tree(1, [lt, rt])
    >>> count_depth(t, 3)
    7
    """
    if tree.is_empty():
        return 0
    elif d == 1:
        return 1
    elif d == 2:
        return len(tree._subtrees)
    else:
        r = 0
        for sub in tree._subtrees:
            r += count_depth(sub, d-1)
        return r

def size (bst):
    """
    Return the number of items contained in this BST .
    @type bst: BinarySearchTree
    @rtype: int
    >>> bst = BinarySearchTree(7)
    >>> left = BinarySearchTree(3)
    >>> left._left = BinarySearchTree(2)
    >>> left._right = BinarySearchTree(5)
    >>> right = BinarySearchTree(11)
    >>> right._left = BinarySearchTree(9)
    >>> right._right = BinarySearchTree(13)
    >>> bst._left = left
    >>> bst._right = right
    >>> bst.items()
    [2, 3, 5, 7, 9, 11, 13]
    >>> size(bst)
    7
    """
    if bst.is_empty():
        return 0
    else:
        return 1 + size(bst._left) + size(bst._right)


def kth_smallest(bst, k):
    """
    Precondition : 1 <= k <= size of this BST
    Return the kth_smallest value in this BST . So if a BST b contains
    the items {1 ,3 ,5 ,8 ,10 ,11} , then b . kth_smallest (2) returns 3 , and
    b . kth_smallest (5) returns 10.

    Note : the return value depends only on the items in the tree , and
    not the structure . So if two trees contain the same items , but have
    different roots , calling kth_smallest still returns the same value .

    @type bst: BinarySearchTree
    @type k: int
    @rtype: object
    >>> bst = BinarySearchTree(7)
    >>> left = BinarySearchTree(3)
    >>> left._left = BinarySearchTree(2)
    >>> left._right = BinarySearchTree(5)
    >>> right = BinarySearchTree(11)
    >>> right._left = BinarySearchTree(9)
    >>> right._right = BinarySearchTree(13)
    >>> bst._left = left
    >>> bst._right = right
    >>> bst.items()
    [2, 3, 5, 7, 9, 11, 13]
    >>> kth_smallest(bst, 6)
    9
    """
