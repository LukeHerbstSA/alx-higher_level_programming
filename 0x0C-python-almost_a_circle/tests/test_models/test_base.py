#!/usr/bin/python3
"""
unittest for base file
"""
import unittest
import base


class basetest(unittest.testcase):
	def test_init_normal(self):
		b1 = Base()
		self.assertequal(b1.id, 0)

	def test_init_id(self):
		b1 = Base(10)
		self.assertequal(b1.id, 10)

	def test_init_neg(self):
		b1 = Base(-1)
		self.assertequal(b1.id, -1)

if __name__ == "__main__":
	unittest.main()
