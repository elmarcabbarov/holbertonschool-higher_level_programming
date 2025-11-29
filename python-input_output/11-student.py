#!/usr/bin/python3
"""student classi yarat sonra icindekileri json ele deyesen"""


class Student():
    """Public deyerler yarat"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """List olub olmadigini yoxlayir"""
        if not isinstance(attrs, list):
            return self.__dict__.copy()
        """Listin incindeki her seyin str olub olmadigini yoxlayir"""
        if not all(isinstance(attrs, str) for attr in attrs):
            return self.__dict__.copy()
        """Lazim olanlari cap etmekin return eleyirkimi bir sey"""
        result = {}
        for attr in attrs:
            if attr in self.__dict__:
                result[attr] = self.__dict__[attr]
        return result

    def reload_from_json(self, json):
        """Obyektin JSONdan cevrilmesi"""
        for key, value in json.items():
            setattr(self, key, value)
