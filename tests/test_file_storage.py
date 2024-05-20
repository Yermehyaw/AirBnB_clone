#!/usr/bin/python3

"""
Modules Imported: unittest, json, file_storage, os

unittest:tests python modules
json: serializes and deserializes python objects
Filestorage: Class in the file_storage module that stores and retrieves objects
from a json file
os: access shell commannds from the py script

"""
import unittest
import json
from models.engine.file_storage import FileStorage
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
        self.obj2 = FileStorage()
        self.obj3 = FileStorage()

    def test_all(self):
        """Test the all() method of FileStorage class

        Args:
        None

        """
        self.assertEqual(self.obj1.all, self.obj1.objects)
        with self.asserRaises(TypeError):
            self.obj1.all(50)

    def test_new(self):
        """Tesrs the new() method that adds a new object to the FieStorage
        variable

        Args:
        None

        """
        self.obj1.new(self.obj2)
        with self.assertNotRaises(Exception):  # obj2 was successfully added?
            self.obj1.objects[f"{self.obj1.__class__.__name__}.{self.obj1.id}"]
        with self.assertRaises(TypeError):
            self.obj1.new()
        with self.assertRaises(TypeError):
            self.obj1.new(obj2, obj3)

    def test_save(self):
        """Tests the save() method that serializes a class

        Args:
        None

        """
        self.obj1.save()
        self.assertTrue(os.path.getsize(self.obj1.file_path) > 0,
                        "JSON file is empty")

        self.obj1.file_path("new_file.json")
        self.assertEqual(self.obj1.file_path, "new_file.json")

        with self.assertRaises(TypeError):
            self.obj1.file_path("")

        with self.assertRaises(TypeError):
            self.obj1.file_path(50)

    def test_reload(self):
        """Tests the reload() method that loads a JSON file

        Args:
        None

        """
        # Test if the json file is empty
        self.obj1.file_path("empty_file.json")
        self.obj1.save()
        with self.assertNotRaises(Exception):
            self.obj1.reload()

        # Test id the file dosent exist
        with self.assertRaises(FileNotFoundError, IOError):
            # there is no prior config as the file is created if it dosent
            # exist, thus this test is more or less redundant. it is
            # created just to fufill all righteousness
            self.obj1.reload()

        with self.asserRaises(TypeError):
            self.obj1.reaload("Invalid arg")


if __name__ == "__main__":
    unittest.main()
