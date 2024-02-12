#!/usr/bin/python3
"""
class square
"""
import unittest
import square

class testsquare(unittest.testcase()):
	def test_normal(self):
		b1 = Square(10, 10, 10)
		self.assertequal(b1.width, 10)
                self.assertequal(b1.height, 10)
                self.assertequal(b1.x, 10)
                self.assertequal(b1.y, 10)
                self.assertequal(b1, "[Square] ({}) {}/{} - {}/{}".format(b1.id, b1.x, b1.y, b1.width, b1.height))
                self.assertequalstr((b1), "[Square] ({}) {}/{} - {}/{}".format(b1.id, b1.x, b1.y, b1.width, b1.height))
                self.assertequal(b1.area(), 100)

	test_update(self):
		b1 = Square(10, 10, 10)
		b1.update([5, 20, 0, 0], None)

	def test_badwidth(self):
                Rectangle.validator(["hey", 10, 10])

        def test_badx(self):
                b1 = Square(10, "hey", 10)

        def test_bady(self):
                b1 = Square(10, 10, "hey")
