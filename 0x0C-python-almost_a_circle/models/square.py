#!/usr/bin/python3
"""
Square subclass of Rectangle
"""
Rectangle = __import__("rectangle").Rectangle


class Square(Rectangle):
	"""
	class square uses inheritance to initialize special isntances
	"""
	def __str__(self):
		firsthlf = "[Square] ({}) {}/{} ".format(self.id, self.x, self.y)
        scndhlf = "- {}/{}".format(self.width, self.height)
        return (firsthlf + scndhlf)	

	def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

	def update(self, *args, **kwargs):
		if (args == None):
			for key, value in kwargs:
				setattr(self, key, value)
		for i in range(0, len(args)):
			if (i == 0):
				self.id = args[i]
			if (i == 1):
				self.size = args[i]
			if (i == 2):
				self.x = args[i]
			if (i == 3):
				self.y = args[i]

	@property
	def size(self):
		return (self.width)

	@size.setter
	def size(self, value):
		super().validator("width", value)
		self.width = value
		self.height = value