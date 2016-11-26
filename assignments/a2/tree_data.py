"""Assignment 2: Trees for Treemap

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the basic tree interface required by the treemap
visualiser. You will both add to the abstract class, and complete a
concrete implementation of a subclass to represent files and folders on your
computer's file system.
"""
import os
from random import randint
import math


class AbstractTree:
    """A tree that is compatible with the treemap visualiser.

    This is an abstract class that should not be instantiated directly.

    You may NOT add any attributes, public or private, to this class.
    However, part of this assignment will involve you adding and implementing
    new public *methods* for this interface.

    === Public Attributes ===
    @type data_size: int
        The total size of all leaves of this tree.
    @type colour: (int, int, int)
        The RGB colour value of the root of this tree.
        Note: only the colours of leaves will influence what the user sees.

    === Private Attributes ===
    @type _root: obj | None
        The root value of this tree, or None if this tree is empty.
    @type _subtrees: list[AbstractTree]
        The subtrees of this tree.
    @type _parent_tree: AbstractTree | None
        The parent tree of this tree; i.e., the tree that contains this tree
        as a subtree, or None if this tree is not part of a larger tree.

    === Representation Invariants ===
    - data_size >= 0
    - If _subtrees is not empty, then data_size is equal to the sum of the
      data_size of each subtree.
    - colour's elements are in the range 0-255.

    - If _root is None, then _subtrees is empty, _parent_tree is None, and
      data_size is 0.
      This setting of attributes represents an empty tree.
    - _subtrees IS allowed to contain empty subtrees (this makes deletion
      a bit easier).

    - if _parent_tree is not empty, then self is in _parent_tree._subtrees
    """
    def __init__(self, root, subtrees, data_size=0):
        """Initialize a new AbstractTree.

        If <subtrees> is empty, <data_size> is used to initialize this tree's
        data_size. Otherwise, the <data_size> parameter is ignored,
         and this tree's
        data_size is computed from the data_sizes of the subtrees.

        If <subtrees> is not empty, <data_size> should not be specified.

        This method sets the _parent_tree attribute for each subtree to self.

        A random colour is chosen for this tree.

        Precondition: if <root> is None, then <subtrees> is empty.

        @type self: AbstractTree
        @type root: object
        @type subtrees: list[AbstractTree]
        @type data_size: int
        @rtype: None
        """
        self._root = root
        self._subtrees = subtrees
        self._parent_tree = None

        self.colour = (randint(0, 255),
                       randint(0, 255),
                       randint(0, 255))

        if self._subtrees == []:
            self.data_size = data_size
        else:
            self.data_size = 0
            for t in self._subtrees:
                self.data_size += t.data_size

        for t in self._subtrees:
            t._parent_tree = self

        # Make sure no dupelicate colours happen
        if self._subtrees != []:
            while self.colour in self._exclude_colors():
                self.colour = (randint(0, 255),
                               randint(0, 255),
                               randint(0, 255))

    def _exclude_colors(self):
        """ Return all colours in all subtrees
        @type self: AbstractTree
        @rtype: list[(int, int, int)]
        """
        if self._subtrees == []:
            return [self.colour]
        else:
            r = []
            for s in self._subtrees:
                r += [s.colour]
                r += s._exclude_colors()
            return r + [(0, 0, 0)]

    def is_empty(self):
        """Return True if this tree is empty.

        @type self: AbstractTree
        @rtype: bool
        """
        return self._root is None

    def generate_treemap(self, rect):
        """Run the treemap algorithm on this tree and return the rectangles.

        Each returned tuple contains a pygame rectangle and a colour:
        ((x, y, width, height), (r, g, b)).

        One tuple should be returned per non-empty leaf in this tree.

        @type self: AbstractTree
        @type rect: (int, int, int, int)
            Input is in the pygame format: (x, y, width, height)
        @rtype: list[((int, int, int, int), (int, int, int))]
        """
        if self.is_empty():
            pass
        elif self._subtrees == []:
            return [(rect, self.colour)]
        else:
            treemaps = []
            x, y, width, height = rect
            big_x = x
            big_y = y

            for i in range(len(self._subtrees)):
                if self._subtrees[i].data_size > 0:  # empty folders are ignored
                    ratio = self._subtrees[i].data_size/self.data_size
                    if width > height:

                        small_w = math.floor(width*ratio)
                        treemaps += self._subtrees[i].generate_treemap(
                            (x, y, small_w, height))
                        x += small_w
                        size_fixing_w(treemaps, width)

                    else:
                        small_h = math.floor(height * ratio)
                        treemaps += self._subtrees[i].generate_treemap(
                            (x, y, width, small_h))
                        y += small_h
                        size_fixing_h(treemaps, height)

            return treemaps

    def get_separator(self):
        """Return the string used to separate nodes in the string
        representation of a path from the tree root to a leaf.

        Used by the treemap visualiser to generate a string displaying
        the items from the root of the tree to the currently selected leaf.

        This should be overridden by each AbstractTree subclass, to customize
        how these items are separated for different data domains.

        @type self: AbstractTree
        @rtype: str
        """
        raise NotImplementedError

    # Debugging purposes only
    # def to_nested_list(self):
    #     """Return the nested list representation of this tree.
    #
    #     @type self: Tree
    #     @rtype: list
    #     """
    #     if len(self._subtrees) == 0:
    #         return [self._root]
    #     else:
    #         nested = [self._root]
    #         for subtree in self._subtrees:
    #             nested.append(subtree.to_nested_list())
    #         return nested

    def get_item_by_color(self, color):
        """ return the item with the color <color>
        @type self: AbstractTree
        @type color: tuple(int, int, int)
            the color that the user inputs
        @rtype: AbstractTree
            return the AbstractTree with the color <color>
        """

        if self.is_empty():
            pass
        elif self.colour == color and self._subtrees == []:
            return self
        else:
            for s in self._subtrees:
                if s.get_item_by_color(color) is not None:
                    return s.get_item_by_color(color)

    def re_calculate_size(self, change):
        """ re calculate the size of everything
        This method mutate tree sizes
        @type self: AbstractTree
        @type change: int
            the change in size, can be positive or negative
        @rtype: None
        """
        if self._parent_tree is None:
            self.data_size += change
        else:
            self.data_size += change
            self._parent_tree.re_calculate_size(change)

    def delete_item(self, item):
        """ delete item from the tree
        @type self: AbstractTree
        @type item: AbstractTree
            item to be deleted
        @rtype: None
        """
        if self._parent_tree is None:
            pass
        elif self == item:
            self._root = None
            self._subtrees = []
            self._parent_tree = None
        else:
            for s in self._subtrees:
                s.delete_item(item)

    def get_path_helper(self):
        """ format path for self and return it in a list
        @type self: AbstractTree
        @rtype: list[str]
        """
        if self._parent_tree is None:
            return [self._root]
        else:
            return self._parent_tree.get_path_helper() + [self._root]

    def get_path_and_size(self):
        """ return the full path of item in a string
        @type self: AbstractTree
        @rtype: str
            used to be displayed in the pygame window
        """
        return self.get_separator().join(self.get_path_helper()) +\
            ' ({})'.format(self.data_size)


