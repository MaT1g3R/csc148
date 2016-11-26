""" Tests the missing cases from ex7_test.py

=== Credits ===
Allan Chang
Piyush Datta
Marvin Chui
"""
import unittest
from hypothesis import given
from hypothesis.strategies import *
from ex7 import *


class KthSmallestTest(unittest.TestCase):
    """Test function <kth_smallest()>"""
    @given(lists(integers(), min_size=1, max_size=1000, unique=True))
    @given(integers(min_value=0, max_value=100))
    def test_index_error(self, lst, k_shift):
        """Test index error given list input changes, <k> changes

        Tests index error

        200 examples will be tested. Should be: 10+ <k> >= len(list), 10+ <k> < 0.

        === Parameters and Return Types ===

        @type self: KthSmallestTest
        @type lst: list
            use <lst> as a parameter for <kth_smallest()>
        @type k_shift: int
            <k> is -1-<k_shift> and len(lst) + <k_shift>
            use <k> as a parameter for <kth_smallest()>
        @rtype: None
        """
        self.assertRaises(IndexError, kth_smallest, lst, -1 - k_shift)
        self.assertRaises(IndexError, kth_smallest, lst, len(lst) + k_shift)

    @given(integers(min_value=-5, max_value=100))
    def test_index_error_edge(self, k):
        """Test [] input given different <k> parameter

        Tests edge case []

        200 examples will be tested. Should be: 5+ below 0, 5+ >= 0.

        === Parameters and Return Types ===

        @type self: KthSmallestTest
        @type k: int
            use <k> as a parameter for <kth_smallest()>
        @rtype: None
        """
        self.assertRaises(IndexError, kth_smallest, [], k)

    @given(lists(integers(), min_size=1, max_size=1000, unique=True))
    @given(integers())
    def test_mutation(self, lst, k_mod):
        """Test list mutation given different [k] and list sizes

        Tests input mutation

        200 examples will be tested. Should be: 5+ different k, 5+ different list sizes.

        === Parameters and Return Types ===

        @type self: KthSmallestTest
        @type lst: list
            use <lst> as a parameter for <kth_smallest()>
        @type k_mod: int
            <k> = <k_mod> % len(lst)
            use <k> as a parameter for <kth_smallest()>
        @rtype: None
        """
        new_lst = list(lst)
        new_k = k_mod % len(lst)
        kth_smallest(new_lst, new_k)
        self.assertEqual(lst, new_lst)


