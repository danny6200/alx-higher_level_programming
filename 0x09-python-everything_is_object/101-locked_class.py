#!/usr/bin/python3
"""
    This module supplies the lockedClass.
"""


class LockedClass:
    """
        This is the locked class.
        It allows only the creation
        of first_name as attribute
    """
    def __setattr__(self, name, value):
        """
            This method is reponsible for
            checking and setting the attribute
            to be created
        """
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")