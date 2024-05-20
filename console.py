#!/usr/bin/python3

"""
Modules Imported: cmd

cmd: contains classes for creating a python command interpreter

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter for the Airbnb clone

    Attributes (non-methods):
    None (All attributes used are inherited from )

    """
    prompt = "(hbnb)"
    """Change the default prompt of the Cmd class
    """

    def do_quit(self, invalid_param=None):
        """Exit the command interpreter

        Args:
        None

        """
        if invalid_param != None:
            print "Usage: quit"
            return
        else:
            return True  # returns True to break the cmdloop()

    def help_quit(self):
        """Help docs for do_quit()

        Args:
        None

        """
        print("Exit command to quit the program")

    def do_EOF(self):
        """Exit the command interpreter

        Args:
        None

        """
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
