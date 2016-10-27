"""Lab 7: Recursion, Task 2

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains a few nested list functions for you to practice
implementing recursively.
"""


def nested_max(obj):
    """Return the maximum item stored in <obj>.

    You may assume all the items are positive, and calling
    nested_max on an empty list returns 0.

    @type obj: int | list
    @rtype: int

    >>> nested_max(17)
    17
    >>> nested_max([1, 2, [1, 2, [3], 4, 5], 4])
    5
    """
    if isinstance(obj, int):
        return obj
    else:
        max_ = 0
        for item in obj:
            if nested_max(item) > max_:
                max_ = nested_max(item)
        return max_


def length(obj):
    """Return the length of <obj>.

    The *length* of a nested list is defined as:
    1. 0, if <obj> is a number.
    2. The maximum of len(obj) and the lengths of the nested lists contained
       in <obj>, if <obj> is a list.

    @type obj: int | list
    @rtype: int

    >>> length(17)
    0
    >>> length([1, 2, [1, 2], 4])
    4
    >>> length([1, 2, [1, 2, [3], 4, 5], 4])
    5
    """
    if isinstance(obj, int):
        return 0
    else:
        len_ = len(obj)
        for item in obj:
            len2 = length(item)
            if len2 > len_:
                len_ = len2
        return len_


def equal(obj1, obj2):
    """Return whether two nested lists are equal, i.e., have the same value.

    Note: order matters.

    @type obj1: int | list
    @type obj2: int | list
    @rtype: bool

    >>> equal(17, [1, 2, 3])
    False
    >>> equal([1, 2, [1, 2], 4], [1, 2, [1, 2], 4])
    True
    >>> equal([1, 2, [1, 2], 4], [4, 2, [2, 1], 3])
    False
    >>> equal([1,2,3], [1,[2],3])
    True
    """
    return flatten(obj1) == flatten(obj2)


def flatten(lst):
    """Return a list containing all the numbers in <lst>.

    <lst> is a nested list, but the returned list should not be nested.
    The items should appear in the output in the left-to-right order they
    appear in <lst>.

    @type lst: int | list
    @rtype: list[int]

    >>> flatten(5)
    [5]
    >>> flatten([1, [2], 3])
    [1, 2, 3]
    >>> flatten([[1, 5, 7], [[4]], 0, [-4, [6], [7, [8], 8]]])
    [1, 5, 7, 4, 0, -4, 6, 7, 8, 8]
    """
    if isinstance(lst, int):
        return [lst]
    else:
        result = []
        for lst_i in lst:
            result += flatten(lst_i)
        return result