class FileSystemTree(AbstractTree):
    """A tree representation of files and folders in a file system.

    The internal nodes represent folders, and the leaves represent regular
    files (e.g., PDF documents, movie files, Python source code files, etc.).

    The _root attribute stores the *name* of the folder or file, not its full
    path. E.g., store 'assignments', not '/Users/David/csc148/assignments'

    The data_size attribute for regular files as simply the size of the file,
    as reported by os.path.getsize.
    """
    def __init__(self, path):
        """Store the file tree structure contained in the given file or folder.

        Precondition: <path> is a valid path for this computer.

        @type self: FileSystemTree
        @type path: str
        @rtype: None
        """

        if not os.path.isdir(path):
            AbstractTree.__init__(self, os.path.basename(path),
                                  [], os.path.getsize(path))
        else:
            subtrees = []
            for filename in os.listdir(path):
                subitem = os.path.join(path, filename)
                subtrees += [FileSystemTree(subitem)]
            AbstractTree.__init__(self, os.path.basename(path), subtrees)

    def get_separator(self):
        """ Use </> to indicate the path for the file tree
        @type self: FileSystemTree
        @rtype: str
        """
        return '/'


def size_fixing_h(treemaps, passed_in_height):
    """size fixing helper for height
    @type treemaps: list[((int, int, int, int), (int, int, int))]
    @type passed_in_height: int
    @rtype: None
    """
    for index in range(len(treemaps)):
        x, y, width, height = treemaps[index][0]
        color = treemaps[index][1]
        height += passed_in_height - y - height
        treemaps[index] = ((x, y, width, height), color)


def size_fixing_w(treemaps, passed_in_width):
    """size fixing helper for height
    @type treemaps: list[((int, int, int, int), (int, int, int))]
    @type passed_in_width: int
    @rtype: None
    """
    for index in range(len(treemaps)):
        x, y, width, height = treemaps[index][0]
        color = treemaps[index][1]
        width += passed_in_width - x - width
        treemaps[index] = ((x, y, width, height), color)

if __name__ == '__main__':
    import python_ta
    # Remember to change this to check_all when cleaning up your code.
    python_ta.check_all(config='pylintrc.txt')

    # mac_dir = '/Users/PeijunsMac/Desktop/csc148/assignments'
    _windr = 'A:/Python Projects/csc148 _backup'
    # _common = 'a2/tree_data.py'
    #
    tree = FileSystemTree(os.path.join(_windr))
    # print(tree.data_size)
    #
    # tree2 = FileSystemTree(_windr)
    # print(tree2.to_nested_list())
    tree.generate_treemap((0, 0, 1024, 720))
