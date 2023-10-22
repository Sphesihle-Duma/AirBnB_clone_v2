#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if not cls:
            return FileStorage.__objects
        cls_objs = {}
        for key, obj in FileStorage.__objects.items():
            if isinstance(obj, cls):
                cls_objs[key] = obj
        return cls_objs

    def search(self, cls=None, **kwargs):
        """serialize the file path to JSON file path"""
        objs = self.all(cls)
        for key, obj in objs:
            flag = 0
            for attr, value in kwargs:
                if obj.get(attr) != value:
                    flag = 1
                    break
            if flag == 0:
                return obj
        return None

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """serialize the file path to JSON file path"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj:
<<<<<<< HEAD
            for key, value in FileStorage.__objects.items():
                if obj == value:
                    del FileStorage.__objects[key]
                    break

    def close(self):
        """Calls reload() method for deserializing the JSON file to objects"""
=======
            fmd_key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[fmd_key]

    def close(self):
        """ calls reload() """
>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da
        self.reload()
