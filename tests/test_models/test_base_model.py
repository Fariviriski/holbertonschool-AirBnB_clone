#!/usr/bin/python3
"""test casses for BaseModel"""

import unittest
import os
from datetime import datetime
from models import storage
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ all of the test Cases"""

    def setup(self):
        """set up test env"""
        self.file_path = "test_base_model_save.json"
        self.storage = storage
        self.storage._FileStorage__file_path = self.file_path
        self.model = BaseModel()

    def teardown(self):
        """clean up after test"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)


    def test_init(self):
        """test initialization"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """tests __str__ method"""
        my_model = BaseModel()
        str_output = str(my_model)
        self.assertIn("[BaseModel]", str_output)
        self.assertIn(f"{my_model.id}", str_output)

    def test_save(self):
        """test save method updated_at"""
        my_model = BaseModel()
        og_updated_at = my_model.updated_at
        my_model.save()
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertNotEqual(my_model.updated_at, og_updated_at)
        obj_dict = my_model.to_dict()
        obj_dict_updated_at = obj_dict['updated_at']
        self.assertEqual(my_model.updated_at.isoformat(), obj_dict_updated_at)
        self.assertNotEqual(my_model.updated_at.utcnow(), obj_dict_updated_at)

    def test_persistance(self):
        """test if save() persists"""
        self.model.save()
        loaded_storage = storage
        loaded_storage.reload()
        all_obj = loaded_storage.all()
        key = "BaseModel.{}".format(self.model.id)
        self.assertIn(key, all_obj)
        loaded_model = all_obj[key]
        self.assertEqual(loaded_model.updated_at, self.model.updated_at)

    def test_to_dict(self):
        """test to_dict method"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        my_model.__dict__['name'] = "Test Model"
        self.assertIn('name', my_model.__dict__)

if __name__ == '__main__':
    unittest.main()
