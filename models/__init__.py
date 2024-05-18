#!/usr/bin/python3

"""
Impoted Modules: file_storage

file_storage
serializes instances to a JSON file and deserializes JSON file to instances

"""
import engines.file_storage  ###


# Creates a unique FileStorage class object
storage = file_storage.FileStorage()
storage.reload()

