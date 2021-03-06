"""CSC148 Lab 11: More on sorting

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains an in-place implementation of mergesort,
and a skeleton implementation of Timsort that you will work through
during this lab.
"""


def mergesort(lst, i=0, j=None):
    """Sort the items in lst[i:j] in non-decreasing order.
    Note: this mutates the list.

    @type lst: list
    @type i: int
    @type j: int | None
    @rtype: None
    """
    if j is None:
        j = len(lst)

    if j - i < 2:  # lst[i:j] has 0 or 1 elements
        pass
    else:
        # "Division" is just finding the middle index.
        # No new lists are created.
        mid = (i + j) // 2
        # Sort the two halves. Notice that we pass in indices
        # to change the "size of the input" we're recursing on.
        mergesort(lst, i, mid)
        mergesort(lst, mid, j)
        # Merge the sorted halves.
        merge(lst, i, mid, j)


def merge(lst, i, mid, j):
    """Sort the items in <lst> so that lst[i:j] is sorted.

    Precondition: lst[i:mid] and lst[mid:j] are sorted.

    @type lst: list
    @type i: int
    @type mid: int
    @type j: int
    @rtype: None
    """
    result = []
    left_index = i
    right_index = mid
    while left_index < mid and right_index < j:
        if lst[left_index] < lst[right_index]:
            result.append(lst[left_index])
            left_index += 1
        else:
            result.append(lst[right_index])
            right_index += 1

    # Rather than return the list, we mutate lst[i:j] directly.
    lst[i:j] = result + lst[left_index:mid] + lst[right_index:j]


def find_runs(lst):
    """Return a list of tuples indexing the runs of <lst>.

    @type lst: list
        Precondition: lst is non-empty
    @rtype: list[(int, int)]

    >>> find_runs([1, 4, 7, 10, 2, 5, 3, -1])
    [(0, 4), (4, 6), (6, 7), (7, 8)]
    >>> find_runs([0, 1, 2, 3, 4, 5])
    [(0, 6)]
    >>> find_runs([10, 4, -2, 1])
    [(0, 1), (1, 2), (2, 4)]
    """
    runs = []

    # Keep track of the start and end points of a run.
    run_start = 0
    run_end = 1
    while run_end < len(lst):
        # How can you tell if a run should continue?
        #   (When you do, update run_end.)
        if lst[run_end] >= lst[run_end - 1]:
            run_end += 1
        else:
            runs.append((run_start, run_end))
            run_start = run_end
            run_end += 1
        # How can you tell if a run is over?
        #   (When you do, update runs, run_start, and run_end.)
    runs.append((run_start, run_end))
    return runs


def timsort(lst):
    """Sort <lst> in place.

    Note: this mutates the list.

    @type lst: list
    @rtype: None

    >>> lst = []
    >>> timsort(lst)
    >>> lst
    []
    >>> lst = [1]
    >>> timsort(lst)
    >>> lst
    [1]
    >>> lst = [1, 4, 7, 10, 2, 5, 3, -1]
    >>> timsort(lst)
    >>> lst
    [-1, 1, 2, 3, 4, 5, 7, 10]
    """
    runs = find_runs(lst)

    # Treat runs as a stack and repeatedly merge the top two runs
    # When the loop ends, the only run should be the whole list.
    # HINT: you should be able to use the "merge" function provided
    # in this file.

    if len(runs) == 1:
        pass
    else:
        # i, m, j = runs[0][0], runs[0][1], runs[1][1]
        # merge(lst, i, m, j)
        # timsort(lst)

        # while len(runs) > 1:
        #     i, m, j = runs[0][0], runs[0][1], runs[1][1]
        #     merge(lst, i, m, j)
        #     runs = find_runs(lst)

        while len(runs) > 1:
            end = runs.pop()
            start = runs.pop()
            i, m, j = start[0], start[1], end[1]
            merge(lst, i, m, j)
            runs.append((i, j))


def find_runs2(lst):
    """Return a list of tuples indexing the runs of <lst>.

    Now, a run can be either ascending or descending!

    Precondition: len(lst) > 0

    @type lst: list
    @rtype: list[(int, int)]

    >>> find_runs2([1, 4, 7, 10, 2, 5, 3, -1])
    [(0, 4), (4, 6), (6, 8)]
    >>> find_runs2([0, 1, 2, 3, 4, 5])
    [(0, 6)]
    >>> find_runs2([10, 4, -2, 1])
    [(0, 3), (3, 4)]
    >>> find_runs2([10, 4, -2, 1, -1])
    [(0, 3), (3, 5)]
    """
    # Hint: this is similar to find_runs, except
    # you'll need to keep track of whether the "current run"
    # is ascending or descending.
    runs = []
    start = 0
    end = 1
    while end < len(lst):
        acending = False
        if lst[end] >= lst[start]:
            acending = True

        while acending and end < len(lst):
            if lst[end] >= lst[end - 1]:
                end += 1
            else:
                runs.append((start, end))
                start = end
                end += 1
                break

        while not acending and end < len(lst):
            if lst[end] < lst[end - 1]:
                end += 1
            else:
                runs.append((start, end))
                start = end
                end += 1
                break

    runs.append((start, end))
    return runs


def find_runs3(lst):
    """Same as find_runs2, but each run (except the last one)
    must be of length >= 32.

    Precondition: len(lst) > 0

    @type lst: list
    @rtype: list[(int, int)]
    >>> find_runs3([1, 4, 7, 10, 2, 5, 3, -1])
    [(6, 8)]
    >>> find_runs3([0, 1, 2, 3, 4, 5])
    [(0, 6)]
    >>> find_runs3([10, 4, -2, 1])
    [(3, 4)]
    >>> find_runs3([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, -10])
    [(0, 32), (32, 33)]
    """
    runs = []
    start = 0
    end = 1
    while end < len(lst):
        acending = False
        if lst[end] >= lst[start]:
            acending = True

        while acending and end < len(lst):
            if lst[end] >= lst[end - 1]:
                end += 1
            else:
                if end - start >= 32:
                    runs.append((start, end))
                start = end
                end += 1
                break

        while not acending and end < len(lst):
            if lst[end] < lst[end - 1]:
                end += 1
            else:
                if end - start >= 32:
                    runs.append((start, end))
                start = end
                end += 1
                break

    runs.append((start, end))
    return runs


def insertion_sort(lst, left, right):
    """Sort the items in lst[left:right] in non-decreasing order.

    @type lst: list
    @type left: int
    @type right: int
    @rtype: None
    """
    for i in range(left + 1, right):
        # Find where lst[i] belongs in lst[left:i], but don't swap!
        j = i - 1
        while j >= left and lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j -= 1


def merge2(lst, i, mid, j):
    """Sort the items in lst so that lst[i:j] is sorted.
    Note: this mutates the list.

    Only use temporary storage of size (mid - i).

    @type lst: list
        Precondition: lst[i:mid] and lst[mid:j] are sorted.
    @type i: int
    @type mid: int
    @type j: int
    @rtype: None
    """
    pass


def timsort2(lst):
    """Sort <lst> using the version of timsort from Task 6.
    Note: this mutates the list.

    @type lst: list
    @rtype: None

    >>> lst = []
    >>> timsort(lst)
    >>> lst
    []
    >>> lst = [1]
    >>> timsort(lst)
    >>> lst
    [1]
    >>> lst = [1, 4, 7, 10, 2, 5, 3, -1]
    >>> timsort(lst)
    >>> lst
    [-1, 1, 2, 3, 4, 5, 7, 10]
    """
    pass
