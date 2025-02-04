import unittest

from algorithms.is_valid_subsequence import run as is_valid_subsequence
from algorithms.non_constructible_change import run as non_constructible_change

class TestIsValidSubsequence(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(is_valid_subsequence([1, 2, 3, 4], [2, 4]))
    def test_example_2(self):
        self.assertFalse(is_valid_subsequence([1, 2, 3, 4], [4, 2]))
    def test_example_3(self):
        self.assertTrue(is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
    def test_example_4(self):
        self.assertTrue(is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 6, -1, 8, 10]))
    def test_example_5(self):
        self.assertFalse(is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 6, -1, 8, 11]))


class TestNonConstructibleChange(unittest.TestCase):
    def test_example_1(self):
        coins = [5, 7, 1, 1, 2, 3, 22]
        expected_output = 20
        self.assertEqual(non_constructible_change(coins), expected_output)

    def test_example_2(self):
        coins = [1, 2, 5]
        expected_output = 4
        self.assertEqual(non_constructible_change(coins), expected_output)

    def test_example_3(self):
        coins = []
        expected_output = 1
        self.assertEqual(non_constructible_change(coins), expected_output)

    def test_example_4(self):
        coins = [1, 1, 1, 1, 1]
        expected_output = 6
        self.assertEqual(non_constructible_change(coins), expected_output)

    def test_example_5(self):
        coins = [1, 1, 3, 4]
        expected_output = 10
        self.assertEqual(non_constructible_change(coins), expected_output)

