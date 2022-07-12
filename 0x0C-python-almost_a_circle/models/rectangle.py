#!/usr/bin/python3
"""
A rectangle module
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes object atrributes"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """position x getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """position y setter"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """get area of the rectangle"""

        return self.height * self.width

    def display(self):
        """print the instance using #"""

        row_shift = "\n"*self.y
        cols_shift = " "*self.x
        print(row_shift, end='')
        for row in range(self.height):
            print(cols_shift, end='')
            for col in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a user friendly string representation of the rectangle"""

        cls = self.__class__.__name__
        hg = self.height
        wd = self.width
        id = self.id
        x = self.x
        y = self.y

        return "[{}] ({}) {}/{} - {}/{}".format(cls, id, x, y, wd, hg)

    def update(self, *args, **kwargs):
        """updates a rectangle instance"""

        flag = 0
        for i, arg in enumerate(args, start=1):
            if i == 1:
                self.id = arg
            elif i == 2:
                self.width = arg
            elif i == 3:
                self.height = arg
            elif i == 4:
                self.x = arg
            elif i == 5:
                self.y = arg
            flag = 1
        if flag == 0:
            for kwarg, value in kwargs.items():
                if kwarg == "id":
                    self.id = value
                elif kwarg == "width":
                    self.width = value
                elif kwarg == "height":
                    self.height = value
                elif kwarg == "x":
                    self.x = value
                elif kwarg == "y":
                    self.y = value

    def to_dictionary(self):
        """creates a dictionary out of a given instance attributes"""

        rect_dict = dict()
        rect_dict["id"] = self.id
        rect_dict["width"] = self.width
        rect_dict["height"] = self.height
        rect_dict["x"] = self.x
        rect_dict["y"] = self.y
        return rect_dict
