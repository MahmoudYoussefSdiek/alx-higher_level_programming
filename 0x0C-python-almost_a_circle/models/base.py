#!/usr/bin/python3
"""This module defines the Base class"""

import json
import csv
import os


class Base:
    """
    Base class for managing the id attribute in future classes.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of the
        number of objects created.
                            It is initialized to 0.

    Methods:
        __init__(self, id=None): Class constructor method.
                                 If id is provided, assigns it to the
                                 public instance attribute 'id'.
                                 If id is not provided, increments
                                 __nb_objects and assigns the new
                                 value to 'id'.
    """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): The list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): The list of instances.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by json_string.

        Args:
            json_string (str): The JSON string representation of a list.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: The dictionary of attributes.
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        else:
            instance = cls()
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.

        Returns:
            list: The list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                instances = [
                    cls.create(**dictionary) for dictionary in list_dicts
                ]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""

        filename = cls.__name__ + ".csv"
        list_instances = []
        if os.path.exists(filename):
            with open(filename, "r") as file:
                reader = csv.reader(file)
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                for row in reader:
                    dict = {}
                    for i in range(len(fields)):
                        dict[fields[i]] = int(row[i])
                    list_instances.append(cls.create(**dict))
        return list_instances
