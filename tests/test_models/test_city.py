#!/usr/bin/python3
"""Unit tests for the City class."""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for the City class."""

    def test_is_subclass(self):
        """Test that City inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_instance_type(self):
        """Test that a new object is an instance of City."""
        self.assertIsInstance(City(), City)

    def test_id_is_string(self):
        """Test that the id of a new City is a string."""
        self.assertIsInstance(City().id, str)

    def test_unique_ids(self):
        """Test that two City objects have different ids."""
        self.assertNotEqual(City().id, City().id)

    def test_dates_are_datetime(self):
        """Test that the dates of a new City are datetime objects."""
        obj = City()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict_class_name(self):
        """Test that to_dict gives the right class name."""
        self.assertEqual(City().to_dict()["__class__"], "City")

    def test_str_contains_class_name(self):
        """Test that the string contains the class name."""
        self.assertIn("[City]", str(City()))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "save is tested differently with db storage")
    def test_save_updates_time(self):
        """Test that save changes the updated_at value."""
        obj = City()
        first = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, first)


if __name__ == "__main__":
    unittest.main()
