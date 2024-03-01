#!/usr/bin/python3
"""defines FileStorarge class to serialize instances to JSON File"""

import json

class FileStorarge:
    """serializes instances to a JSON"""

    __file_path = 'file.json'
    __objects = {}

    def classes(self):
        """returns a dict of supported chars"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

    def all(self):
        """Return the dict __objects"""
        return self.__objects

    def new(self, obj):
        """sets __objects with key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON"""
        save_dict = {}
        for key, obj in self.__objects.items():
            save_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as tha_file:
            json.dump(save_dict, tha_file)

    def reload(self):
        """deserializes JSON file to __objects """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        try:
            with open(self.__file_path, encoding='utf-8') as tha_file:
                objs = json.load(tha_file)
                for k, v in objs.items():
                    class_name = v['__class__']
                    del v['__class__']
                    self.new(eval(class_name)(**v))

        except FileNotFouendError:
            pass
