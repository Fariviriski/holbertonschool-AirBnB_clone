#!/usr/bin/python3

import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def test_city_instance(self):
        """test if is instance and has correct attr"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

if __name__ == '__main__':
    unittest.main()
