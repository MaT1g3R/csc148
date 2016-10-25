"""Lab 5: Linked List Exercises

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the code for a linked list implementation with two classes,
LinkedList and _Node.

All of the code from lecture is here, as well as some exercises to work on.
"""


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one
    which is only meant to be used in this module by the
    LinkedList class, but not by client code.

    === Attributes ===
    @type item: object
        The data stored in this node.
    @type next: _Node | None
        The next node in the list, or None if there are
        no more nodes in the list.
    """
    def __init__(self, item):
        """Initialize a new node storing <item>, with no next node.

        @type self: _Node
        @type item: object
        @rtype: None
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.

    === Private Attributes ===
    @type _first: _Node | None
        The first node in the list, or None if the list is empty.
    @type length: int

    """
    def __init__(self, items):
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.

        @type self: LinkedList
        @type items: list
        @rtype: None
        """
        self.length = 0

        if len(items) == 0:  # No items, and an empty list!
            self._first = None
        else:
            self._first = _Node(items[0])
            current_node = self._first
            self.length += 1
            for item in items[1:]:
                current_node.next = _Node(item)
                current_node = current_node.next
                self.length += 1
        # Initialize a node for the iterator
        self._iter_node = None

    # ------------------------------------------------------------------------
    # Non-mutating methods: these methods do not change the list
    # ------------------------------------------------------------------------
    def is_empty(self):
        """Return whether this linked list is empty.

        @type self: LinkedList
        @rtype: bool
        """
        return self._first is None

    def __str__(self):
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        @type self: LinkedList
        @rtype: str

        >>> lst = LinkedList([1, 2, 3])
        >>> str(lst)
        '[1 -> 2 -> 3]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def __getitem__(self, index):
        """Return the item at position <index> in this list.

        Raise IndexError if <index> is >= the length of this list.

        @type self: LinkedList
        @type index: int
        @rtype: object
        """
        curr = self._first
        curr_index = 0

        # Iterate to (index)-th node
        while curr is not None and curr_index < index:
            curr = curr.next
            curr_index += 1

        if curr is None:
            raise IndexError
        else:
            return curr.item

    # --- Lab Exercises ---

    def __len__(self):
        """Return the number of elements in this list.

        @type self: LinkedList
        @rtype: int

        >>> lst = LinkedList([])
        >>> len(lst)              # Equivalent to lst.__len__()
        0
        >>> lst = LinkedList([1, 2, 3])
        >>> len(lst)
        3
        """
        return self.length

    def __contains__(self, item):
        """Return whether <item> is in this list.

        Use == to compare items.

        @type self: LinkedList
        @type item: object
        @rtype: bool

        >>> lst = LinkedList([1, 2, 3])
        >>> 2 in lst                     # Equivalent to lst.__contains__(2)
        True
        >>> 4 in lst
        False
        """
        current = self._first
        while current is not None:
            if current.item == item:
                return True
            else:
                current = current.next
        return False

    def count(self, item):
        """Return the number of times <item> occurs in this list.

        Use == to compare items.

        @type self: LinkedList
        @type item: object
        @rtype: int

        >>> lst = LinkedList([1, 2, 1, 3, 2, 1])
        >>> lst.count(1)
        3
        >>> lst.count(2)
        2
        >>> lst.count(3)
        1
        """
        i = 0
        current = self._first
        while current is not None:
            if current.item == item:
                i += 1
            current = current.next
        return i

    def index(self, item):
        """Return the index of the first occurrence of <item> in this list.

        Raise ValueError if the <item> is not present.

        Use == to compare items.

        @type self: LinkedList
        @type item: object
        @rtype: int

        >>> lst = LinkedList([1, 2, 1, 3, 2, 1])
        >>> lst.index(1)
        0
        >>> lst.index(3)
        3
        """
        i = 0
        current = self._first
        while current is not None:
            if current.item == item:
                return i
            else:
                i += 1
                current = current.next

        raise ValueError

if __name__ == '__main__':
    import python_ta
    python_ta.check_all()
