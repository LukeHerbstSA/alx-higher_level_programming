#!/usr/bin/python3
"""
module base - highest parent
"""
import json


class Base:
	"""
	Class base - initializes id of instances of children
	"""
	__nb_objects = 0

	@classmethod
	def create(cls, **dictionary):
		if (cls.__name__ == "Rectangle"):
			Rectangle = __import__("rectangle").Rectangle
			new_inst = Rectangle(1, 2)
			new_inst.update(None, dictionary)
		elif (cls.__name__ == "Square"):
			Base = __import_("square").Square
			new_inst = Square(1)
			new_inst.update(None, dictionary)
		else:
			return
		return (new_inst)

	@classmethod
	def save_to_file(cls, list_objs):
		if (list_objs is None):
			empty_list = json.dumps([])
			with open(cls.__name__ + ".json", "w+") as myfile:
				myfile.write(empty_list)
			return
		with open(cls.__name__ + ".json", "w+") as myfile:
			json_list = Base.to_json_string(list_objs)
			myfile.write(json_list)

	@classmethod
	def load_from_file(cls):
		if (cls.__name__ == "Rectangle" or cls.__name__ == "Rectangle"):
			try:
				with open(cls.__name__ + ".json", r) as myfile:
					list_instances = []
					json_text = myfile.read()
					list_dicts = Base.from_json_string(json_text)
					for element in list_dicts:
						new_inst = Base.create(element)
						list_instances.append(new_inst)
					return (list_instances)
			except FileNotFoundError:
				return ([])

	@staticmethod
	def from_json_string(json_string):
		if (json_string is None):
			return ([])
		return (json.loads(json_string))

	@staticmethod
	def to_json_string(list_dictionaries):
		if (list_dictionaries is None or len(list_dictionaries) == 0):
			return("[]")
		json_dict = json.dumps(list_dictionaries)
		return (json_dict)

	def __init__(self, id=None):
		if not (id is None):
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
