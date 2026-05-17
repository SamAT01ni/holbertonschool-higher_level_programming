#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def max_at_end(self):
        self.assertEqual(max_integer([1, 3, 5, 7]), 7)
    def max_at_beginning(self):
        self.assertEqual(max_integer([7, 5, 3, 1]), 7)
    def max_in_middle(self):
        self.assertEqual(max_integer([1, 7, 3, 5]), 7)
    def one_negative(self):
        self.assertEqual(max_integer([1, -3, 5, 7]), 7)
    def only_negative(self):
        self.assertEqual(max_integer([-1, -3, -5, -7]), -1)
    def one_element(self):
        self.assertEqual(max_integer([7]), 7)
    def empty(self):
        self.assertIsNone(max_integer([]))
