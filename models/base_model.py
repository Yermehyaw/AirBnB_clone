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
            self.created_at = datetime.today()  ###
            self.updated_at = datetime.today()  ###
        else:
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
        return f"[{self.__class__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """Updates the time of the object after an edit

        Args:
        None

        """
        self.updated_at = datetime.today()  ###

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the __dict__
        of an instance

        Args:
        None

        """
        # All instance attributes should be returned in the dict via
        # self.__dict__ regardless whether they were initialized by __init__
        return dict['__class__': self.__class___, 'updated_at':
                datetime(updated_at).isoformat(), 'id': self.id,
                'created_at': datetime(created_at).isoformat()]


if __name__ == "__main__":
    diction = {'id': "66885"}
    obj = BaseModel()
    obj.new = "value to __dict__"
    try:
        print(obj.id)
        print(obj.__dict__)
    except Exception:
        print("attribute(s) not found")
    print("All attributes of obj are: {}".format(dir(obj)))
    print("Printing dict rep of object")
    if type(obj.to_dict) == type(dict):
        print(obj.to_dict)
    else:
        print("The object returned is not a dict")
