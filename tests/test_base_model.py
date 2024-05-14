"""
Modules Imported: unittest

unittest
Unit tests for python packages and modules
"""
import unittest

class TestBaseModel(unittest.TestCase):
    """Tests the BAseModel claass
    """
    def setUp(self):
        """Test fixture for the BaseModel class objects
        """
        sample_dict = {}
        obj = BaseModel()
        obj_dict = BaseModel(**sample_dict)

    def 
