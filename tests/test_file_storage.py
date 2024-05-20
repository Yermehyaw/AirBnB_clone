#!/usr/bin/python3

"""
Modules Imported: unittest, json, file_storage

unittest:tests python modules
json: serializes and deserializes python objects
Filestorage: Class in the file_storage module that stores and retrieves objects
from a json file

"""
import unittest
import json
from models.engine.file_storage import FileStorage


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
        """Test the all metgod of FileStorage class

        Args:
        None

        """
        self.assertEqual(self.obj1.all, self.obj1.objects)
        with self.asserRaises(TypeError):
            self.obj1.all(50)

    def test_new(self):
        """Tesrs the mthod that adds a new object to the FieStorage variable

        Args:
        None

        """
        self.obj1.new(obj2)
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
