"""Assignment 2 - Tests

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains sample tests for Assignment 2, Tasks 1 and 2.
Note that the data set here is a pretty small one, but should be enough to
give you an idea of how we could test your code.

NOTE:
    - If using PyCharm, go into your Settings window, and go to
      Editor -> General.
      Make sure the "Ensure line feed at file end on Save" is NOT checked.
      Then, make sure none of the example files have a blank line at the end.
      (If they do, the data size will be off.)
"""
import os

import unittest
from hypothesis import given
from hypothesis.strategies import integers, lists, recursive, builds, text, just

from tree_data import FileSystemTree


# This should be the path to the "B" folder in the sample data.
# You may need to modify this, depending on where you downloaded and
# extracted the files.
EXAMPLE_PATH = os.path.join('example-data', 'B')


class FileSystemTreeConstructorTest(unittest.TestCase):
    def test_single_file(self):
        tree = FileSystemTree(os.path.join(EXAMPLE_PATH, 'f4.txt'))
        self.assertEqual(tree._root, 'f4.txt')
        self.assertEqual(tree._subtrees, [])
        self.assertIs(tree._parent_tree, None)

        self.assertEqual(tree.data_size, 10)

        # Check colours
        for i in range(3):
            self.assertGreaterEqual(tree.colour[i], 0)
            self.assertLessEqual(tree.colour[i], 255)

    def test_example_data_basic(self):
        tree = FileSystemTree(EXAMPLE_PATH)
        self.assertEqual(tree._root, 'B')
        self.assertIs(tree._parent_tree, None)

        self.assertEqual(tree.data_size, 40)

        # Check colours
        for i in range(3):
            self.assertGreaterEqual(tree.colour[i], 0)
            self.assertLessEqual(tree.colour[i], 255)

    def test_example_data_parent_tree_of_subtrees(self):
        tree = FileSystemTree(EXAMPLE_PATH)

        self.assertEqual(len(tree._subtrees), 2)

        for subtree in tree._subtrees:
            # Note the use of assertIs rather than assertEqual.
            # This checks ids rather than values.
            self.assertIs(subtree._parent_tree, tree)

    def test_example_data_subtree_order(self):
        """NOTE: the order of the subtrees for a FileSystemTree object
        *must* match the order of the items returned by os.listdir.
        """
        tree = FileSystemTree(EXAMPLE_PATH)

        self.assertEqual(len(tree._subtrees), 2)
        first, second = tree._subtrees

        self.assertEqual(first._root, 'A')
        self.assertEqual(len(first._subtrees), 3)
        self.assertEqual(first.data_size, 30)

        self.assertEqual(second._root, 'f4.txt')
        self.assertEqual(second._subtrees, [])
        self.assertEqual(second.data_size, 10)


class GenerateTreemapTest(unittest.TestCase):
    @given(integers(min_value=100, max_value=1000),
           integers(min_value=100, max_value=1000),
           integers(min_value=100, max_value=1000),
           integers(min_value=100, max_value=1000))
    def test_single_file(self, x, y, width, height):
        tree = FileSystemTree(os.path.join(EXAMPLE_PATH, 'f4.txt'))
        rects = tree.generate_treemap((x, y, width, height))

        # This should be just a single rectangle and colour returned
        self.assertEqual(len(rects), 1)
        rect, colour = rects[0]
        self.assertEqual(rect, (x, y, width, height))

        for i in range(3):
            self.assertGreaterEqual(colour[i], 0)
            self.assertLessEqual(colour[i], 255)

    def test_example_data(self):
        tree = FileSystemTree(EXAMPLE_PATH)
        rects = tree.generate_treemap((0, 0, 800, 1000))

        # This should be one rectangle per file in 'B'.
        self.assertEqual(len(rects), 4)

        # Here, we illustrate the correct order of the returned rectangle.
        # Note that this again corresponds to the order in which os.listdir
        # reports the contents of a folder.
        rect_f1 = rects[0][0]
        rect_f2 = rects[1][0]
        rect_f3 = rects[2][0]
        rect_f4 = rects[3][0]

        self.assertEqual(rect_f1, (0, 0, 400, 750))
        # Note the rounding down on f2.
        self.assertEqual(rect_f2, (400, 0, 133, 750))
        # Note that f3 has a width of 267, to bring the total width of
        # the 'A' rectangle to exactly 800.
        self.assertEqual(rect_f3, (533, 0, 267, 750))

        self.assertEqual(rect_f4, (0, 750, 800, 250))


if __name__ == '__main__':
    unittest.main(exit=False)
