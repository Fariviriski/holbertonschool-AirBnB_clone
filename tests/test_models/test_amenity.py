#!/usr/bin/python3
"""tests for amenity class"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_amenity_instance(self):
        """tets if amenity is instance with correct attr"""
        amenity Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    if __name__ == '__main__':
        unittest.main()
