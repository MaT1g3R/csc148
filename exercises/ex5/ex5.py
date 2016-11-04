"""CSC148 Exercise 5: Tree Practice

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains starter code for Exercise 5.
It is divided into three parts:
- Task 1, which contains one Tree method to implement.
- Task 2, which asks you to implement two operations that allow you
  to convert between trees and nested lists.
- Task 3, which asks you to learn about and use a more restricted form of
  trees known as *binary trees*.
"""


class Tree:
    """A recursive tree data structure.

    Note the relationship between this class and LinkedListRec
    from Lab 7; the only major difference is that _rest
    has been replaced by _subtrees to handle multiple
    recursive sub-parts.

    === Private Attributes ===
    @type _root: object | None
        The item stored at the tree's root, or None if the tree is empty.
    @type _subtrees: list[Tree]
        A list of all subtrees of the tree.

    === Representation Invariants ===
    - If self._root is None then self._subtrees is empty.
      This setting of attributes represents an empty Tree.
    - self._subtrees does not contain any empty Trees.
    """
    def __init__(self, root, subtrees):
        """Initialize a new Tree with the given root
        value and subtrees.

        If <root> is None, the tree is empty.

        @type self: Tree
        @type root: object
        @type subtrees: list[Tree]
        @rtype: None
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self):
        """Return True if this tree is empty.

        @type self: Tree
        @rtype: bool
        """
        return self._root is None

##############################################################################
# Task 1: Another tree method
##############################################################################
    def __eq__(self, other):
        """Return whether <self> and <other> are equal.

        @type self: Tree
        @type other: Tree
        @rtype: bool

        >>> tree1 = Tree(10, [])
        >>> tree2 = Tree(10, [])
        >>> tree3 = Tree(10000, [])
        >>> tree1 == tree2
        True
        >>> tree3 == tree2
        False
        >>> tree4 = Tree(10, [Tree(10,[])])
        >>> tree5 = Tree(10, [Tree(20,[])])
        >>> tree4 == tree5
        False
        >>> tree1 == tree4
        False
        >>> tree6 = Tree(10, [tree4, tree5])
        >>> tree6 == tree5
        False
        >>> tree7 = Tree(10, [Tree(10,[Tree(20,[])])])
        >>> tree8 = Tree(10, [Tree(10,[Tree(20,[])])])
        >>> tree7 == tree8
        True
        >>> tree9 = Tree(None,[])
        >>> tree10 = Tree(None,[])
        >>> tree9 == tree10
        True
        >>> tree1 == tree9
        False
        """
        if self.is_empty():
            return self._root == other._root
        elif len(self._subtrees) != len(other._subtrees) \
                or self._root != other._root:
            return False
        else:
            r_bool = True
            for i in range(len(self._subtrees)):
                r_bool = self._subtrees[i] == other._subtrees[i]
                if r_bool is False:
                    return False
            return r_bool


##############################################################################
# Task 2: Trees and nested lists
##############################################################################
    def to_nested_list(self):
        """Return the nested list representation of this tree.

        @type self: Tree
        @rtype: list
        >>> tree7 = Tree(10, [Tree(10,[Tree(20,[])])])
        >>> tree7.to_nested_list()
        [10, [10, [20]]]

        >>> E = Tree('E',[])
        >>> F = Tree('F',[])
        >>> G = Tree('G',[])
        >>> I = Tree('I',[])
        >>> J = Tree('J',[])
        >>> H = Tree('H',[J])
        >>> B = Tree('B',[E,F])
        >>> C = Tree('C',[G,H])
        >>> D = Tree('D',[I])
        >>> A = Tree('A',[B,C,D])
        >>> A.to_nested_list()
        ['A', ['B', ['E'], ['F']], ['C', ['G'], ['H', ['J']]], ['D', ['I']]]
        """
        if len(self._subtrees) == 0:
            return [self._root]
        else:
            nested = [self._root]
            for i in self._subtrees:
                nested.append(i.to_nested_list())
            return nested


def to_tree(obj):
    """Return the Tree which <obj> represents.

    Precondition: <obj> is a valid nested list representation of a tree.
                  (In particular, <obj> is not an int.)

    You may not access Tree attributes directly. This function can be
    implemented only using the Tree constructor.

    @type obj: list
    @rtype: Tree
    >>> n = ['A', ['B', ['E'], ['F']], ['C', ['G'], ['H', ['J']]], ['D', ['I']]]
    >>> E = Tree('E',[])
    >>> F = Tree('F',[])
    >>> G = Tree('G',[])
    >>> I = Tree('I',[])
    >>> J = Tree('J',[])
    >>> H = Tree('H',[J])
    >>> B = Tree('B',[E,F])
    >>> C = Tree('C',[G,H])
    >>> D = Tree('D',[I])
    >>> A = Tree('A',[B,C,D])
    >>> new_tree = to_tree(n)
    >>> new_tree == A
    True
    >>> print(new_tree.to_nested_list())
    ['A', ['B', ['E'], ['F']], ['C', ['G'], ['H', ['J']]], ['D', ['I']]]


    >>> tree7 = Tree(10, [Tree(10,[Tree(20,[])])])
    >>> newnew = to_tree([10, [10, [20]]])
    >>> newnew.to_nested_list()
    [10, [10, [20]]]
    >>> tree7 == newnew
    True
    """
    if len(obj) == 1:
        return Tree(obj[0], [])
    else:
        subtree = []
        for i in obj[1:]:
            subtree += [to_tree(i)]

        return Tree(obj[0], subtree)

##############################################################################
# Task 3: Binary trees
##############################################################################


class BinaryTree:
    """A class representing a binary tree.

    A binary tree is either empty, or a root connected to
    a *left* binary tree and a *right* binary tree (which could be empty).

    === Private Attributes ===
    @type _root: object | None
    @type _left: BinaryTree | None
    @type _right: BinaryTree | None

    === Representation Invariants ===
    _root, _left, _right are either ALL None, or none of them are None.
      If they are all None, this represents an empty BinaryTree.
    """
    def __init__(self, root, left, right):
        """Initialise a new binary tree with the given values.

        If <root> is None, this represents an empty BinaryTree
        (<left> and <right> are ignored in this case).

        Precondition: if <root> is not None, then neither <left> nor <right>
                      are None.

        @type self: BinaryTree
        @type root: object | None
        @type left: object | None
        @type right: object | None
        @rtype: None
        """
        if root is None:
            # store an empty BinaryTree
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = left
            self._right = right

    def is_empty(self):
        """Return True if this binary tree is empty.

        Note that only empty binary trees can have left and right
        attributes set to None.

        @type self: BinaryTree
        @rtype: bool
        """
        return self._root is None

    def preorder(self):
        """Return a list of this tree's items using a *preorder* traversal.

        @type self: BinaryTree
        @rtype: list
        >>> empty = BinaryTree(None,None,None)
        >>> C = BinaryTree('C', empty, empty)
        >>> E = BinaryTree('E', empty,empty)
        >>> H = BinaryTree('H', empty,empty)
        >>> D = BinaryTree('D', C, E)
        >>> I = BinaryTree('I', H, empty)
        >>> A = BinaryTree('A',empty,empty)
        >>> B = BinaryTree('B', A, D)
        >>> G = BinaryTree('G', empty, I)
        >>> F = BinaryTree('F', B, G)
        >>> F.preorder()
        ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
        """

        if self.is_empty():
            return []
        else:
            re = [self._root]
            re += self._left.preorder()
            re += self._right.preorder()
            return re

    def inorder(self):
        """Return a list of this tree's items using an *inorder* traversal.

        @type self: BinaryTree
        @rtype: list
        >>> empty = BinaryTree(None,None,None)
        >>> C = BinaryTree('C', empty, empty)
        >>> E = BinaryTree('E', empty,empty)
        >>> H = BinaryTree('H', empty,empty)
        >>> D = BinaryTree('D', C, E)
        >>> I = BinaryTree('I', H, empty)
        >>> A = BinaryTree('A',empty,empty)
        >>> B = BinaryTree('B', A, D)
        >>> G = BinaryTree('G', empty, I)
        >>> F = BinaryTree('F', B, G)
        >>> F.inorder()
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        """
        if self.is_empty():
            return []
        else:
            return self._left.inorder() + [self._root] + self._right.inorder()

    def postorder(self):
        """Return a list of this tree's items using a *postorder* traversal.

        @type self: BinaryTree
        @rtype: list
       list
        >>> empty = BinaryTree(None,None,None)
        >>> C = BinaryTree('C', empty, empty)
        >>> E = BinaryTree('E', empty,empty)
        >>> H = BinaryTree('H', empty,empty)
        >>> D = BinaryTree('D', C, E)
        >>> I = BinaryTree('I', H, empty)
        >>> A = BinaryTree('A',empty,empty)
        >>> B = BinaryTree('B', A, D)
        >>> G = BinaryTree('G', empty, I)
        >>> F = BinaryTree('F', B, G)
        >>> F.postorder()
        ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']
        """
        if self.is_empty():
            return []
        else:
            return self._left.postorder() + \
                   self._right.postorder() + [self._root]


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='pylintrc.txt')
