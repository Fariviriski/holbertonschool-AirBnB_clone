#!/usr/bin/python3
"""defines Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """review class inherits from BaseModel represents a review"""
    place_id = ""
    user_id = ""
    text = ""
