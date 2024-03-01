#!/usr/bin/python3
"""defines a city class from BaseModel"""

from models.base_model import BaseModel

class City(BaseModel):
    """city class inherits from BaseModel represents a city"""
    state_id = ""
    name = ""
