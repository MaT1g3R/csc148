def mergesort(lst):
    """return a sorted list with the same elements as <list>
    This is a non-mutating version
    @type lst: list
    @rtype: list
    """
    if lst == []:
        return []
    elif len(lst) == 1:
        return [lst[0]]
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
    pass


def quicksort(lst):
    pass
