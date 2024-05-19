#!/usr/bin/python3

"""
Modules Imported: json

json; serializes and deserializes python objects

"""
import json


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
        FileStorage.__objects = dict_rep

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
#        self.__objects[obj_class_id] = obj.to_dict
        FileStorage.__objects.update({obj_class_id: obj.to_dict()})

    def save(self):
        """Serializes __objects to a JSON string and stores it in __filr_path

        Args:
        None

        """
        if FileStorage.__file_path is not None and FileStorage != "":
            try:
                with open(FileStorage.__file_path, "w") as f:
                    json.dump(FileStorage.__objects, f)
            except Exception:
                print("JSON file is unavailable")

    def reload(self):
        """Deserializes JSON file to a dict rep of the instances of
        their respective classes and saves them in __objects

        Args:
        None

        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
        except Exception:
            pass
