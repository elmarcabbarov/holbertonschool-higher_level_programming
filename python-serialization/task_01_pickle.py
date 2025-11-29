#!/usr/bin/python3
"""
Pickle ile Serilasiya ve Deserilasiya eden kod
"""

import pickle


class CustomObject():

    """Init metodu"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    """Melumatlarin cap edilmesi"""

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    """Serilasiya"""

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                return pickle.dump(self, f)
        except Exception:
            return None

    """Deserilasiya"""
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except BaseException:
            return None
