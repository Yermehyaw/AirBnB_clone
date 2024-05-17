#!/usr/bin/python3
"""
Modules Imported: uuid, datetime, json

uuid: Generates random user id
datetime: Generate time
json: Serializes and deserializes a python object

"""
import uuid
from datetime import datetime
import json


class BaseModel():
    """Defines all common attributes/methods for other classes in the Airbnb
    console

    Attributes:
    id (str): Unique user's id
    created_at (obj): Time the object is created
    updated_at (obj): Updated time for any changes made top the object

    """

    def __init__(self, *args, **kwargs):
        """Object constructor for the BaseModel class

        Args:
        args (tuple): Variable number of positional arguments
        kwargs (dict): Variable number of keyword arguments

        """
        if kwargs == {} or kwargs is None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:  # only the available variables should be used, if not a variable is not available the standard values shoukd be initialized
            for attr, value in kwargs.items():
                if attr == "id":
                    self.id = value
                elif attr == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif attr == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)

    def __str__(self):
        """Returns an augmented string representation of the object

        Args:
        None

        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """Updates the time of the object after an edit

        Args:
        None

        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the __dict__
        of an instance

        Args:
        None

        """
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        # Add a key: class name, to the objlects dict attribute
        self.__dict__.update({'__class__': self.__class__.__name__})
        return self.__dict__
