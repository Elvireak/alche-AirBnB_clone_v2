#!/usr/bin/python3
"""Unit tests for the console."""
import os
import unittest
from io import StringIO
from unittest.mock import patch
import models
from console import HBNBCommand


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 "only works with file storage")
class TestConsole(unittest.TestCase):
    """Tests for the HBNBCommand class."""

    def run_command(self, line):
        """Run one console command and return what it printed."""
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd(line)
        return out.getvalue().strip()

    def tearDown(self):
        """Remove the JSON file created by a test."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_create_missing_class(self):
        """Test create without a class name."""
        self.assertEqual(self.run_command("create"),
                         "** class name missing **")

    def test_create_unknown_class(self):
        """Test create with a class that does not exist."""
        self.assertEqual(self.run_command("create Nope"),
                         "** class doesn't exist **")

    def test_create_prints_id(self):
        """Test that create prints the id of the new object."""
        new_id = self.run_command("create State")
        self.assertIn("State." + new_id, models.storage.all())

    def test_create_string_param(self):
        """Test that a string parameter replaces underscores by spaces."""
        new_id = self.run_command('create State name="New_York"')
        obj = models.storage.all()["State." + new_id]
        self.assertEqual(obj.name, "New York")

    def test_create_integer_param(self):
        """Test that an integer parameter is stored as an integer."""
        new_id = self.run_command("create Place number_rooms=4")
        obj = models.storage.all()["Place." + new_id]
        self.assertEqual(obj.number_rooms, 4)

    def test_create_float_param(self):
        """Test that a float parameter is stored as a float."""
        new_id = self.run_command("create Place latitude=37.77")
        obj = models.storage.all()["Place." + new_id]
        self.assertEqual(obj.latitude, 37.77)

    def test_create_escaped_quote(self):
        """Test that an escaped double quote is kept in the string."""
        new_id = self.run_command(r'create State name="My_\"State\""')
        obj = models.storage.all()["State." + new_id]
        self.assertEqual(obj.name, 'My "State"')

    def test_create_skips_bad_param(self):
        """Test that a parameter that cannot be read is skipped."""
        new_id = self.run_command("create State name=abc")
        obj = models.storage.all()["State." + new_id]
        self.assertNotEqual(getattr(obj, "name", None), "abc")

    def test_show_missing_id(self):
        """Test show without an id."""
        self.assertEqual(self.run_command("show State"),
                         "** instance id missing **")

    def test_show_no_instance(self):
        """Test show with an id that does not exist."""
        self.assertEqual(self.run_command("show State 123"),
                         "** no instance found **")

    def test_destroy_removes_object(self):
        """Test that destroy removes the object from storage."""
        new_id = self.run_command("create State")
        self.run_command("destroy State " + new_id)
        self.assertNotIn("State." + new_id, models.storage.all())

    def test_all_unknown_class(self):
        """Test all with a class that does not exist."""
        self.assertEqual(self.run_command("all Nope"),
                         "** class doesn't exist **")


if __name__ == "__main__":
    unittest.main()
