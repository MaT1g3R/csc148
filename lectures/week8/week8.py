""" Trees
"""


class Tree:
    """ A recursive tree data structure
    === Private Attributes ===
    @type _root: object | None
    @type _subtrees: list[Tree]

    === Representation Invariants ===
    - if self._root is None then self._subtrees is empty.
    - self._subtrees does not contain any empty trees
    """
    def __init__(self, root, subtrees):
        """
        @type self: Tree
        @type root: object
        @type subtrees: list[Tree]
        @rtype: None
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self):
        """
        @type self: Tree
        @rtype: bool

        >>> tree = Tree(None, [])
        >>> tree.is_empty()
        True
        >>> tree = Tree(10, [])
        >>> tree.is_empty()
        False
        """
        return self._root is None

    def __len__(self):
        """
        @type self: Tree
        @rtype: int
        >>> subtree = Tree(10,[])
        >>> tree = Tree(100, [subtree])
        >>> len(tree)
        2
        """
        if self.is_empty():
            return 0
        else:
            size = 1
            for subtree in self._subtrees:
                size += len(subtree)
            return size

    def count(self, item):
        """
        @type self: Tree
        @type item: object
        @rtype: int
        >>> subtree = Tree(10,[])
        >>> tree = Tree(10, [subtree])
        >>> tree.count(10)
        2
        >>> tree.count(100)
        0
        """
        if self.is_empty():
            return 0
        else:
            c = 1 if self._root == item else 0
            for subtree in self._subtrees:
                c += subtree.count(item)
            return c
