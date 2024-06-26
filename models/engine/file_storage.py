#!/usr/bin/python3

"""
Modules Imported: json, os

json; serializes and deserializes python objects
os: execute shell commannds from a py module

"""
import json
import os


class FileStorage():
    """Serializes instances of a JSON file and deserializes the JSON file
    back to instances

    Attributes (non-methods);
    __file_path (str): path to JSON file
    __objects (dict): dictionary of all instances

    """
    __file_path = "file.json"  # sane as ./file.json
    """str: file where all instances are saved as a json string
    """
    __objects = {}
    """dict: dictionary of instances, keys are a concatenation of the
    instance's Class and its id attribute e.g ClassName.3455335
    """

    @property
    def objects(self):
        """Property getter of __objects

        Args:
        None

        """
        return FileStorage.__objects

    @objects.setter
    def objects(self, dict_rep):
        """Property setter for __objects

        Args:
        dict_rep (dict): dictionary to be saved in __objects

        """
        if isinstance(dict_rep, dict):
            FileStorage.__objects = dict_rep
        else:
            raise TypeError("Invalid argument")

    @property
    def file_path(self):
        """Property getter for __file_path

        Args:
        None

        """
        return FileStorage.__file_path

    @file_path.setter
    def file_path(self, new_path):
        """Property setter for __file_path


        Args:
        None

        """
        if isinstance(new_path, str) and new_path != "":
            FileStorage.__file_path = new_path
        else:
            raise TypeError("Invalid argument")

    def all(self):
        """Returns all objects stored in __objects

        Args:
        None

        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id

        Args:
        obj (obj): instance of an acceptable class

        """
        class_name = obj.__class__.__name__
        obj_class_id = f"{class_name}.{obj.id}"
        FileStorage.__objects.update({obj_class_id: obj.to_dict()})

    def save(self):
        """Serializes __objects to a JSON string and stores it in __filr_path

        Args:
        None

        """
        if isinstance(FileStorage.__file_path, str) and FileStorage != "":
            try:
                with open(FileStorage.__file_path, "w") as f:
                    json.dump(FileStorage.__objects, f)
            except Exception:
                print("JSON file is unavailable")
        else:
            raise TypeError("File location in unavailable")

    def reload(self):
        """Deserializes JSON file to a dict rep of the instances of
        their respective classes and saves them in __objects

        Args:
        None

        """
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r") as f:
                    FileStorage.__objects = json.load(f)
            except Exception:
                pass
            else:
                pass
