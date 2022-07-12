#!/usr/bin/python3
"""
A module for square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""

        return self.width

    @size.setter
    def size(self, value):
        """size setter"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates a Square instance"""

        flag = 0
        for i, arg in enumerate(args, start=1):
            if i == 1:
                self.id = arg
            elif i == 2:
                self.size = arg
            elif i == 3:
                self.x = arg
            elif i == 4:
                self.y = arg
            flag = 1
        if flag == 0:
            for kwarg, value in kwargs.items():
                if kwarg == "id":
                    self.id = value
                elif kwarg == "size":
                    self.size = value
                elif kwarg == "x":
                    self.x = value
                elif kwarg == "y":
                    self.y = value

    def to_dictionary(self):
        """creates a dictionary out of a given instance attributes"""

        sq_rect = dict()
        sq_rect["id"] = self.id
        sq_rect["size"] = self.size
        sq_rect["x"] = self.x
        sq_rect["y"] = self.y
        return sq_rect

    def __str__(self):
        """Returns a user friendly string representation of the rectangle"""

        cls = self.__class__.__name__
        size = self.height
        id = self.id
        x = self.x
        y = self.y

        return "[{}] ({}) {}/{} - {}".format(cls, id, x, y, size)
