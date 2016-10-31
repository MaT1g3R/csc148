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
        """
        return self._root is None

    def __len__(self):
        """
        @type self: Tree
        @rtype: int
        """
        if self.is_empty():
            return 0
        else:
            return 1 + len(self._subtrees)
