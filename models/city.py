#!/usr/bin/python3
"""Module that defines the City class."""
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """Represents a city that belongs to a state."""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"),
                          nullable=False)
        places = relationship("Place", cascade="all, delete",
                              backref="cities")
    else:
        state_id = ""
        name = ""
