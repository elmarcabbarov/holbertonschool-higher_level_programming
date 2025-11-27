#!/usr/bin/python3
"""square to inherit from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square
    """

    def __init__(self, size):
        """
        ilkin melumat cart curt
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
