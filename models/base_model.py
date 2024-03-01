#!/usr/bin/python3
"""BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """BaseModel for inheritance
        id(str): id of instance
        created_at(datetime): when created
        updated_at(datetime): when update
    """
    def __init__(self, *args, **kwargs):
        """ initializes instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """string rep of instance"""
        return f"[{self.__cleass__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the updated_at attr"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """converts instance to dict for serials"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
