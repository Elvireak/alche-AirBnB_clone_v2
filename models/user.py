#!/usr/bin/python3
"""Module that defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user of the application."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
