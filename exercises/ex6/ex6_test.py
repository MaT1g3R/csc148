"""CSC148 Exercise 6: Binary Search Trees

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Exercise 6.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests and to be confident your code is correct.

For more information on hypothesis (one of the testing libraries we're using),
please see
<http://www.teach.cs.toronto.edu/~csc148h/fall/software/hypothesis.html>.

Note: this file is for support purposes only, and is not part of your
submission.
"""
import unittest
from ex6 import BinarySearchTree

deep1 = BinarySearchTree(5)
deep2 = BinarySearchTree(25)
deep3 = BinarySearchTree(66)
deep4 = BinarySearchTree(80)
deep5 = BinarySearchTree(92)
deep6 = BinarySearchTree(111)
deep7 = BinarySearchTree(166)
deep8 = BinarySearchTree(200)

mid1 = BinarySearchTree(20)
mid1._left = deep1
mid1._right = deep2
mid2 = BinarySearchTree(75)
mid2._left = deep3
mid2._right = deep4
mid3 = BinarySearchTree(95)
mid3._left = deep5
mid3._right = deep6
mid4 = BinarySearchTree(175)
mid4._left = deep7
mid4._right = deep8

s1 = BinarySearchTree(50)
s1._left = mid1
s1._right = mid2
s2 = BinarySearchTree(150)
s2._left = mid3
s2._right = mid4

tree = BinarySearchTree(90)
tree._left = s1
tree._right = s2


class BSTNumLessThanTest(unittest.TestCase):
    def test_one(self):
        bst = BinarySearchTree(1)
        self.assertEqual(bst.num_less_than(10), 1)
        self.assertEqual(bst.num_less_than(0), 0)

    def test_bigger(self):
        bst = BinarySearchTree(1)
        bst._left = BinarySearchTree(-10)
        bst._right = BinarySearchTree(100)
        self.assertEqual(bst.num_less_than(5), 2)
        self.assertEqual(bst.num_less_than(-100), 0)
        self.assertEqual(bst.num_less_than(1000), 3)

    def test_huge(self):
        self.assertEqual(tree.num_less_than(50), 3)
        self.assertEqual(tree.num_less_than(90), 7)
        self.assertEqual(tree.num_less_than(95), 9)
        self.assertEqual(tree.num_less_than(-1), 0)


class BSTItemsTest(unittest.TestCase):
    def test_one(self):
        bst = BinarySearchTree(1)
        self.assertEqual(bst.items_at_depth(1), [1])

    def test_empty(self):
        bst = BinarySearchTree(None)
        self.assertEqual(bst.items_at_depth(1), [])

    def test_huge(self):
        self.assertEqual(tree.items_at_depth(1), [90])
        self.assertEqual(tree.items_at_depth(2), [50, 150])
        self.assertEqual(tree.items_at_depth(3), [20, 75, 95, 175])
        self.assertEqual(tree.items_at_depth(4), [5, 25, 66, 80, 92, 111, 166, 200])




class BSTLevelsTest(unittest.TestCase):

    def test_one(self):
        bst = BinarySearchTree(1)
        self.assertEqual(bst.levels(), [(1, [1])])

    def test_huge(self):
        self.assertEqual(tree.levels(), [(1, [90]), (2, [50, 150]), (3, [20, 75, 95, 175]), (4, [5, 25, 66, 80, 92, 111, 166, 200])])

if __name__ == '__main__':
    unittest.main(exit=False)
