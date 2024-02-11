#!/usr/bin/python3

class Base:
    __nb_objects = 0

    def create(cls, **dictionary):
	pass

    def save_to_file(cls, list_objs):
	if (list_objs is None):
		empty_list = json.dumps([])
		with open(self.__name__ + ".json", "w+") as myfile:
			myfile.write(empty_list)
	with open(self.__name__ + ".json", "w+") as myfile:
		json_list = to_json_string(listobjs)
		myfile.write(json_list)

    @staticmethod
    def from_json_string(json_string):
    	if (json_string is None):
		return ([])
	return (json.loads(json_string))

    @staticmethod
    def to_json_string(list_dictionaries):
	if (list_dictionaries is None or len(list_dictionaries == 0)):
		print("[]")
		return
	json_dict = json.dumps(list_dictionaries)
	return (json_dict)

    def __init__(self, id=None):
        if (!(id is None)):
            self.id = id
        else:
            __nb_object += 1
            self.id = __nb_objects
