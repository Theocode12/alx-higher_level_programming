#!/usr/bin/python3
"""
Base class for all other classes
"""

import json
import csv
import turtle
import time


class Base(object):
    """
    Base Class
    """

    __nb_object = 0

    def __init__(self, id=None):
        """Initialization method"""

        if id is None:
            self.__class__.__nb_object += 1
            self.id = self.__class__.__nb_object
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        changes a python dictionary to a json string equivalent
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save attributes of an object in a file"""

        filename = cls.__name__ + ".json"
        if list_objs is None:
            j_obj = Base.to_json_string([])
        else:
            list_dict = []
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                list_dict.append(obj_dict)
            j_obj = Base.to_json_string(list_dict)
        with open(filename, mode="w", encoding="utf-8") as fd:
            fd.write(j_obj)

    @staticmethod
    def from_json_string(json_string):
        """converts json string to python object"""

        if json_string is None:
            return []
        py_obj = json.loads(json_string)
        return py_obj

    @classmethod
    def create(cls, **dictionary):
        """creates an object with values from the dictionary"""
        if cls.__name__ == "Rectangle":
            obj_cls = cls(3, 5)
        else:
            obj_cls = cls(4)
        obj_cls.update(**dictionary)
        return obj_cls

    @classmethod
    def load_from_file(cls):
        """
        opens a file and create an object with content from the file
        """

        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r", encoding="utf-8") as fd:
                j_obj = fd.read()
        except Exception:
            return []
        py_obj = cls.from_json_string(j_obj)
        obj_list = []
        for obj in py_obj:
            create_cls_ins = cls.create(**obj)
            obj_list.append(create_cls_ins)
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves object atrributes to csv file"""

        filename = cls.__name__ + ".csv"
        list_of_dict = []
        for objs in list_objs:
            list_of_dict.append(objs.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as csv_file:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for dictionary in list_of_dict:
                writer.writerow(dictionary)

    @classmethod
    def load_from_file_csv(cls):
        """loads object files from csv file"""

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', encoding='utf-8') as csv_file:
                data = csv.DictReader(csv_file)
                obj_ins = []
                for row in data:
                    for key, value in row.items():
                        row[key] = int(value)
                    obj_ins.append(cls.create(**row))
                return obj_ins
        except Exception:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw both square and rectangle object on the screen using turtle
        """

        turtle.screensize(1000, 500, "lightblue")
        turtle.title("Python as circle")
        pen = turtle.Turtle()
        pen.resizemode("user")
        pen.shapesize(0.5, 0.5, 0.5)
        pen.shape("triangle")
        pen.color("black", "#155370")
        pen.speed(1)
        pen.write("Rectangle Instances", align="center",
                  font=('Helvatica', 16, 'bold'))
        time.sleep(2)
        pen.clear()

        for rect in list_rectangles:
            width = rect.width
            height = rect.height
            x_ptime = rect.x
            y_ptime = rect.y
            area = rect.area()
            pen.penup()
            pen.goto(x_ptime, y_ptime)
            pen.rt(90)

            pen.begin_fill()  # fill the shape
            pen.pendown()
            pen.fd(height*3)
            pen.lt(90)
            pen.fd(width*3)
            pen.lt(90)
            pen.fd(height*3)
            pen.lt(90)
            pen.fd(width*3)
            pen.end_fill()
            pen.write("Area = {}m".format(area), False, align="left")
            pen.penup()
            pen.home()
            pen.clear()
        pen.write("Square Instances", align="center",
                  font=('Helvatica', 16, 'bold'))
        time.sleep(2)
        pen.clear()

        for sqr in list_squares:
            size = sqr.size
            x_ptime = sqr.x
            y_ptime = sqr.y
            area = sqr.area()
            pen.penup()
            pen.goto(x_ptime, y_ptime)
            pen.rt(90)

            pen.begin_fill()  # fill the shape
            pen.pendown()
            for i in range(4):
                pen.fd(size*3)
                pen.lt(90)
            pen.end_fill()
            pen.write("Area = {}m".format(area), False, align="left")
            pen.penup()
            pen.home()
            pen.clear()

        turtle.done()
