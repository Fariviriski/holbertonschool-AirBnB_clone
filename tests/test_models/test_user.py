#!/usr/bin/python3

import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):

    def test_user_instance(self):
        """test user instance and correct attr"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_attribute_types(self):
        """test attr types"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_save(self):
        """test user save"""
        user = User()
        old_created_at = user.created_at
        old_updated_at - user.updated_at
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)

    def test_to_dict(self):
        """test to_dict"""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)

if __name__ == '__main__':
    unittest.main()
