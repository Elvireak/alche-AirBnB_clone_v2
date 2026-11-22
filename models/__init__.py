#!/usr/bin/python3
"""Module that creates the storage instance of the project."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
