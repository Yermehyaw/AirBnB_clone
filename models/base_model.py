"""
Modules Imported: uuid, datetime, json

uuid: Generates random user ids
datetime: Generate time
json: Serializes and deserializes a python object
"""

import json
import uuid
import datetime

class BaseModel():
    """Defines all common attributes/methods for other classes in the Airbnb console
    
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
        if kwargs is None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
#           self.updated_at = datetime.today()
        else:
            for attr, value in kwargs.iteritems():
                if attr == "id":
                    self.id = value
#                elif attr == "created_at":
#                   self.ctreated_at = value
#               elif attr == "updated_at":
#                   self.updated_at = value

    def __str__(self):
        """Returns an augmented string representation of the object

        Args:
        None

        """
#        return f""

    def save(self):
        """Updates the time of the object after an edit

        Args:
        None

        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the __dict__
        of an instance

        Args:
        None

        """
        
