#!/usr/bin/python3
"""This module defines the DBStorage engine (MySQL via SQLAlchemy)"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Manages storage of hbnb models in a MySQL database"""
    __engine = None
    __session = None

    classes = {
        'User': User, 'State': State, 'City': City,
        'Amenity': Amenity, 'Place': Place, 'Review': Review
    }

    def __init__(self):
        """Creates the engine linked to the MySQL database"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries the current database session for objects of cls
        (or all mapped types if cls is None). Returns a dictionary
        with key <class-name>.<object-id> and the object as value."""
        if cls is None:
            targets = list(self.classes.values())
        else:
            if isinstance(cls, str):
                cls = self.classes.get(cls)
            targets = [cls] if cls is not None else []
        result = {}
        for target in targets:
            if not hasattr(target, '__table__'):
                continue
            for obj in self.__session.query(target).all():
                result['{}.{}'.format(type(obj).__name__, obj.id)] = obj
        return result

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables and the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
