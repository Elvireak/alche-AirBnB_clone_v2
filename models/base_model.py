#!/usr/bin/python3
"""Module that defines the BaseModel class for all other classes."""
import uuid
from datetime import datetime
from os import getenv
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

if getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """Base class that defines the common attributes and methods."""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Create a new instance, from kwargs or with default values."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        for key, value in kwargs.items():
            if key == "__class__":
                continue
            if key in ("created_at", "updated_at") and isinstance(value, str):
                value = datetime.fromisoformat(value)
            setattr(self, key, value)

    def __str__(self):
        """Return the string representation of the instance."""
        data = dict(self.__dict__)
        data.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, data)

    def save(self):
        """Update updated_at, add the instance to storage and save."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary with all the keys and values of the instance."""
        new_dict = dict(self.__dict__)
        new_dict.pop("_sa_instance_state", None)
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def delete(self):
        """Delete the instance from storage."""
        models.storage.delete(self)
