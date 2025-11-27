#!/usr/bin/python3
"""rectangle to inherit from basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """_
    REctangle eleyen bir kod
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Saheni hesablayir
        Returns:
            area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        STR Funksiya yazilir
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
