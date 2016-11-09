class Tree:
    """A recursive tree data structure.

    Note the relationship between this class and LinkedListRec
    from Lab 5; the only major difference is that _rest
    has been replaced by _subtrees to handle multiple
    recursive sub-parts.

    === Private Attributes ===
    @type _root: object | None
        The item stored at the tree's root,
        or None if the tree is empty.
    @type _subtrees: list[Tree]
        A list of all subtrees of the tree.

    === Representation Invariants ===
    - If self._root is None then self._subtrees is empty.
      This setting of attributes represents an empty Tree.
    - self._subtrees does not contain any empty Trees.
    """
    def __init__(self, root, subtrees):
        """Initialize a new Tree with the given root value
        and subtrees.

        If <root> is None, the tree is empty.
        A new tree always has no subtrees.

        @type self: Tree
        @type root: object
        @type subtrees: list[Tree]
        @rtype: None
        """
        if root is None:
            self._root = None
            self._subtrees = None
        else:
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

        >>> t0 = Tree(10,[])
        >>> t1 = Tree(10,[t0])
        >>> len(t1)
        2
        """
        if self.is_empty():
            return 0
        else:
            size = 0
            for subtree in self._subtrees:
                size += len(subtree)
            size += 1
            return size

    def count(self, item):
        """Return the number of occurrences of <item> in this tree.

        @type item: object
        @type self: Tree
        @rtype: int
        >>> t0 = Tree(10,[])
        >>> t1 = Tree(10,[t0])
        >>> t1.count(10)
        2
        """
        if self.is_empty():
            return 0
        else:
            count = 1 if self._root == item else 0
            for subtree in self._subtrees:
                if item == subtree._root:
                    count += 1
            return count

    def print_tree(self, depth=0):
        """Print all of the items in this tree.

        For each node, its item is printed before any of its
        descendants' items. The output is nicely indented.

        You may find this method helpful for debugging.

        @type self: Tree
        @type depth: int
        @rtype: None

        >>> t = Tree(1, [Tree(2,[Tree(4,[])]) , Tree(3,[])])
        >>> t.print_tree()
        """
        if len(self._subtrees) == 0:
            print('  '*depth, self._root)
        else:
            print('  '*depth, self._root)
            for subtree in self._subtrees:
                subtree.print_tree(depth + 1)

    def average(self):
        """Return the average of the items in this tree.

        Return 0 if this tree is empty.

        @type self: Tree
        @rtype: float
        >>> t = Tree(1, [Tree(2,[Tree(4,[])]) , Tree(3,[])])
        >>> t.average()
        2.5
        >>> e = Tree(None, [])
        >>> e.average()
        0
        >>> sum([1, 2, 3])
        6
        """
        if self.is_empty():
            return 0
        else:
            return self.sum()/len(self)

    def sum(self):
        """ return sum of the tree
        @type self: Tree
        @rtype: int
        """
        if self.is_empty():
            return 0
        else:
            s = self._root
            for i in self._subtrees:
                s += i.sum()
            return s

    def delete_item(self, item):
        """Delete *one* occurrence of item from this tree.

        Return True if <item> was deleted, and False otherwise.
        Do not modify this tree if it does not contain <item>.

        @type self: Tree
        @type item: object
        @rtype: bool
        """
        if self.is_empty():
            return False
        elif len(self._subtrees) == 0:
            if self._root != item:  # item is not in the tree
                return False
            else:  # resulting tree should be empty
                self._root = None
                return True
        else:
            if self._root == item:
                self._delete_root()  # delete the root
                return True
            else:
                for subtree in self._subtrees:
                    deleted = subtree.delete_item(item)
                    if deleted:
                        # If the subtree is now empty, remove it.
                        # Note that removing an item from a list while looping
                        # through it is usually EXTREMELY DANGEROUS.
                        # We are only doing it because we return immediately
                        # afterwards, and so no more loop iterations occur.
                        if subtree.is_empty():
                            self._subtrees.remove(subtree)
                        # One occurrence of the item was deleted, so we're done.
                        return True
                    else:
                        # No item was deleted. Continue onto the next iteration.
                        # Note that this branch is unnecessary; we've only shown
                        # it to write comments.
                        pass

                # If we don't return inside the loop, the item is not deleted
                # from any of the subtrees. In this case, the item does not
                # appear in <self>.
                return False

    def _delete_root(self):
        """Remove the root item of this tree.

        @type self: Tree
        @rtype: None
        """
        # Get the last subtree in this tree.
        chosen_subtree = self._subtrees.pop()

        self._root = chosen_subtree._root
        self._subtrees.extend(chosen_subtree._subtrees)
