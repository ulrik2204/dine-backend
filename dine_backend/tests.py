"""Dummy test"""
from django.test import TestCase


class TestTemplate(TestCase):
    """This is how you create a test with django"""

    def test_somethnin(self):
        """A dummy test method"""
        actual = 10
        expected = 10
        self.assertEqual(actual, expected)
