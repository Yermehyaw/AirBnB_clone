2#!/usr/bin/python3
"""
Modules Imported: unittest

unittest
Unit tests for python packages and modules

BaseModel
Base class for all Airbnb clone objects
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Tests the BaseModel claass

    Attributes (non-methods):
    None
    """
    def setUp(self):
        """Test fixture for the BaseModel class objects

        Args:
        None
        """
        sample_dict = {'id': "67888"}
        obj = BaseModel()
        obj_dict = BaseModel(**sample_dict)

    def test_custom_str(self):
        """Tests the custom __str__ special method of the BaseModel class

        Args:
        None
        """
        obj = BaseModel()
        self.assertEqual(print(obj), print (f"[{obj.__class__}] ({obj.id}) \
        <{obj.__dict__}>"))

    def test_save(self):
        """Tests the save method of the BaseModel class

        Args:
        None

        """
        obj = BaseModel()
        obj.save()
        new_time = obj.updated_at
        self.assertEqual(obj.updated_at, new_time)
        with self.assertRaises(ValueError):
            raise ValueError

    def test_to_dict(self):
        """Tests the to_dict() meyhod of the BaseModel class

        Args:
        None

        """
        self.assertEqual(obj_dict(to_dict), )
