def iter_bs(lst, item):
    """ return the index of item in a sorted list
    @type lst: list[int]
    @type item: int
    @rtype: int
    >>> lst = [0,1,2,3,4,5,6]
    >>> iter_bs(lst, 2)
    2
    """
    mid = len(lst)//2
    new = lst[:]
