#!/usr/bin/python3
"""Unit tests for the Review class."""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for the Review class."""

    def test_is_subclass(self):
        """Test that Review inherits from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance_type(self):
        """Test that a new object is an instance of Review."""
        self.assertIsInstance(Review(), Review)

    def test_id_is_string(self):
        """Test that the id of a new Review is a string."""
        self.assertIsInstance(Review().id, str)

    def test_unique_ids(self):
        """Test that two Review objects have different ids."""
        self.assertNotEqual(Review().id, Review().id)

    def test_dates_are_datetime(self):
        """Test that the dates of a new Review are datetime objects."""
        obj = Review()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict_class_name(self):
        """Test that to_dict gives the right class name."""
        self.assertEqual(Review().to_dict()["__class__"], "Review")

    def test_str_contains_class_name(self):
        """Test that the string contains the class name."""
        self.assertIn("[Review]", str(Review()))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "save is tested differently with db storage")
    def test_save_updates_time(self):
        """Test that save changes the updated_at value."""
        obj = Review()
        first = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, first)


if __name__ == "__main__":
    unittest.main()
