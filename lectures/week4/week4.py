# Custom error
class EmptyStackError(Exception):
    """ This error is used when pop is called on an empty stack
    """
    pass


class Stack:
    """
    === Private Attributes ===
    @type _items: list
    The back of the list is the front of the list
    """

    def __init__(self):
        """
        @type self: Stack
        @rtype: None
        """
        self._items = []

    def is_empty(self):
        """ Check if the stack is empty
        @type self: Stack
        @rtype: bool
        """
        return len(self._items) == 0

    def push(self, item):
        """ Add a new element to the top of the stack
        @type self: Stack
        @type item: object
        @rtype: None
        """

        self._items.append(item)

    def pop(self):
        """ Remove and return the element at the top of the stack
        @type self: Stack
        @rtype: object
        """
        if not self.is_empty():
            # This pop is the LIST pop
            return self._items.pop()
        else:
            raise EmptyStackError

    """
    Write a function that takes a stack and computes is size, but leaves
    the stack unchanegd when the function returns.
    """

    def get_stack_size(self):
        tmp = []

        while not self.is_empty():
            tmp.append(self.pop())

        tmp.reverse()
        for item in tmp:
            self.push(item)

        return len(tmp)






