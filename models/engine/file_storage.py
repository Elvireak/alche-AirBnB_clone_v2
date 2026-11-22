#!/usr/bin/python3
"""Module that defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Stores instances in a JSON file and loads them back."""

    __file_path = "file.json"
    __objects = {}

    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def all(self, cls=None):
        """Return all objects, or only the objects of the given class."""
        if cls is None:
            return FileStorage.__objects
        name = cls if isinstance(cls, str) else cls.__name__
        return {key: obj for key, obj in FileStorage.__objects.items()
                if type(obj).__name__ == name}

    def new(self, obj):
        """Add an object to the dictionary of stored objects."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Write all stored objects to the JSON file."""
        data = {key: obj.to_dict()
                for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """Load the objects from the JSON file, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                data = json.load(f)
        except FileNotFoundError:
            return
        for key, value in data.items():
            FileStorage.__objects[key] = self.classes[value["__class__"]](
                **value)

    def delete(self, obj=None):
        """Delete an object from the stored objects, if it is there."""
        if obj is None:
            return
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects.pop(key, None)
