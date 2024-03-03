#!/usr/bin/python3
"""
file_storage module that contains the FileStorage class
definition and methods
"""
from models.base_model import BaseModel
import json


class FileStorage:
    """
    FileStorage class which serializes instances to a JSON file
    and deserializes JSON files to instances.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary `__objects`.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in `__objects` the `obj` with key `<obj class name>.id`.
        """
        key = type(obj).__name__ + '.' + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes `__objects` to the JSON file.
        """
        with open(self.__file_path, 'w', enoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to `__objects` if the file exists;
        otherwise, does nothing.
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                self.__objects = {k: BaseModel(**v)
                                  for k, v in json.load(file).items()}
        except Exception:
            pass
