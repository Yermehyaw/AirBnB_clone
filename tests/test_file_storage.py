#!/usr/bin/python3

"""
<<<<<<< HEAD
Modules/Classes Imported: unittest, json, Filestorage, BaseModel, os
=======
Modules Imported: unittest, json, file_storage, os
>>>>>>> master

unittest:tests python modules
json: serializes and deserializes python objects
Filestorage: Class in the file_storage module that stores and retrieves objects
from a json file
<<<<<<< HEAD
BaseModel: Base class
=======
>>>>>>> master
os: access shell commannds from the py script

"""
import unittest
import json
from models.engine.file_storage import FileStorage
<<<<<<< HEAD
from models.base_model import BaseModel
=======
>>>>>>> master
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
<<<<<<< HEAD
        self.obj2 = BaseModel()
        self.obj3 = FileStorage()

    def test_all(self):
        """Test the all() method of FileStorage class
=======
        self.obj2 = FileStorage()
        self.obj3 = FileStorage()

    def test_all(self):
        """Test the all metgod of FileStorage class
>>>>>>> master

        Args:
        None

        """
<<<<<<< HEAD
        self.assertEqual(self.obj1.all(), self.obj1.objects)
        with self.assertRaises(TypeError):
            self.obj1.all(50)

    def test_new(self):
        """Tesrs the new() method that adds a new object to the FileStorage
        variable
=======
        self.assertEqual(self.obj1.all, self.obj1.objects)
        with self.asserRaises(TypeError):
            self.obj1.all(50)

    def test_new(self):
        """Tesrs the mthod that adds a new object to the FieStorage variable
>>>>>>> master

        Args:
        None

        """
<<<<<<< HEAD
        self.obj1.new(self.obj2)
        with self.assertNotRaises(Exception):  # was obj2 successfully added?
            self.obj1.objects[f"{self.obj2.__class__.__name__}.{self.obj2.id}"]

        with self.assertRaises(TypeError):
            self.obj1.new()

        with self.assertRaises(TypeError):
            self.obj1.new(self.obj2, self.obj3)
=======
        self.obj1.new(obj2)
        with self.assertNotRaises(Exception):  # obj2 was successfully added?
            self.obj1.objects[f"{self.obj1.__class__.__name__}.{self.obj1.id}"]
        with self.assertRaises(TypeError):
            self.obj1.new()
        with self.assertRaises(TypeError):
            self.obj1.new(obj2, obj3)
>>>>>>> master

    def test_save(self):
        """Tests the save() method that serializes a class

        Args:
        None

        """
        self.obj1.save()
        self.assertTrue(os.path.getsize(self.obj1.file_path) > 0,
                        "JSON file is empty")

<<<<<<< HEAD
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
=======
        self.obj1.file_path("new_file.json")
        self.assertEqual(self.obj1.file_path, "new_file.json")

        with self.assertRaises(TypeError):
            self.obj1.file_path("")

        with self.assertRaises(TypeError):
            self.obj1.file_path(50)

    def test_reload(self):
        """Tests the JSON load method of the FileStorage class
>>>>>>> master

        Args:
        None

        """
<<<<<<< HEAD
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
=======
        # Test if the json file is empty
        self.obj1.file_path("empty_file.json")
        self.obj1.save()
        with self.assertNotRaises(Exception):
            self.obj1.reload()

        # Test id the fike dosent exist
        with self.assertRaises(FileNotFoundError, IOError):
            # there is no prior config as the file is created if it dosent exist
            # thus this test is more or less redundant. it is created just to
            # fufill all righteousness
            self.obj1.reload()

        with self.asserRaises(TypeError):
            self.obj1.reaload("Invalid arg")
>>>>>>> master


if __name__ == "__main__":
    unittest.main()
