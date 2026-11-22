#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class."""

    def test_is_subclass(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance_type(self):
        """Test that a new object is an instance of Amenity."""
        self.assertIsInstance(Amenity(), Amenity)

    def test_id_is_string(self):
        """Test that the id of a new Amenity is a string."""
        self.assertIsInstance(Amenity().id, str)

    def test_unique_ids(self):
        """Test that two Amenity objects have different ids."""
        self.assertNotEqual(Amenity().id, Amenity().id)

    def test_dates_are_datetime(self):
        """Test that the dates of a new Amenity are datetime objects."""
        obj = Amenity()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict_class_name(self):
        """Test that to_dict gives the right class name."""
        self.assertEqual(Amenity().to_dict()["__class__"], "Amenity")

    def test_str_contains_class_name(self):
        """Test that the string contains the class name."""
        self.assertIn("[Amenity]", str(Amenity()))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "save is tested differently with db storage")
    def test_save_updates_time(self):
        """Test that save changes the updated_at value."""
        obj = Amenity()
        first = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, first)


if __name__ == "__main__":
    unittest.main()
