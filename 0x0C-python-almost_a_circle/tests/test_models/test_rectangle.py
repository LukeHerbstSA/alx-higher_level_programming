#!/usr/bin/python3
"""
unittest for rectangle object
"""
import unittest
import rectangle

class testrectangle(unittest.testcase):
	def test_normal(self):
		b1 = Rectangle(10, 10, 10, 10)
		self.assertequal(b1.width, 10)
		self.assertequal(b1.height, 10)
		self.assertequal(b1.x, 10)
		self.assertequal(b1.y, 10)
		self.assertequal(b1, "[Rectangle] ({}) {}/{} - {}/{}".format(b1.id, b1.x, b1.y, b1.width, b1.height))
		self.assertequalstr((b1), "[Rectangle] ({}) {}/{} - {}/{}".format(b1.id, b1.x, b1.y, b1.width, b1.height))
		self.assertequal(b1.area(), 100)

	def test_badwidth(self):
		Rectangle.validator(["hey", 10, 10, 10])

	def test_badheight(self):
		b1 = Rectangle(10, "hey", 10, 10)

	def test_badx(self):
		b1 = Rectangle(10, 10, "hey", 10)

	def test_bady(self):
		b1 = Rectangle(10, 10, 10, "hey")
