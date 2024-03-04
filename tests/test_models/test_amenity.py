#!/usr/bin/python3
"""
test_amenity is a module used for unit testing of
the Amenity class.
"""
import unittest
from models.amenity import Amenity


class AmenityTests(unittest.TestCase):
    """
    Class AmenityTests provides unit testing for
    the Amenity class.
    """
    def init_test(self):
        """tests initialization of Amenity"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

    def test_attributes(self):
        """testing Amenity's Attr."""
        amenity = Amenity()
        amenity.name = "Smoker's Lounge"
        self.assertEqual(amenity.name, "Smoker's Lounge")

    def test_toDict(self):
        """test 2 dict"""
        amenity = Amenity()
        amenity.name = "Cocktail Bar"
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["name"], "Cocktail Bar")
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_fromDict(self):
        """test from_dic"""
        amenity_dict = {
            "name": "Game Room",
            "__class__": "Amenity",
            "id": "420",
            "created_at": "2023-12-17T12:43:30.0",
            "updated_at": "2024-02-01T09:52:10.1"
        }
        amenity = Amenity(**amenity_dict)
        self.assertEqual(amenity.name, "Game Room")
        self.assertEqual(amenity.id, "420")
        self.assertEqual(amenity.created_at.isoformat(), "2023-12-17T12:43:30")
        self.assertEqual(amenity.updated_at.isoformat(), "2024-02-01T09:52:10.100000")

    if __name__ == '__main__':
        unittest.main()
