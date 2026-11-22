#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage.
        If cls is given, only objects of that class are returned."""
        if cls is None:
            return FileStorage.__objects
        if isinstance(cls, str):
            cls = {c.__name__: c for c in self._classes().values()}.get(cls)
            if cls is None:
                return {}
        return {key: obj for key, obj in FileStorage.__objects.items()
                if isinstance(obj, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside; does nothing if
        obj is None"""
        if obj is None:
            return
        key = obj.to_dict()['__class__'] + '.' + obj.id
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]

    @staticmethod
    def _classes():
        """Returns a dictionary of all model classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        return {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

    def reload(self):
        """Loads storage dictionary from file"""
        classes = self._classes()
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
