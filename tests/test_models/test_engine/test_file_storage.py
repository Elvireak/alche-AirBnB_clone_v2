#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import os
import unittest
import models
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 "only works with file storage")
class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class."""

    def tearDown(self):
        """Remove the JSON file created by a test."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_storage_type(self):
        """Test that the storage is a FileStorage instance."""
        self.assertIsInstance(models.storage, FileStorage)

    def test_all_returns_dict(self):
        """Test that all returns a dictionary."""
        self.assertIsInstance(models.storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new adds the object to the stored objects."""
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel." + obj.id, models.storage.all())

    def test_save_creates_file(self):
        """Test that save creates the JSON file."""
        BaseModel().save()
        self.assertTrue(os.path.exists("file.json"))

    def test_all_with_class(self):
        """Test that all with a class returns only that class."""
        state = State()
        state.save()
        result = models.storage.all(State)
        self.assertIn("State." + state.id, result)
        for obj in result.values():
            self.assertIsInstance(obj, State)

    def test_delete_removes_object(self):
        """Test that delete removes the object from storage."""
        obj = BaseModel()
        obj.save()
        models.storage.delete(obj)
        self.assertNotIn("BaseModel." + obj.id, models.storage.all())

    def test_reload_loads_saved_object(self):
        """Test that reload brings back a saved object."""
        obj = BaseModel()
        obj.save()
        key = "BaseModel." + obj.id
        models.storage.all().pop(key)
        models.storage.reload()
        self.assertIn(key, models.storage.all())


if __name__ == "__main__":
    unittest.main()
