#!/usr/bin/python3
"""Unit tests for the DBStorage class."""
import unittest
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """Tests for the structure of the DBStorage class."""

    def test_class_has_docstring(self):
        """Test that the DBStorage class has a docstring."""
        self.assertIsNotNone(DBStorage.__doc__)

    def test_module_has_docstring(self):
        """Test that the db_storage module has a docstring."""
        import models.engine.db_storage as module
        self.assertIsNotNone(module.__doc__)

    def test_has_all_method(self):
        """Test that DBStorage has an all method."""
        self.assertTrue(callable(getattr(DBStorage, "all", None)))

    def test_has_new_method(self):
        """Test that DBStorage has a new method."""
        self.assertTrue(callable(getattr(DBStorage, "new", None)))

    def test_has_save_method(self):
        """Test that DBStorage has a save method."""
        self.assertTrue(callable(getattr(DBStorage, "save", None)))

    def test_has_delete_method(self):
        """Test that DBStorage has a delete method."""
        self.assertTrue(callable(getattr(DBStorage, "delete", None)))

    def test_has_reload_method(self):
        """Test that DBStorage has a reload method."""
        self.assertTrue(callable(getattr(DBStorage, "reload", None)))

    def test_methods_have_docstrings(self):
        """Test that every public method has a docstring."""
        for name in ("all", "new", "save", "delete", "reload"):
            self.assertIsNotNone(getattr(DBStorage, name).__doc__)


if __name__ == "__main__":
    unittest.main()
