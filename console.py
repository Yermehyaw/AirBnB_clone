#!/usr/bin/python3

"""
Modules Imported: cmd

cmd: contains classes for creating a python command interpreter
BaseMOdel: base class for all hbnb classes
FileStorage: class defining methods used to store objects in JSON

"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter for the Airbnb clone

    Attributes (non-methods):
    None (All attributes used are inherited from )

    """
    prompt = "(hbnb) "
    """Change the default prompt of the Cmd class
    """

    def do_quit(self, line):
        """Exit the command interpreter

        Args:
        line (str): Arguments passed to the command

        """
        if line != "":  # do_quit() should receive no argument(s)
            print("Usage: quit")
            return
        else:
            return True  # returns True to break the cmdloop()

    def help_quit(self):
        """Help docs for do_quit()

        Args:
        None

        """
        print("Exit command to quit the program")

    def do_EOF(self, line=""):
        """Exit the command interpreter

        Args:
        line (str): Arguments passed to command

        """
        if line != "":
            print("Usage: EOF")
            return
        return True

    def help_EOF(self):
        """Help docs for do_EOF()

        Args:
        None

        """
        print("Exit command to quit the program")

    def emptyline(self):
        """Executed when an empty line is passed to the interpreter

        Args:
        None

        """
        pass  # do nothing


    def do_create(self, line=""):
        """Creates a new instance of the BaseMOdel class

        Args:
        line (str): Arguments passed to command

        """
        if line == "":
            print("** class name missing **")
            return
        list_args = line.split()
        no_args = len(list_args)
        if no_args > 1:  # can be removed to allow multiple object creation
            print("** Enter only one class name **")
            return
        if line == "BaseMOdel":
            new_obj = BaseMOdel()
        FileStorage.new(new_obj)
        FileStorage.save()
        print(new_obj.id)
    # extra valid classes are added here
    else:
        print("** class doesn't exist **")

    def help_create(self):
        """Help docs for do_create()

        Args:
        None

        """
        print("Creates a new instance of BaseModel and saves it")    

    def do_show(self, line=""):
        """Prints the string rep of an instance

        Args:
        line (str): Arguments passed to command

        """
        if line == "":
            print("** class name missing **")
            return
        list_args = line.split()
        no_args = len(list_args)
        if no_args == 0:  # just in case ;)
            print("** class name missing **")
        elif no_args == 1:
            print("** instance id missing **")
            return

        if list_args[0] == "BaseModel":
            key = f"{list_args[0]}.{list_args[1]}"
            FileStorage.reload()
            all_objects = Filetorage.all()
            try:
                object_found = all_objects[key]
                print(object_found)
            except (KeyError):
                print("** no instance found **")
        # any other valid class names can be aded here(best in a match statement)
        else:
            print ("** class doesn't exist **")

    def do_destroy(self, line=""):
        """Deletes an instance of a specified class

        Args:
        line (str): Arguments passed to command

        """
        if line == "" or line is None:
            print("** class name missing **")
            return
        list_args = line.split()
        no_args = len(list_args)
        if no_args == 0:  # just in case ;)
            print("** class name missing **")
        elif no_args == 1:
            print("** instance id missing **")
            return

        if list_args[0] == "BaseModel":
            key = f"{list_args[0]}.{list_args[1]}"
            FileStorage.reload()
            all_objects = FileStorage.all()
            try:
                all_objects.remove(key)
                FileStorage.objects = all_objects
                FileStorage.save()
            except Exception:
                print("** no instance found **")
        # other valid instance classes
    else:
        print("** instance id missing **")

    def do_all(self, line=""):
        """Print string representations of all instances

        Args:
        line (str): Argument(s) passed to command

        """
        if line is None:  # what happens when None is passed to a method expecting zero args
            print("** class doesn't exist **")
            return
        else:
            list_args = line.split()
            no_args = len(list_args)
            if no_args == 0:  # if no argument is passed, still print all instances
                FileStorage.all()
                return
            for class_name in list_args:
                if class_name == "BaseModel":
                    try:
                        #FileStorage.all()
                # other valid class names
                else:
                    print ("** class doesn't exist **")

    def do_update(self, line-""):
        """Updates an instance of a valid class

        Args:
        line (str): Argument(s) passed to command
        
        """
        if line == "" or line is None:
            print("** class name missing **")
            return
        else:
            list_args = line.split()
            no_args = len(list_args)
            # Verify the correct no of args are passed
            if no_args == 0:
                print("** class name missing **")
                return
            elif no_args == 1:
                print("** instance id missing **")
                return
            elif no_args == 2:
                print("** attribute name missing **")
                return
            elif no_args == 3:
                print("** value missing **")
                return
            else: # the correct no of args is 4, anything else > 4 is ignored
                class_name = list_args[0]
                instance_id = list_args[1]
                attr_name = list_args[2]
                attr_value = list_args[3]
                # Verify a valid class is entered
                if class_name == "BaseModel":




# Help methods for commands
    def help_show(self):
        """Help docs for do_show()

        Args:
        None

        """
        print("Prints the string representation of an instance based
                on the class name and id passed\nUsage: <class> <class_id>")

    def help_destroy(self):
        """Help docs for do_destroy()

        Args:
        None
        
        """
        print("Deletes an instance of a class\nUsage: destroy <class-name> 
                <instance-id>")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
