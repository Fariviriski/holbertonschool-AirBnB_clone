#!/usr/bin/python3

import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setup(self):
        """test setup env"""
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.model = BaseModel()

    def tearDown(self):
        """clean up test"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """test all method"""
        all_obj = self.storage.all()
        self.assertIsInstance(all_obj, dict)

    def test_new(self):
        """test new method"""
        self.storage.new(self.model)
        all_obj = self.storage.all()
        key = "BaseModel.{}".format(self.model.id)
        self.assertIn(key, all_obj)

    def test_save(self):
        """test save"""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """tests reaload"""
        self.storage.new(self.model)
        self.storage.save()
        loaded_storage = FileStorage()
        with self.assertRaises(TypeError):
            loaded_storage.reload("incorrect_type_parameter")
        loaded_storage.reload()
        all_obj = loaded_storage.all()
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, all_obj)

    def reload_docstr(self):
        """test for doc"""
        instance = FileStorage()
        self.assertIsNotNone(instance.reload.__doc__)

    def test_reload_types(self):
        """types of parameter test"""
        self.storage.new(self.model)
        self.storage.save()

        loaded_storage = FileStorage()

        with self.assertRaises(TypeError):
            loaded_storage.reload("incorrect_parameter")

        loaded_storage.reload()

        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, loaded_storage.all())

    def Test_reload_nonexixtent(self):
        """test for nones=xistant file"""
        self.storage.new(self.model)
        self.storage.save()
        os,remove(self.file_path)
        loaded_storage = FileStorage()
        loaded_storage = reload()
        self.assertGreaterEqual(len(loaded_storage.all()), 0)

    if __name__ == '__main__':
        unitest.main()
