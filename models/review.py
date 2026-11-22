#!/usr/bin/python3
"""Module that defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review of a place by a user."""
    place_id = ""
    user_id = ""
    text = ""
