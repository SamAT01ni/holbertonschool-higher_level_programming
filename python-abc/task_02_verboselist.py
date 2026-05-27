#!/usr/bin/python3
""" Verbose list
    What the hell is verbose
    """


class VerboseList(list):
    """ Inherits built in list with all them things
        """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        super().extend(x)
        print("Extended the list with [{}] items.".format(len(x)))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
