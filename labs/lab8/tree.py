"""Lab 8: Trees and Recursion, Tasks 1 & 2

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains a few Tree methods that you should implement recursively.
Make sure you understand both the theoretical idea of trees, as well as how
we represent them in our Tree class.
"""
import random  # For Task 2


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
        """Initialize a new Tree with the given root value and subtrees.

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

    def __len__(self):
        """Return the number of nodes contained in this tree.

        @type self: Tree
        @rtype: int
        """
        if self.is_empty():
            return 0
        else:
            size = 1
            for subtree in self._subtrees:
                size += subtree.__len__()  # Could also do size += len(subtree)
            return size

    def count(self, item):
        """Return the number of occurrences of <item> in this tree.

        @type self: Tree
        @type item: object
        @rtype: int
        """
        if self.is_empty():
            return 0
        else:
            num = 0
            if self._root == item:
                num += 1
            for subtree in self._subtrees:
                num += subtree.count(item)
            return num

    # ------------------------------------------------------------------------
    # Lab Exercises
    # ------------------------------------------------------------------------
    def __contains__(self, item):
        """Return whether <item> is in this tree.

        @type self: Tree
        @type item: object
        @rtype: bool

        >>> t = Tree(1, [Tree(2, []), Tree(5, [])])
        >>> 1 in t  # Same as t.__contains__(1)
        True
        >>> 5 in t
        True
        >>> 4 in t
        False
        """
        if self.is_empty():
            return False
        elif self._root == item:
            return True
        else:
            for i in self._subtrees:
                if item in i:
                    return True

    def leaves(self):
        """Return a list of all of the leaf items in the tree.

        @type self: Tree
        @rtype: list

        >>> Tree(None, []).leaves()
        []
        >>> t = Tree(1, [Tree(2, []), Tree(5, [])])
        >>> t.leaves()
        [2, 5]
        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t.leaves()
        [4, 5, 6, 7]
        """
        if self.is_empty():
            return []
        elif self._subtrees == []:
            return [self._root]
        else:
            r = []
            for i in self._subtrees:
                r += (i.leaves())
            return r

    def branching_factor(self):
        """Return the average branching factor of this tree.

        Remember to ignore all 0's coming from leaves in this calculation.

        Return 0 if this tree is empty or consists of just a single root node.

        @type self: Tree
        @rtype: float

        >>> Tree(None, []).branching_factor()
        0.0
        >>> t = Tree(1, [Tree(2, []), Tree(5, [])])
        >>> t.branching_factor()
        2.0
        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t.branching_factor()
        3.0
        """
        if self._branching_factor_helper()[1] == 0:
            return 0.0
        else:
            return self._branching_factor_helper()[0] / \
                   self._branching_factor_helper()[1]

    def _branching_factor_helper(self):
        """Return a tuple (x,y) where:

        x is the total branching factor of all non-leaf nodes in this tree, and
        y is the total number of non-leaf nodes in this tree.

        @type self: Tree
        @rtype: (int, int)
        """
        if self.is_empty() or self._subtrees == []:
            return [0, 0]
        else:
            non_leaves = 1
            branches = len(self._subtrees)
            for i in self._subtrees:
                branches += i._branching_factor_helper()[0]
                non_leaves += i._branching_factor_helper()[1]
            return branches, non_leaves

    def insert(self, item):
        """Insert <item> into this tree using the following algorithm.

          1. If the tree is empty, <item> is the new root of the tree.
          2. If the tree has a root but no subtrees, create a
             new tree containing the item, and make this new tree a subtree
             of the original tree.
          3. Otherwise, pick a random number between 1 and 3 inclusive.
             - If the random number is 3, create a new tree containing
               the item, and make this new tree a subtree of the original.
             - If the random number is a 1 or 2, pick one of the existing
               subtrees at random, and *recursively insert* the new item
               into that subtree.

        @type self: Tree
        @type item: object
        @rtype: None

        >>> t = Tree(None, [])
        >>> t.insert(1)
        >>> 1 in t
        True
        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t.insert(100)
        >>> 100 in t
        True
        """
        # Use the function randint as follows:
        # >>> random.randint(1, 3)
        # 2  # Randomly returns 1, 2, or 3

        if self.is_empty():
            self._root = item
        elif self._subtrees == []:
            self._subtrees.append(Tree(item, []))
        else:
            rng = random.randint(1, 3)
            if rng == 3:
                self._subtrees.append(Tree(item, []))
            else:
                sub_tree_inserting = random.choice(self._subtrees)
                sub_tree_inserting._insert_child(item, sub_tree_inserting._root)

    def _insert_child(self, item, parent):
        """Insert <item> into this tree as a child of <parent>.

        If successful, return True. If <parent> is not in the
        tree, return False.

        @type self: Tree
        @type item: object
        @type parent: object
        @rtype: bool
        """
        if parent not in self:
            return False
        else:
            self._subtrees.append(Tree(item, []))
            return True

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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
