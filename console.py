#!/usr/bin/python3
"""Module that contains the entry point of the command interpreter."""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone."""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program when Ctrl-D is pressed."""
        print()
        return True

    def do_create(self, arg):
        """Create a new object, with optional key=value parameters."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        obj = HBNBCommand.classes[args[0]]()
        for param in args[1:]:
            if "=" not in param:
                continue
            key, value = param.split("=", 1)
            if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
                value = value[1:-1].replace('\\"', '"').replace('_', ' ')
            elif '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    continue
            else:
                try:
                    value = int(value)
                except ValueError:
                    continue
            setattr(obj, key, value)
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj = models.storage.all().get("{}.{}".format(args[0], args[1]))
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj = models.storage.all().get("{}.{}".format(args[0], args[1]))
        if obj is None:
            print("** no instance found **")
            return
        models.storage.delete(obj)
        models.storage.save()

    def do_all(self, arg):
        """Print all instances, or all instances of one class."""
        args = shlex.split(arg)
        cls = None
        if args:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            cls = HBNBCommand.classes[args[0]]
        objs = models.storage.all(cls)
        print("[" + ", ".join(str(obj) for obj in objs.values()) + "]")

    def do_update(self, arg):
        """Update an instance: update <class> <id> <attribute> <value>."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj = models.storage.all().get("{}.{}".format(args[0], args[1]))
        if obj is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr, value = args[2], args[3]
        try:
            value = type(getattr(obj, attr))(value)
        except (AttributeError, ValueError, TypeError):
            pass
        setattr(obj, attr, value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
