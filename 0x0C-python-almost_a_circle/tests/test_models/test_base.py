#!/usr/bin/python3
"""
unittest for base file
"""
import unittest
Base = __import__("base").Base


class basetest(unittest.TestCase):
    """
    class basetest creates instances to test
    """
    def test_init_normal(self):
        b1 = Base()
        self.assertEqual(b1.id, 0, "incorrect id")

    def test_init_id(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10, "incorrect id")

    def test_init_neg(self):
        b1 = Base(-1)
        self.assertEqual(b1.id, -1, "incorrect id")


if __name__ == "__main__":
    unittest.main()
