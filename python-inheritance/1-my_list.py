#!/usr/bin/python3
"""
Bu taskda listden miras alib kod yaziriq
"""


class MyList(list):
    """
    List miras alir sonra funksiya yaradir
    """

    def print_sorted(self):
        """
        sortlanmis lsit print edir
        """
        print(sorted(self))