class AnagramsTest(unittest.TestCase):
    """Test function <anagrams()>"""
    def test_no_solution(self):
        """Test an input that results in 0 solutions

        Tests str input, empty list return

        6 chosen examples will be tested.

        === Parameters and Return Types ===

        @type self: AnagramsTest
        @rtype: None
        """
        self.assertEqual(anagrams('meet'), [])
        self.assertEqual(anagrams('boilingz'), [])
        self.assertEqual(anagrams('cerztain'), [])
        self.assertEqual(anagrams('windowpqwe'), [])
        self.assertEqual(anagrams('asdf'), [])
        self.assertEqual(anagrams('comitteee'), [])

    def test_possible_solution(self):
        """Test an input that results in 1+ solutions

        Tests str input, list[str] return, str in alpha order

        10 examples will be tested. 5+ examples should test alphabetical order.

        === Parameters and Return Types ===

        @type self: AnagramsTest
        @rtype: None
        """
        self.assertEqual(anagrams("destruction"), ['credit nut so',
                                                   'credit so nut',
                                                   'credit sun to',
                                                   'credit to sun',
                                                   'destruction',
                                                   'dust not rice',
                                                   'dust rice not',
                                                   'not dust rice',
                                                   'not rice dust',
                                                   'nut credit so',
                                                   'nut so credit',
                                                   'rice dust not',
                                                   'rice not dust',
                                                   'so credit nut',
                                                   'so nut credit',
                                                   'sun credit to',
                                                   'sun to credit',
                                                   'to credit sun',
                                                   'to sun credit'])
        self.assertEqual(anagrams("distribution"), ['bit dust i in or', 'bit dust i iron', 'bit dust i or in', 'bit dust in i or', 'bit dust in or i', 'bit dust iron i', 'bit dust or i in', 'bit dust or in i', 'bit i dust in or', 'bit i dust iron', 'bit i dust or in', 'bit i in dust or', 'bit i in or dust', 'bit i iron dust', 'bit i or dust in', 'bit i or in dust', 'bit in dust i or', 'bit in dust or i', 'bit in i dust or', 'bit in i or dust', 'bit in or dust i', 'bit in or i dust', 'bit iron dust i', 'bit iron i dust', 'bit or dust i in', 'bit or dust in i', 'bit or i dust in', 'bit or i in dust', 'bit or in dust i', 'bit or in i dust', 'burst do i i tin', 'burst do i tin i', 'burst do tin i i', 'burst i do i tin', 'burst i do tin i', 'burst i i do tin', 'burst i i tin do', 'burst i tin do i', 'burst i tin i do', 'burst tin do i i', 'burst tin i do i', 'burst tin i i do', 'distribution', 'do burst i i tin', 'do burst i tin i', 'do burst tin i i', 'do i burst i tin', 'do i burst tin i', 'do i i burst tin', 'do i i tin burst', 'do i tin burst i', 'do i tin i burst', 'do tin burst i i', 'do tin i burst i', 'do tin i i burst', 'dust bit i in or', 'dust bit i iron', 'dust bit i or in', 'dust bit in i or', 'dust bit in or i', 'dust bit iron i', 'dust bit or i in', 'dust bit or in i', 'dust i bit in or', 'dust i bit iron', 'dust i bit or in', 'dust i in bit or', 'dust i in or bit', 'dust i iron bit', 'dust i or bit in', 'dust i or in bit', 'dust in bit i or', 'dust in bit or i', 'dust in i bit or', 'dust in i or bit', 'dust in or bit i', 'dust in or i bit', 'dust iron bit i', 'dust iron i bit', 'dust or bit i in', 'dust or bit in i', 'dust or i bit in', 'dust or i in bit', 'dust or in bit i', 'dust or in i bit', 'i bit dust in or', 'i bit dust iron', 'i bit dust or in', 'i bit in dust or', 'i bit in or dust', 'i bit iron dust', 'i bit or dust in', 'i bit or in dust', 'i burst do i tin', 'i burst do tin i', 'i burst i do tin', 'i burst i tin do', 'i burst tin do i', 'i burst tin i do', 'i do burst i tin', 'i do burst tin i', 'i do i burst tin', 'i do i tin burst', 'i do tin burst i', 'i do tin i burst', 'i dust bit in or', 'i dust bit iron', 'i dust bit or in', 'i dust in bit or', 'i dust in or bit', 'i dust iron bit', 'i dust or bit in', 'i dust or in bit', 'i i burst do tin', 'i i burst tin do', 'i i do burst tin', 'i i do tin burst', 'i i tin burst do', 'i i tin do burst', 'i in bit dust or', 'i in bit or dust', 'i in dust bit or', 'i in dust or bit', 'i in or bit dust', 'i in or dust bit', 'i iron bit dust', 'i iron dust bit', 'i or bit dust in', 'i or bit in dust', 'i or dust bit in', 'i or dust in bit', 'i or in bit dust', 'i or in dust bit', 'i tin burst do i', 'i tin burst i do', 'i tin do burst i', 'i tin do i burst', 'i tin i burst do', 'i tin i do burst', 'in bit dust i or', 'in bit dust or i', 'in bit i dust or', 'in bit i or dust', 'in bit or dust i', 'in bit or i dust', 'in dust bit i or', 'in dust bit or i', 'in dust i bit or', 'in dust i or bit', 'in dust or bit i', 'in dust or i bit', 'in i bit dust or', 'in i bit or dust', 'in i dust bit or', 'in i dust or bit', 'in i or bit dust', 'in i or dust bit', 'in or bit dust i', 'in or bit i dust', 'in or dust bit i', 'in or dust i bit', 'in or i bit dust', 'in or i dust bit', 'iron bit dust i', 'iron bit i dust', 'iron dust bit i', 'iron dust i bit', 'iron i bit dust', 'iron i dust bit', 'or bit dust i in', 'or bit dust in i', 'or bit i dust in', 'or bit i in dust', 'or bit in dust i', 'or bit in i dust', 'or dust bit i in', 'or dust bit in i', 'or dust i bit in', 'or dust i in bit', 'or dust in bit i', 'or dust in i bit', 'or i bit dust in', 'or i bit in dust', 'or i dust bit in', 'or i dust in bit', 'or i in bit dust', 'or i in dust bit', 'or in bit dust i', 'or in bit i dust', 'or in dust bit i', 'or in dust i bit', 'or in i bit dust', 'or in i dust bit', 'tin burst do i i', 'tin burst i do i', 'tin burst i i do', 'tin do burst i i', 'tin do i burst i', 'tin do i i burst', 'tin i burst do i', 'tin i burst i do', 'tin i do burst i', 'tin i do i burst', 'tin i i burst do', 'tin i i do burst'])
        self.assertEqual(anagrams("experience"), ['experience'])
        self.assertEqual(anagrams("government"), ['government'])
        self.assertEqual(anagrams("instrument"), ['in stem turn', 'in turn stem', 'instrument', 'mist net run', 'mist run net', 'net mist run', 'net run mist', 'run mist net', 'run net mist', 'run stem tin', 'run tin stem', 'stem in turn', 'stem run tin', 'stem tin run', 'stem turn in', 'tin run stem', 'tin stem run', 'turn in stem', 'turn stem in'])
        self.assertEqual(anagrams("ironjewel"), ['in jewel or', 'in or jewel', 'iron jewel', 'jewel in or', 'jewel iron', 'jewel or in', 'or in jewel', 'or jewel in'])
        self.assertEqual(anagrams("kissknee"), ['kiss knee', 'knee kiss'])
        self.assertEqual(anagrams("liftlimit"), ['lift limit', 'limit lift'])
        self.assertEqual(anagrams("orangerice"), ['go near rice', 'go rice near', 'ice or range', 'ice range or', 'near go rice', 'near rice go', 'or ice range', 'or range ice', 'orange rice', 'range ice or', 'range or ice', 'rice go near', 'rice near go', 'rice orange'])
        self.assertEqual(anagrams("aaaaa"), ["a a a a a"])

if __name__ == '__main__':
    unittest.main(exit=False)
