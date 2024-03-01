#!/usr/bin/python3

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def test_place_instance(self):
        """ test if place is instance and hac=s correct attr"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathroom"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_id"))

    def test_attribute_types(self):
        """test types of attr"""
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathroom, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_id, list)


if __name__ == '__main__':
    unittest.main()
