#!/usr/bin/python3
"""Module that defines the DBStorage class."""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Stores and reads instances in a MySQL database."""

    __engine = None
    __session = None

    def __init__(self):
        """Create the engine from the environment variables."""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, database),
            pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary of all objects, or of one class only."""
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        elif isinstance(cls, str):
            classes = [c for c in (User, State, City, Amenity, Place, Review)
                       if c.__name__ == cls]
        else:
            classes = [cls]
        result = {}
        for one_class in classes:
            for obj in self.__session.query(one_class).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                result[key] = obj
        return result

    def new(self, obj):
        """Add an object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and start a new database session."""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)
