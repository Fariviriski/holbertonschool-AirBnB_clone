#!/usr/bin/python3
"""model that inherits for BaseModel"""

from models.base_model import BaseModel

class User(BaseModel):
    """represents a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
