#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""

    def test_id_is_string(self):
        """Test that the id of a new instance is a string."""
        self.assertIsInstance(BaseModel().id, str)

    def test_unique_ids(self):
        """Test that two instances do not share the same id."""
        self.assertNotEqual(BaseModel().id, BaseModel().id)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        self.assertIsInstance(BaseModel().created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        self.assertIsInstance(BaseModel().updated_at, datetime)

    def test_str_format(self):
        """Test that the string starts with the class name and id."""
        obj = BaseModel()
        self.assertTrue(str(obj).startswith(
            "[BaseModel] ({})".format(obj.id)))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "save is tested differently with db storage")
    def test_save_updates_time(self):
        """Test that save changes the updated_at value."""
        obj = BaseModel()
        first = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, first)

    def test_to_dict_class_name(self):
        """Test that to_dict contains the class name."""
        self.assertEqual(BaseModel().to_dict()["__class__"], "BaseModel")

    def test_to_dict_dates_are_strings(self):
        """Test that to_dict converts dates to strings."""
        data = BaseModel().to_dict()
        self.assertIsInstance(data["created_at"], str)
        self.assertIsInstance(data["updated_at"], str)

    def test_kwargs_recreate_instance(self):
        """Test that an instance can be rebuilt from its dictionary."""
        obj = BaseModel()
        new = BaseModel(**obj.to_dict())
        self.assertEqual(obj.id, new.id)
        self.assertEqual(obj.created_at, new.created_at)

    def test_kwargs_skip_class_key(self):
        """Test that the __class__ key is not set as an attribute."""
        new = BaseModel(**BaseModel().to_dict())
        self.assertNotIn("__class__", new.__dict__)


if __name__ == "__main__":
    unittest.main()
