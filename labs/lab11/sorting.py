"""Recursive sorting: mergesort and quicksort

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the two recursive sorting algorithms
mergesort and quicksort.
"""


def mergesort(lst):
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of mergesort; it does not mutate the
    input list.

    @type lst: list
    @rtype: list
    >>> lst = [3,56,2,7,1,9]
    >>> mergesort(lst)
    [1, 2, 3, 7, 9, 56]
    """
    if len(lst) < 2:
        return lst[:]  # what's the difference between this and "return lst"?
    else:
        # Divide the list into two parts, and sort them recursively.
        mid = len(lst) // 2
        left_sorted = mergesort(lst[:mid])
        right_sorted = mergesort(lst[mid:])

        # Merge the two sorted halves. Need a helper here!
        return merge(left_sorted, right_sorted)


def merge(lst1, lst2):
    """Return a sorted list with the elements in <lst1> and <lst2>.

    Precondition: <lst1> and <lst2> are sorted

    @type lst1: list
    @type lst2: list
    @rtype: list
    """
    # Use <index1> and <index2> to keep track of where you are
    # in each list, and <merged> to store the sorted list to return.
    index1 = 0
    index2 = 0
    merged = []

    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] < lst2[index2]:
            merged.append(lst1[index1])
            index1 += 1
        else:
            merged.append(lst2[index2])
            index2 += 1

    merged += lst1[index1:] + lst2[index2:]

    return merged


def quicksort(lst):
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of quicksort; it does not mutate the
    input list.

    @type lst: list
    @rtype: list
    >>> lst = [3,56,2,7,1,9]
    >>> quicksort(lst)
    [1, 2, 3, 7, 9, 56]
    """
    if len(lst) < 2:
        return lst[:]
    else:
        # Pick pivot to be first element.
        # Could make lots of other choices here (e.g., last, random)
        pivot = lst[0]

        # Partition rest of list into two halves
        smaller, bigger = partition(lst[1:], pivot)

        # Recurse on each partition
        smaller_sorted = quicksort(smaller)
        bigger_sorted = quicksort(bigger)

        # Return! Notice the simple combining step
        return smaller_sorted + [pivot] + bigger_sorted


def partition(lst, pivot):
    """Return a partition of <lst> according to the given pivot.

    Return two lists, where the first is the items in <lst> that are <= pivot,
    and the second is the items in <lst> that are > pivot.

    @type lst: list
    @type pivot: object
    @rtype: (list, list)
    """
    # Use a loop to go through <lst> to build up the two
    # lists. Note that <smaller> and <bigger> do *not* need to be sorted here.
    smaller = []
    bigger = []

    for i in lst:
        if i <= pivot:
            smaller.append(i)
        else:
            bigger.append(i)

    return smaller, bigger
