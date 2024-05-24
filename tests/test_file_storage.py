#!/usr/bin/python3

"""
Modules/Classes Imported: unittest, json, Filestorage, BaseModel, os

unittest:tests python modules
json: serializes and deserializes python objects
Filestorage: Class in the file_storage module that stores and retrieves objects
from a json file
BaseModel: Base class
os: access shell commannds from the py script

"""
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """Tests the file_storage module

    Attributes (non-methods):
    None

    """
    def setUp(self):
        """Test fixture: Preparatory exec before gest methods are tested

        Args:
        None

        """
        self.obj1 = FileStorage()
        self.obj2 = BaseModel()
        self.obj3 = FileStorage()

    def test_all(self):
        """Test the all() method of FileStorage class

        Args:
        None

        """
        self.assertEqual(self.obj1.all(), self.obj1.objects)
        with self.assertRaises(TypeError):
            self.obj1.all(50)

    def test_new(self):
        """Tesrs the new() method that adds a new object to the FileStorage
        variable

        Args:
        None

        """
        self.obj1.new(self.obj2)
        with self.assertNotRaises(Exception):  # was obj2 successfully added?
            self.obj1.objects[f"{self.obj2.__class__.__name__}.{self.obj2.id}"]

        with self.assertRaises(TypeError):
            self.obj1.new()

        with self.assertRaises(TypeError):
            self.obj1.new(self.obj2, self.obj3)

    def test_save(self):
        """Tests the save() method that serializes a class

        Args:
        None

        """
        self.obj1.save()
        self.assertTrue(os.path.getsize(self.obj1.file_path) > 0,
                        "JSON file is empty")

        self.obj1.file_path = "new_file.json"
        self.assertEqual(self.obj1.file_path, "new_file.json")

        with self.assertRaises(TypeError):
            self.obj1.file_path = ""
            self.obj1.save()

        with self.assertRaises(TypeError):
            self.obj1.file_path = 50
            self.obj1.save()

    def test_reload(self):
        """Tests the reload() method that loads a JSON file

        Args:
        None

        """
        # Test if the objects before loading == objects after loadirg
        self.obj1.file_path = "empty_file.json"
        self.obj1.save()
        lambda_reload = lambda obj: (obj.reload(), obj.objects)
        self.assertEqual((None, self.obj1.objects), lambda_reload(self.obj1))

        # Test if the file dosent existm: No exception should be raised
        self.obj1.file_path = "invalid_file.json"
        self.obj1.reload()

        # Test if the file is empty
        with self.assertRaises(JSONDecodeError, EOFError):
            self.obj1.file_path = "empty_file.json"
            with open(self.obj1.file_path, "w") as f:
                f.write("")
            self.obj1.reload()

        with self.asserRaises(TypeError):
            self.obj1.reload("Invalid arg")


if __name__ == "__main__":
    unittest.main()
