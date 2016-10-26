"""
Recursion
"""

def sum_list(lst):
    """
    @type lst: list[int]
    @rtype: int
    """
    s = 0
    for i in lst:
        s += i
    return s


def sum_list_2(lst):
    """
    @type lst: list[list[int]]
    @rtype: int
    """
    s = 0
    for i in lst:
        s += sum_list(i)
    return s


# etc...

def sum_of_nested_list(lst):
    """
    @type lst: list|int
    @rtype: int
    >>> sum_of_nested_list([1,2,3])
    6
    >>> sum_of_nested_list([1,2,[1,2]])
    6
    >>> sum_of_nested_list([1,2,3,4,[2,2,[1,2,[[1]]]]])
    18
    >>> sum_of_nested_list(5)
    5
    """
    s = 0
    if isinstance(lst, int):
        s += lst
    else:
        for i in lst:
            s += sum_of_nested_list(i)
    return s
