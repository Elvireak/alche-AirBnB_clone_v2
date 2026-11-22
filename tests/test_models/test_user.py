#!/usr/bin/python3
"""Unit tests for the User class."""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for the User class."""

    def test_is_subclass(self):
        """Test that User inherits from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_instance_type(self):
        """Test that a new object is an instance of User."""
        self.assertIsInstance(User(), User)

    def test_id_is_string(self):
        """Test that the id of a new User is a string."""
        self.assertIsInstance(User().id, str)

    def test_unique_ids(self):
        """Test that two User objects have different ids."""
        self.assertNotEqual(User().id, User().id)

    def test_dates_are_datetime(self):
        """Test that the dates of a new User are datetime objects."""
        obj = User()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict_class_name(self):
        """Test that to_dict gives the right class name."""
        self.assertEqual(User().to_dict()["__class__"], "User")

    def test_str_contains_class_name(self):
        """Test that the string contains the class name."""
        self.assertIn("[User]", str(User()))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "save is tested differently with db storage")
    def test_save_updates_time(self):
        """Test that save changes the updated_at value."""
        obj = User()
        first = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, first)


if __name__ == "__main__":
    unittest.main()
