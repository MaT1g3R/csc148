def mergesort(lst):
    """return a sorted list with the same elements as <list>
    This is a non-mutating version
    @type lst: list
    @rtype: list
    >>> lst =[4,5,7,1,3,8]
    >>> mergesort(lst)
    [1, 3, 4, 5, 7, 8]
    """
    if lst == []:
        return []
    elif len(lst) == 1:
        return lst[:]
    else:
        mid = len(lst)//2  # // rounds down
        # divide the list into two halves
        left_half = lst[:mid]
        right_half = lst[mid:]

        # recursivly sort each half
        sorted_left = mergesort(left_half)
        sorted_right = mergesort(right_half)

        # combine
        return merge(sorted_left, sorted_right)


def merge(lst1, lst2):
    """ return a sorted list with the elements in <lst1> and <lst2>
    precndition: <lst1> and <lst2> are sorted

    @type lst1: list
    @type lst2: list
    @rtype: list
    """
    if lst1 == lst2 == []:
        return []
    else:
        r = []
        while lst1 != [] and lst2 != []:
            if lst1[0] < lst2[0]:
                r.append(lst1.pop(0))
            else:
                r.append(lst2.pop(0))

        if lst1 == []:
            r += lst2
        elif lst2 == []:
            r += lst1

        return r


def quicksort(lst):
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of quicksort; it does not mutate the
    input list.

    @type lst: list
    @rtype: list
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
