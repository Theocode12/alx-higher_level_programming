"""
Test cases for Rectangle class
"""

from models import rectangle
import unittest
import json
import inspect
import pep8
Rectangle = rectangle.Rectangle

class TestRectangleDocs(unittest.TestCase):
    """
    Testing if docs are present and if the files are PEP valid
    """

    def test_rectangle_pep8_conformance(self):
        """Test if rectangle conforms to pep8 style"""

        pep_check = pep8.StyleGuide()
        result = pep_check.check_files(["models/rectangle.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docs(self):
        """checks if module documentation is present"""

        self.assertTrue(len(rectangle.__doc__) > 4)

    def test_cls_docs(self):
        """checks if class docs are present"""

        self.assertTrue(len(Rectangle.__doc__) > 4)

    def test_method_docs(self):
        """checks if method documentation are present"""

        methods = inspect.getmembers(Rectangle, inspect.isfunction)
        for method in methods:
            method = Rectangle.__name__ + '.' + method[0]
            self.assertTrue(len(eval(method).__doc__) > 4)

class TestRectangle(unittest.TestCase):
    """check that rectangles functionality"""

    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(1, 1)
        cls.r2 = Rectangle(3, 1, 1)
        cls.r3 = Rectangle(6, 1, 1, 1)
        cls.r4 = Rectangle(9, 1, 1, 1, 10)
    
    def test_object_id(self):
        """test object id"""

        self.assertEqual(self.r1.id, 12)
        self.assertEqual(self.r2.id, 13)
        self.assertEqual(self.r3.id, 14)
        self.assertEqual(self.r4.id, 10)
    
    def test_width_getter(self):
        """Test width property"""

        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r2.width, 3)
        self.assertEqual(self.r3.width, 6)
        self.assertEqual(self.r4.width, 9)
    
    def test_width_setter(self):
        """Test width setter."""

        self.r1.width = 14
        self.assertEqual(self.r1.width, 14)

    def test_width_setter_when_none(self):
        """Test setter when none is passed"""

        with self.assertRaises(TypeError):
            self.r1.width = None

    def test_width_setter_when_type_wrong(self):
        """test setter when wrong type is passed"""

        with self.assertRaises(TypeError):
            self.r2.width = "13"

    def test_width_when_neg_num_passed(self):
        """test setter when negative number is passed"""

        with self.assertRaises(ValueError):
            self.r2.width = -3

    def test_height_setter(self):
        """Test height setter."""

        self.r4.height = 14
        self.assertEqual(self.r4.height, 14)

    def test_height_setter_when_none(self):
        """Test setter when none is passed"""

        with self.assertRaises(TypeError):
            self.r4.height = None

    def test_height_setter_when_type_wrong(self):
        """test setter when wrong type is passed"""

        with self.assertRaises(TypeError):
            self.r2.height = "13"

    def test_width_when_neg_num_passed(self):
        """test setter when negative number is passed"""

        with self.assertRaises(ValueError):
            self.r4.height = -10



    def test_x_setter(self):
        """Test x setter."""

        self.r3.x = 14
        self.assertEqual(self.r3.x, 14)

    def test_x_setter_when_none(self):
        """Test setter when none is passed"""

        with self.assertRaises(TypeError):
            self.r3.x = None

    def test_x_setter_when_type_wrong(self):
        """test setter when wrong type is passed"""

        with self.assertRaises(TypeError):
            self.r2.x = "13"

    def test_x_when_neg_num_passed(self):
        """test setter when negative number is passed"""

        with self.assertRaises(ValueError):
            self.r4.x = -10


    def test_y_setter(self):
        """Test y setter."""

        self.r1.y = 3
        self.assertEqual(self.r1.y, 3)

    def test_y_setter_when_none(self):
        """Test setter when none is passed"""

        with self.assertRaises(TypeError):
            self.r1.y = None

    def test_y_setter_when_type_wrong(self):
        """test setter when wrong type is passed"""

        with self.assertRaises(TypeError):
            self.r1.y = "13"

    def test_y_when_neg_num_passed(self):
        """test setter when negative number is passed"""

        with self.assertRaises(ValueError):
            self.r4.y = -10

    def test_area(self):
        self.assertEqual(self.r1.area(), 1)
        self.assertEqual(self.r2.area(), 3)
        self.assertEqual(self.r3.area(), 6)
        self.assertEqual(self.r4.area(), 9)


