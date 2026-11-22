#!/usr/bin/python3
"""Module that defines the BaseModel class for all other classes."""
import uuid
from datetime import datetime
import models
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel:
    """Base class that defines the common attributes and methods."""

    def __init__(self, *args, **kwargs):
        """Create a new instance, from kwargs or with default values."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    if isinstance(value, str):
                        value = datetime.fromisoformat(value)
                setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Return the string representation of the instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Update updated_at, add the instance to storage and save."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary with all the keys and values of the instance."""
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def delete(self):
        """Delete the instance from storage."""
        models.storage.delete(self)
