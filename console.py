#!/usr/bin/python3
"""module entry point of cmnd interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine import file_storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command"""
        return True
    def do_EQF(self, arg):
        """EQF to end prog"""
        if cmd is None:
            return True
    def emptyline(self):
        """empty line + enter does nothin"""
        pass
    def do_create(self, arg):
        """creates new instance of BaseModel, saves it and prints id"""
        if not arg:
            print("** class name missing **")
            return
        else:
            try:
                obj = eval(arg)()
                obj.save()
                print(obj.id)

            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """prints string rep of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** instance id is missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id is missing **")
            return

        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """deletes an instance based on name & id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        objects = storage.all()

        if args[0] in storage.classes():
            if len(args) == 2:
                key = f"{args[0]}.{args[1]}"
                if key in objects:
                    del objects[key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """prints string rp for all instances"""
        if arg:
            try:
                eval(arg)
            except NameError:
                print("** class doesn't exist **")
                return
        objects = storage.all()
        result = []
        for key in objects:
            if not arg or arg == key.split(".")[0]:
                result.append(str(objects[key]))
            print(result)

    def do_update(self, arg):
        """updates instance based on class name & id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) == 2:
            print("** attribute name misiing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        objects = storage.all()
        key - f"{args[0]}.{args[1]}"

        if key not in objects:
            print("** not instance found **")
            return
        if args[2] not in ['id', 'created_at', 'updated_at']:
            setattr(objects[key], args[2], args[3].strip("\""))
            objects[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
