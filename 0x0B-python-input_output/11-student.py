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

    def to_json(self, attrs=None):
        stu_dict = self.__dict__.copy()
        for key in stu_dict:
            if key[-2:] == "__":
                del stu_dict[key]
        if type(attrs) is list:
            nw_dict = dict()
            for attr in attrs:
                if attr in stu_dict.keys():
                    nw_dict[attr] = stu_dict[attr]
            return nw_dict
        return stu_dict

    def reload_from_json(self, json):
        stu_dict = self.__dict__
        for key in json:
            if key in stu_dict:
                stu_dict[key] = json[key]
