#!/usr/bin/python3
"""Unit tests for the Place class."""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for the Place class."""

    def test_is_subclass(self):
        """Test that Place inherits from BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_instance_type(self):
        """Test that a new object is an instance of Place."""
        self.assertIsInstance(Place(), Place)

    def test_id_is_string(self):
        """Test that the id of a new Place is a string."""
        self.assertIsInstance(Place().id, str)

    def test_unique_ids(self):
        """Test that two Place objects have different ids."""
        self.assertNotEqual(Place().id, Place().id)

    def test_dates_are_datetime(self):
        """Test that the dates of a new Place are datetime objects."""
        obj = Place()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict_class_name(self):
        """Test that to_dict gives the right class name."""
        self.assertEqual(Place().to_dict()["__class__"], "Place")

    def test_str_contains_class_name(self):
        """Test that the string contains the class name."""
        self.assertIn("[Place]", str(Place()))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "save is tested differently with db storage")
    def test_save_updates_time(self):
        """Test that save changes the updated_at value."""
        obj = Place()
        first = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, first)


if __name__ == "__main__":
    unittest.main()
