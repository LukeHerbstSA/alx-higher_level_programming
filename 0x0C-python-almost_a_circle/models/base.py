#!/usr/bin/python3
"""
module base - highest parent
"""
import json
Rectangle = __import__("rectangle").Rectangle
Square = __import__("square").Square


class Base:
    """
    Class base - initializes id of instances of children
    """
    __nb_objects = 0

    @classmethod
    def create(cls, **dictionary):
	    if (cls.__name__ == "Rectangle"):
		    new_inst = Rectangle(1, 2)
		    new_inst.update(dictionary)
	    if (cls.__name__ == "Square"):
		    new_inst = Square(1)
		    new_inst.update(dictionary)
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
