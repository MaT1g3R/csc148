def funtion (mychar, mystr):

    mid = len(mystr)/2 + 0.5
    c = 0

    for char in mystr:
        c += 1
        if char == mychar:
            return c > mid


class A :
    def __init__ ( self , x ):
        self . x = x

    def show ( self ):
        print ( self . x )

class B ( A ):
    def show ( self ):
        print (" I ’ m a B !")

    def noshow ( self ):
        print (" shhh ")

from stack import Stack
def combine ( stack1 , stack2 ):
    """
    >>> stack1 = Stack()
    >>> stack1.push(1)
    >>> stack1.push(2)
    >>> stack1.push(3)
    >>> stack2 = Stack()
    >>> stack2.push(4)
    >>> stack2.push(5)
    >>> stack2.push(6)
    >>> new = combine(stack1, stack2)
    >>> new.pop()
    6
    >>> new.pop()
    5
    >>> new.pop()
    4
    >>> new.pop()
    3
    >>> new.pop()
    2
    >>> new.pop()
    1
    >>> new.is_empty()
    True
    >>> stack1.pop()
    3
    >>> stack1.pop()
    2
    >>> stack1.pop()
    1
    >>> stack1.is_empty()
    True
    >>> stack2.pop()
    6
    >>> stack2.pop()
    5
    >>> stack2.pop()
    4
    >>> stack2.is_empty()
    True
    """
    stack1_orig = Stack()
    stack1_reversed = Stack()
    stack2_orig = Stack()
    stack2_reversed = Stack()
    new_stack = Stack()

    while not stack1.is_empty():
        x = stack1.pop()
        stack1_orig.push(x)
        stack1_reversed.push(x)

    while not stack2.is_empty():
        x = stack2.pop()
        stack2_orig.push(x)
        stack2_reversed.push(x)

    while not stack1_reversed.is_empty():
        new_stack.push(stack1_reversed.pop())

    while not stack2_reversed.is_empty():
        new_stack.push(stack2_reversed.pop())

    while not stack1_orig.is_empty():
        stack1.push(stack1_orig.pop())

    while not stack2_orig.is_empty():
        stack2.push(stack2_orig.pop())

    return new_stack

from library_linked_list import *


def filter_positive ( lst ):
    """
    >>> lst = LinkedList ([3 , -10 , 4 , 0])

    >>> pos = filter_positive (lst) # [3 -> 4]
    >>> pos._first.item
    3
    >>> pos._first.next.item
    4
    >>> pos._first.next.next is None
    True
    >>> lst[0]
    3
    >>> lst[1]
    -10
    """



    current = lst._first
    new_list = []
    while current is not None:
        if current.item > 0:
            new_list.append(current.item)
        current = current.next

    return LinkedList(new_list)


class _DoubleNode:

    def __init__(self, item):
        self.item = item
        self.next = None
        self.pre = None


class DoubleLinkedList:

    def __init__(self, items):
        if len(items) == 0:
            self._first = None
        else:
            self._first = _DoubleNode(items[0])
            current_node = self._first
            for item in items[1:]:
                current_node.next = _DoubleNode(item)
                current_node.next.pre = current_node
                current_node = current_node.next



if __name__ == '__main__':
    lst = [0, 1, 2, 3, 4]
    linky = DoubleLinkedList(lst)

    print(linky._first.item)
    print(linky._first.next.item)
    print(linky._first.next.next.item)
    print(linky._first.next.next.next.item)
    print(linky._first.next.next.next.next.item)
    print(linky._first.next.next.next.next.pre.item)
    print(linky._first.next.next.next.next.pre.pre.item)








