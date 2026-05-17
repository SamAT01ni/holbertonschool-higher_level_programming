#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 3, 5, 7]), 7)
    def test_max_at_beginning(self):
        self.assertEqual(max_integer([7, 5, 3, 1]), 7)
    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 7, 3, 5]), 7)
    def test_one_negative(self):
        self.assertEqual(max_integer([1, -3, 5, 7]), 7)
    def test_only_negative(self):
        self.assertEqual(max_integer([-1, -3, -5, -7]), -1)
    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)
    def test_empty(self):
        self.assertIsNone(max_integer([]))
