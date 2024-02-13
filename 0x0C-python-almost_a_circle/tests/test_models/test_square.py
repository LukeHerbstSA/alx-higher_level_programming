#!/usr/bin/python3
"""
unittest for rectangle object
"""
import unittest
Square = __import__("square").Square


class testsquare(unittest.TestCase):
        """
        class testsquare tests inst of rectangle
        """
        def test_normal(self):
                b1 = Square(10, 10, 10, 10)
                self.assertEqual(b1.width, 10, "width incorrectly set for inst")
                self.assertEqual(b1.height, 10, "height incorrectly set for inst")
                self.assertEqual(b1.x, 10, "x incorrectly set for inst")
                self.assertEqual(b1.y, 10, "y incorrectly set for inst")
		self.assertEqualstr(str(b1), "[Square] ({}) {}/{} - {}".format(b1.id, b1.x, b1.y, b1.width), "incorrect str repr"))
                self.assertEqualstr(b1, "[Square] ({}) {}/{} - {}".format(b1.id, b1.x, b1.y, b1.width), "incorrect str repr"))
                self.assertEqual(b1.area(), 100, "invalid area returned")

        def test_badwidth(self):
                with self.assertRaises(TypeError):
                        b1 = Square(["hey", 10, 10])

	def test_badwidthval(self):
		with self.assertRaises(ValueError):
			b1 = Square(-1, 10, 10)

        def test_badx(self):
                with self.assertRaises(TypeError):
                        b1 = Square(10, "hey", 10)

        def test_bady(self):
                with self.assertRaises(TypeError):
                        b1 = Square(10, 10, "hey")
