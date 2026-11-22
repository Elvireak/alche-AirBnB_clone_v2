#!/usr/bin/python3
"""Unit tests for the State class."""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Tests for the State class."""

    def test_is_subclass(self):
        """Test that State inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance_type(self):
        """Test that a new object is an instance of State."""
        self.assertIsInstance(State(), State)

    def test_id_is_string(self):
        """Test that the id of a new State is a string."""
        self.assertIsInstance(State().id, str)

    def test_unique_ids(self):
        """Test that two State objects have different ids."""
        self.assertNotEqual(State().id, State().id)

    def test_dates_are_datetime(self):
        """Test that the dates of a new State are datetime objects."""
        obj = State()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict_class_name(self):
        """Test that to_dict gives the right class name."""
        self.assertEqual(State().to_dict()["__class__"], "State")

    def test_str_contains_class_name(self):
        """Test that the string contains the class name."""
        self.assertIn("[State]", str(State()))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "save is tested differently with db storage")
    def test_save_updates_time(self):
        """Test that save changes the updated_at value."""
        obj = State()
        first = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, first)


if __name__ == "__main__":
    unittest.main()
