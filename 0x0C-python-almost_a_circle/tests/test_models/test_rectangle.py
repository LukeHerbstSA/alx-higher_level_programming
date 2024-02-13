#!/usr/bin/python3
"""
unittest for rectangle object
"""
import unittest
Rectangle = __import__("rectangle").Rectangle


class testrectangle(unittest.TestCase):
	"""
	class testrectangle tests inst of rectangle
	"""
	def test_normal(self):
		b1 = Rectangle(10, 10, 10, 10)
		self.assertEqual(b1.width, 10, "width incorrectly set for inst")
		self.assertEqual(b1.height, 10, "height incorrectly set for inst")
		self.assertEqual(b1.x, 10, "x incorrectly set for inst")
		self.assertEqual(b1.y, 10, "y incorrectly set for inst")
		self.assertEqual(b1, "[Rectangle] ({}) {}/{} - {}/{}".format(b1.id, b1.x, b1.y, b1.width, b1.height), "incorrect str repr")
		self.assertEqualstr((b1), "[Rectangle] ({}) {}/{} - {}/{}".format(b1.id, b1.x, b1.y, b1.width, b1.height, "incorrect str repr"))
		self.assertEqual(b1.area(), 100, "invalid area returned")

	def test_badwidth(self):
		with self.assertRaises(TypeError):
			Rectangle.validator(["hey", 10, 10, 10])
	def test_badheight(self):
		with self.assertRaises(TypeError):
			b1 = Rectangle(10, "hey", 10, 10)

	def test_badx(self):
		with self.assertRaises(TypeError):
			b1 = Rectangle(10, 10, "hey", 10)

	def test_bady(self):
		with self.assertRaises(TypeError):
			b1 = Rectangle(10, 10, 10, "hey")