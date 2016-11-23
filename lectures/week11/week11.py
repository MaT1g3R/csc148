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
    pass
