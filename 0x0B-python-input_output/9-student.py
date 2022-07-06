#!/usr/bin/python3
"""
A module that retrives dictionary rep of student
"""


class Student(object):
    """
    A student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        stu_dict = self.__dict__.copy()
        for key in stu_dict:
            if key[-2:] == "__":
                del stu_dict[key]
        return stu_dict
