#!/usr/bin/python3
"""
Bu taskda bos bir class yaradilir
"""


class BaseGeometry():
    """
    Bos bir kals yaratdim
    """

    def area(self):
        """
        Exception qaldiririq nesede cixis verir
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        TyepError ValueError fln qaldiri
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
