#!/usr/bin/python3
"""Module for TestHBNBCommand class."""
"""Test Console Module"""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
from io import StringIO
import sys
import datetime
from unittest.mock import patch
import re
import os


class Test_CommanConsole(unittest.TestCase):
    """Test Console Module (console.py)"""

    def do_quit(self, line):
        """Quit command to exit the HBNB console"""
        print("Thank you for using The Console")
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        print()
        return True

    def emptyline(self):
        """Ingnore empty line"""
        pass

    def do_create(self, user_input):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        """
        if not user_input:
            print("** class name missing **")
        elif user_input in class_check:
            _input = user_input.split()
            new_obj = class_check[_input[0]]()
            new_obj.save()
            storage.reload()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            _input = line.split(' ')
            if _input[0] not in class_check:
                print("** class doesn't exist **")
            elif len(_input) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(_input[0], _input[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            _input = line.split(' ')
            if _input[0] not in class_check():
                print("** class doesn't exist **")
            elif len(_input) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(_input[0], _input[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, name):
        """
        Prints all string representation of all instances
        bases on a class name
        """
        if name != "":
            _inputt = name.split(' ')
            if _inputt[0] not in class_check:
                print("** class doesn't exist **")
            else:
                list_str = [str(obj) for key, obj in storage.all().items()
                            if type(obj).__name__ == _inputt[0]]
                print(list_str)
        else:
            list_str = [str(obj) for key, obj in storage.all().items()]
            print(list_str)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute(save the change into the JSON file)
        """
        inpu = line.split()
        if line == "" or line is None:
            print("** class name missing **")
        elif inpu[0] in self.class_list:
            if len(inpu) < 2:
                print("**instance id missing**")
            elif len(inpu) < 3:
                print("**attribute name missing**")
            elif len(inpu) < 4:
                print("**value missing**")
            else:
                key = "{}.{}".format(inpu[0], inpu[1])
                if key in storage.all():
                    if type(inpu[3]) is dict:
                        storage.all()[key].setattr(inpu[2], inpu[3])
                    objs[key].__setattr__(inpu[2], inpu[3])
                    objs[key].save()
                else:
                    print("**no instance found**")
        else:
            print("**class doesn't exist**")


if __name__ == '__main__':
    class_check = {"Amenity", "BaseModel", "City" "Place", "Review",
                   "State", "User"}
    HBNBCommand().cmdloop()
